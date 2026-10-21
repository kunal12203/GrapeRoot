"""Exercise the launcher's argument parsing without starting its MCP services."""
import json
import os
from pathlib import Path
import subprocess
import unittest


ROOT = Path(__file__).resolve().parents[1]
LAUNCHER = ROOT / "bin" / "dual_graph_launch.sh"


def route(*args, region="global_en", mode="openai", api_key="fixture"):
    # Stop before project initialization, downloads and telemetry. Execute the
    # actual parser so aliases, passthrough flags and exported auth are covered.
    source = LAUNCHER.read_text().split('DATA_DIR="$PROJECT/.dual-graph"', 1)[0]
    source += '''
export ROUTED_ASSISTANT="$ASSISTANT"
python3 - "${CLAUDE_EXTRA_ARGS[@]}" <<'PY'
import json, os, sys
print(json.dumps({"assistant": os.environ["ROUTED_ASSISTANT"],
                  "args": sys.argv[1:],
                  "base_url": os.environ.get("ANTHROPIC_BASE_URL"),
                  "auth_token": os.environ.get("ANTHROPIC_AUTH_TOKEN"),
                  "api_key": os.environ.get("ANTHROPIC_API_KEY"),
                  "context": os.environ.get("CLAUDE_CODE_AUTO_COMPACT_WINDOW")}))
PY
'''
    env = {"PATH": os.environ["PATH"], "HOME": str(ROOT), "LANG": "C.UTF-8",
           "MINIMAX_API_KEY": api_key, "MINIMAX_REGION": region,
           "MINIMAX_API_MODE": mode, "ANTHROPIC_API_KEY": "stale-fixture"}
    return subprocess.run(["bash", "-s", "--", "codex", str(ROOT), *args],
                          input=source, text=True, capture_output=True, env=env)


class MiniMaxRoutingTests(unittest.TestCase):
    def test_models_regions_and_protocols(self):
        models = {
            "minimax": ("MiniMax-M3.1-Flash", 1000000),
            "minimax-m3.1-flash": ("MiniMax-M3.1-Flash", 1000000),
            "MiniMax-M3.1-Flash": ("MiniMax-M3.1-Flash", 1000000),
            "minimax-m3": ("MiniMax-M3", 1000000),
            "MiniMax-M3": ("MiniMax-M3", 1000000),
            "minimax-m2.7": ("MiniMax-M2.7", 204800),
            "MiniMax-M2.7": ("MiniMax-M2.7", 204800),
        }
        for alias, (model, context) in models.items():
            for region, host in (("global_en", "api.minimax.io"),
                                 ("cn_zh", "api.minimaxi.com")):
                for mode in ("openai", "anthropic"):
                    with self.subTest(alias=alias, region=region, mode=mode):
                        result = route(f"--model={alias}", region=region, mode=mode)
                        self.assertEqual(result.returncode, 0, result.stderr)
                        routed = json.loads(result.stdout)
                        self.assertEqual(routed["args"][:2], ["--model", model])
                        if mode == "openai":
                            self.assertEqual(routed["assistant"], "codex")
                            self.assertIn(f'model_providers.minimax.base_url="https://{host}/v1"', routed["args"])
                            self.assertIn('model_providers.minimax.wire_api="responses"', routed["args"])
                            self.assertIn(f"model_context_window={context}", routed["args"])
                        else:
                            self.assertEqual(routed["assistant"], "claude")
                            self.assertEqual(routed["base_url"], f"https://{host}/anthropic")
                            self.assertEqual(routed["auth_token"], "fixture")
                            self.assertIsNone(routed["api_key"])
                            self.assertEqual(routed["context"], str(context))

    def test_custom_and_non_minimax_model_passthrough(self):
        for args in (("--model=custom-model",), ("--model", "saved-model"),
                     ("--model=opus",), ("--model=MiniMax-M2.1",)):
            with self.subTest(args=args):
                result = route(*args)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(json.loads(result.stdout)["args"], list(args))

    def test_explicit_effort_passthrough(self):
        result = route("--model=minimax", "--effort", "high", mode="anthropic")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["args"][-2:], ["--effort", "high"])

    def test_invalid_configuration(self):
        for options in ({"region": "invalid"}, {"mode": "invalid"}, {"api_key": ""}):
            with self.subTest(options=options):
                result = route("--model=minimax", **options)
                self.assertEqual(result.returncode, 2)
                self.assertIn("must be", result.stderr)


if __name__ == "__main__":
    unittest.main()

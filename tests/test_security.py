import importlib.util
import logging
import os
from pathlib import Path
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
class SecurityTests(unittest.TestCase):
    def test_missing_or_short_key_fails_closed(self):
        for value in (None, "short"):
            with patch.dict(os.environ, {}, clear=True), patch("dotenv.load_dotenv"):
                if value is not None:
                    os.environ["SECRET_KEY"] = value
                spec = importlib.util.spec_from_file_location("isolated_config", ROOT / "config.py")
                module = importlib.util.module_from_spec(spec)
                with self.assertRaises(RuntimeError):
                    spec.loader.exec_module(module)

    def test_ticket_form_does_not_log_submitted_value(self):
        with patch.dict(os.environ, {"SECRET_KEY": "synthetic-test-key-" * 4}), patch("dotenv.load_dotenv"):
            from app import app
            with patch("app.routes.log") as logger:
                response = app.test_client().post("/ticket", data={"nt": "private-form-sentinel"})
                self.assertEqual(response.status_code, 200)
                self.assertNotIn("private-form-sentinel", str(logger.mock_calls))

if __name__ == "__main__":
    unittest.main()

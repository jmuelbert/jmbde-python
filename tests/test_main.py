# test_main.py
import unittest
from unittest.mock import patch

from jmbde.main import main


class TestMainCLI(unittest.TestCase):
    @patch("jmbde.main.gui_main")
    @patch("jmbde.main.start_api_server")
    @patch("jmbde.main.logging")
    def test_main_gui_mode(self, mock_logging, mock_start_api_server, mock_gui_main):
        with patch("sys.argv", ["main.py", "--mode", "gui"]):
            main()
            mock_logging.info.assert_called_with("Starting JMBDE GUI...")
            mock_gui_main.assert_called_once()

    @patch("jmbde.main.gui_main")
    @patch("jmbde.main.start_api_server")
    @patch("jmbde.main.logging")
    def test_main_api_mode(self, mock_logging, mock_start_api_server, mock_gui_main):
        with patch("sys.argv", ["main.py", "--mode", "api"]):
            main()
            mock_logging.info.assert_called_with("Starting JMBDE API server...")
            mock_start_api_server.assert_called_once()

    @patch("jmbde.main.logging")
    def test_main_unknown_mode(self, mock_logging):
        with patch("sys.argv", ["main.py", "--mode", "unknown"]):
            with self.assertRaises(SystemExit):
                main()
            mock_logging.error.assert_called_with("Unknown mode: unknown")


if __name__ == "__main__":
    unittest.main()

# test_main.py
import sys
import unittest
from unittest.mock import MagicMock, patch

from jmbde.__main__ import main as gui_main


class TestMain(unittest.TestCase):
    @patch("jmbde.__main__.QGuiApplication")
    @patch("jmbde.__main__.QQmlApplicationEngine")
    @patch("jmbde.__main__.DatabaseConnection")
    @patch("jmbde.__main__.EmployeeModel")
    @patch("jmbde.__main__.MainApp")
    @patch("jmbde.__main__.logging")
    def test_main(
        self,
        mock_logging,
        mock_main_app,
        mock_employee_model,
        mock_db_connection,
        mock_engine,
        mock_qgui_app,
    ):
        mock_engine.return_value.rootObjects.return_value = [MagicMock()]

        with patch("sys.exit") as mock_exit:
            gui_main()
            mock_logging.info.assert_called_with("Starting JMBDE GUI application...")
            mock_exit.assert_called_once_with(mock_qgui_app.exec.return_value)

    @patch("jmbde.__main__.QQmlApplicationEngine")
    def test_main_fail_to_load_qml(self, mock_engine):
        mock_engine.return_value.rootObjects.return_value = []

        with self.assertRaises(SystemExit):
            gui_main()


if __name__ == "__main__":
    unittest.main()

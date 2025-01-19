from PySide6.QtWidgets import QFileDialog


def test_file_dialog(monkeypatch, qtbot):
    def mock_get_open_file_name(*args, **kwargs):
        return "/path/to/file.txt", "Text Files (*.txt)"

    monkeypatch.setattr(QFileDialog, "getOpenFileName", mock_get_open_file_name)

    filename, _ = QFileDialog.getOpenFileName()
    assert filename == "/path/to/file.txt"

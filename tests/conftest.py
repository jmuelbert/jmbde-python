import io

import pytest
from PySide6.QtCore import QBuffer, QByteArray
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication


@pytest.fixture
def screenshot(qtbot):
    """Fixture to take a screenshot of the application window."""
    # Create a QApplication instance if it doesn't exist
    app = QApplication.instance() or QApplication([])

    # Get the primary screen
    screen = app.primaryScreen()

    # Take a screenshot
    screenshot = screen.grabWindow(0)  # 0 is the ID of the main window

    # Create a QByteArray to hold the screenshot data
    byte_array = QByteArray()
    qbuffer = QBuffer(byte_array)  # Wrap the QByteArray in a QBuffer
    qbuffer.open(QBuffer.ReadWrite)  # Open the buffer for reading and writing

    # Save the screenshot to the QBuffer
    screenshot.save(qbuffer, "PNG")
    qbuffer.close()  # Close the buffer

    # Return the byte array as bytes
    return byte_array.data()  # Convert QByteArray to bytes

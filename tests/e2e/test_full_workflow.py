def test_full_workflow(qtbot):
    window = MyWindow()
    qtbot.addWidget(window)

    # Step 1: Type in the text field
    qtbot.keyClicks(window.edit, "Test Input")
    assert window.edit.text() == "Test Input"

    # Step 2: Submit the input
    qtbot.mouseClick(window.button, Qt.LeftButton)
    assert window.edit.text() == "Submitted!"

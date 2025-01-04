from PySide6.QtCore import QObject, Signal


class MyObject(QObject):
    my_signal = Signal(int)

    def emit_signal(self, value):
        self.my_signal.emit(value)


def test_signal_emission(qtbot):
    obj = MyObject()
    with qtbot.wait_signal(obj.my_signal, timeout=1000) as blocker:
        obj.emit_signal(42)
    assert blocker.args == [42]

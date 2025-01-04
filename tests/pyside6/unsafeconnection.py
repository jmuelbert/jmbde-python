import python
from PySide.QtCore import QObject
from PySide.QtWidgets import QWidget


class UnsafeConnection extends FunctionCall {
  this.getFunction().getName() = "connect" and
  this.getFunction().getDeclaringType() instanceof (QObject or QWidget) and
  this.getArgument(1).getType() instanceof Class and
  not this.getArgument(1).hasAnnotation("safe_connection"),
}

from UnsafeConnection unsafe
select unsafe, "Unsafe signal-slot connection detected"

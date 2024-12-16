#
#   jmbde a BDE Tool for datacontext
#   Copyright (C) 2018-2020  Jürgen Mülbert
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
"""The Application Class."""
import locale
import os
import sys

from gui.mainwindow import MainWindow
from PySide2.QtCore import QTranslator
from PySide2.QtWidgets import QApplication, QIcon
from utils import CONF_DIR, IMAGES_DIR, TRANSLATION_DIR


def run():
    """Run the Gui."""
    os.environ["QT_QUICK_CONTROLS_CONF"] = (
        (CONF_DIR / "qtquickcontrols2.conf").resolve().as_posix()
    )

    app = QApplication(sys.argv)

    lang = locale.getdefaultlocale()[0]
    lang_file_path = (
        (TRANSLATION_DIR / f"jmbde_{lang}.qm").resolve().as_posix()
    )
    translator = QTranslator()
    translator.load(lang_file_path)
    app.installTranslator(translator)

    icon_file_path = (IMAGES_DIR / "jmbde.png").resolve().as_posix()
    app.setWindowIcon(QIcon(icon_file_path))

    main_window = MainWindow(app, translator)
    main_window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    run()

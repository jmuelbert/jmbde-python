# -*- coding: utf-8 -*-
import sys

from gui.mainwindow import MainWindow
from PySide2.QtCore import QLocale
from PySide2.QtCore import QTranslator
from PySide2.QtWidgets import QApplication


def run():
    app_path = os.path.abspath(os.path.dirname(sys.argv[0]))
    os.environ["QT_QUICK_CONTROLS_CONF"] = (
        (CONF_DIR / "qtquickcontrols2.conf").resolve().as_posix()
    )

    app = QApplication(sys.argv)

    lang = locale.getdefaultlocale()[0]
    lang_file_path = (
        (TRANSLATION_DIR / "jmbde_{lang}.qm".format(lang=lang)).resolve().as_posix()
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

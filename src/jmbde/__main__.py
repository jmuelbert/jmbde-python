import argparse
import logging
import sys
from pathlib import Path

from PySide6.QtCore import QUrl
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

from jmbde.core.db_handler import DBHandler
from jmbde.gui.main_app import MainApp
from jmbde.models.employee import EmployeeModel
from jmbde.utils.exceptions import DatabaseError

logger = logging.getLogger(__name__)


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="JMBDE Application")
    parser.add_argument(
        "--db-path", type=str, default="data/jmbde.db", help="Path to database file"
    )
    return parser.parse_args()


def main():
    """Initialize and start the JMBDE GUI application."""
    try:
        # Set up logging
        logging.basicConfig(level=logging.INFO)
        logger.info("Starting JMBDE GUI application...")

        # Parse arguments
        args = parse_args()
        db_path = Path(args.db_path)

        # Ensure database directory exists
        db_path.parent.mkdir(parents=True, exist_ok=True)

        # Check for existing QApplication instance
        app = QGuiApplication.instance()
        if app is not None:
            app.quit()
            app = None

        # Initialize application
        app = QGuiApplication(sys.argv)
        engine = QQmlApplicationEngine()

        try:
            # Initialize database
            db_handler = DBHandler(db_path)

            # Initialize models and main app
            model = EmployeeModel(database=db_handler.db)
            main_app = MainApp(db_handler=db_handler)

            # Set up QML context
            engine.rootContext().setContextProperty("mainApp", main_app)
            engine.rootContext().setContextProperty("employeeModel", model)

            # Load QML
            engine.load(QUrl("qrc:/qml/main.qml"))

            if not engine.rootObjects():
                logger.error("Failed to load QML")
                return sys.exit(-1)

            # Start event loop
            return_code = app.exec()

            # Cleanup
            db_handler.cleanup()
            engine.deleteLater()

            return sys.exit(return_code)

        except DatabaseError as e:
            logger.error(f"Database error: {e}")
            return sys.exit(1)

    except Exception as e:
        logger.error(f"Application error: {e}")
        return sys.exit(1)
    finally:
        # Ensure cleanup
        if "db_handler" in locals():
            db_handler.cleanup()
        if "engine" in locals():
            engine.deleteLater()


if __name__ == "__main__":
    main()

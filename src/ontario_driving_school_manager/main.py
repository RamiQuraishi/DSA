"""
Main application module for the Ontario Driving School Manager.
"""

import sys
from PyQt5.QtWidgets import QApplication
from loguru import logger

from ontario_driving_school_manager.config.settings import load_settings
from ontario_driving_school_manager.config.logging import setup_logging

def main():
    """
    Main entry point for the application.
    Sets up logging, loads configuration, and starts the GUI application.
    """
    # Setup logging
    setup_logging()
    logger.info("Starting Ontario Driving School Manager")

    # Load application settings
    settings = load_settings()
    logger.debug(f"Loaded settings: {settings}")

    # Initialize Qt Application
    app = QApplication(sys.argv)
    app.setApplicationName("Ontario Driving School Manager")
    app.setApplicationVersion("0.1.0")

    # TODO: Initialize main window and show it
    # main_window = MainWindow()
    # main_window.show()

    # Start the event loop
    sys.exit(app.exec_())

if __name__ == "__main__":
    main() 
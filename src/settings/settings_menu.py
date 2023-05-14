from PyQt5.QtWidgets import QMenu, QAction
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QCursor

from .settings_window import SettingsWindow
from .settings_manager import SettingsManager


class SettingsMenu(QMenu):
    def __init__(self, settings_manager: SettingsManager, parent=None):
        super().__init__(parent)
        self.settings_manager = settings_manager

        self.settings_action = QAction("Settings", self)
        self.settings_action.triggered.connect(self.open_settings_window)
        self.addAction(self.settings_action)

        self.toggleModeAction = QAction('Toggle light/dark mode', self)
        self.toggleModeAction.triggered.connect(
            self.settings_manager.theme_manager.toggle_mode)
        self.addAction(self.toggleModeAction)

        self.changeLanguageAction = QAction('Change language', self)
        # Need a mechanism to select language
        # self.changeLanguageAction.triggered.connect(
        #     self.settings_manager.user_settings.change_language)
        self.addAction(self.changeLanguageAction)

        self.changeFontAction = QAction('Change font', self)
        # We already change font from settings window, so we may not need this.
        # self.changeFontAction.triggered.connect(self.settings_manager.font_manager.change_font)
        self.addAction(self.changeFontAction)

    def open_settings_window(self):
        self.settings_window = SettingsWindow(self.settings_manager, self)
        self.settings_window.show()
        
    def exec_(self, point=None):
        if point is None:
            super().popup(QCursor.pos())
        else:
            super().popup(point)

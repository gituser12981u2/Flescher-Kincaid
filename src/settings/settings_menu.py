from PyQt5.QtWidgets import QMenu, QAction
from .user_settings import UserSettings
from .settings_window import SettingsWindow


class SettingsMenu(QMenu):
    def __init__(self, settings_manager, parent=None):
        super(SettingsMenu, self).__init__('Settings', parent)
        self.settings_manager = settings_manager

        self.showSettingsAction = QAction('Show settings', self)
        self.showSettingsAction.triggered.connect(self.show_settings)
        self.addAction(self.showSettingsAction)

        self.toggleModeAction = QAction('Toggle light/dark mode', self)
        self.toggleModeAction.triggered.connect(
            self.settings_manager.user_settings.toggle_mode)
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

    def show_settings(self):
        settings_window = SettingsWindow(self.settings_manager, self.parent())
        settings_window.exec_()

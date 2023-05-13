from PyQt5.QtWidgets import QMenu, QAction
from .user_settings import UserSettings
from .settings_window import SettingsWindow


class SettingsMenu(QMenu):
    def __init__(self, main_window, parent=None):
        super(SettingsMenu, self).__init__('Settings', parent)
        self.settings = UserSettings(main_window)

        self.showSettingsAction = QAction('Show settings', self)
        self.showSettingsAction.triggered.connect(self.show_settings)
        self.addAction(self.showSettingsAction)

        self.toggleModeAction = QAction('Toggle light/dark mode', self)
        self.toggleModeAction.triggered.connect(self.settings.toggle_mode)
        self.addAction(self.toggleModeAction)

        self.changeLanguageAction = QAction('Change language', self)
        self.changeLanguageAction.triggered.connect(
            self.settings.change_language)
        self.addAction(self.changeLanguageAction)

        self.changeFontAction = QAction('Change font', self)
        self.changeFontAction.triggered.connect(self.settings.change_font)
        self.addAction(self.changeFontAction)

    def show_settings(self):
        settings_window = SettingsWindow(self.settings, self.parent())
        settings_window.exec_()

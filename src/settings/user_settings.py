import json
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import qApp

from .theme_manager import ThemeManager


class UserSettings:
    def __init__(self, settings_file='settings.json'):
        self.settings_file = settings_file
        self.theme_manager = ThemeManager(self)
        self.settings = self.load_settings()

    def load_settings(self):
        try:
            with open(self.settings_file, 'r') as file:
                settings = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            settings = self.default_settings()
            self.settings = settings
            self.save_settings()
        font = QFont()
        font.fromString(settings['font'])
        font.setPointSize(16)  # Set the desired font size
        settings['font'] = font.toString()
        return settings

    def save_settings(self):
        with open(self.settings_file, 'w') as file:
            json.dump(self.settings, file)

    def default_settings(self):
        return {
            'font': 'Arial',
            'change_application_font': False,
            'mode': self.theme_manager.get_system_theme(),
            'day/night auto': False,
        }

    def get_settings(self):
        return self.settings

    def update_settings(self, new_settings):
        if not self.settings.get('day/night auto', False):
            self.settings.update(new_settings)
            self.save_settings()

    def toggle_application_font(self):
        self.settings['change_application_font'] = not self.settings['change_application_font']
        self.save_settings()

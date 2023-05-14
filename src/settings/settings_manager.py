from .user_settings import UserSettings
from .font_manager import FontManager

class SettingsManager:
    def __init__(self, main_window):
        self.user_settings = UserSettings(main_window, 'settings.json')
        self.font_manager = FontManager(main_window, self.user_settings)
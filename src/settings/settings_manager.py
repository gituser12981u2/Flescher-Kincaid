from .theme_manager import ThemeManager
from .user_settings import UserSettings
from .font_manager import FontManager

class SettingsManager:
    def __init__(self, main_window):
        self.user_settings = UserSettings('settings.json')
        self.font_manager = FontManager(main_window, self.user_settings)
        self.theme_manager = ThemeManager(self.user_settings)
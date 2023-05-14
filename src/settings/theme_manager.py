from datetime import datetime
from geopy.geocoders import Nominatim
from astral.sun import sun
from astral import LocationInfo

import pytz
import requests
import json

from PyQt5.QtWidgets import qApp

import darkdetect

from tzwhere.tzwhere import tzwhere

from timezonefinder import TimezoneFinder


class ThemeManager:
    def __init__(self, user_settings):
        self.user_settings = user_settings
        self.stylesheet_light = open('src/styles/light.qss', 'r').read()
        self.stylesheet_dark = open('src/styles/dark.qss', 'r').read()

    def load_stylesheet(self):
        if self.user_settings.settings['mode'] == 'light':
            qApp.setStyleSheet(self.stylesheet_light)
        else:
            qApp.setStyleSheet(self.stylesheet_dark)

    def get_system_location(self):
        try:
            ip_request = requests.get('https://get.geojs.io/v1/ip.json')
            ip_info = ip_request.json()
            latitude = ip_info.get('lat')
            longitude = ip_info.get('lon')
            if latitude and longitude:
                tf = TimezoneFinder()
                tz_str = tf.timezone_at(lng=longitude, lat=latitude)
                if tz_str:
                    return latitude, longitude, tz_str
            return None, None, None
        except requests.exceptions.RequestException:
            return None, None, None

    def get_sunrise_sunset_based_mode(self):
        latitude, longitude, timezone_str = self.get_system_location()
        if latitude and longitude and timezone_str:
            location_info = LocationInfo("", latitude, longitude)
            timezone = pytz.timezone(timezone_str)
            now = datetime.now(timezone)
            s = sun(location_info.observer,
                    date=now.date())

            print(location_info)
            print(timezone)
            print(now)

            if s['sunrise'] <= now <= s['sunset']:
                return 'light'  # switch to light
            else:
                return 'dark'  # switch to dark
        else:
            if latitude is None or longitude is None or timezone_str is None:
                now = datetime.now()
                if 6 <= now.hour < 18:
                    return 'light'  # switch to light
                else:
                    return 'dark'  # switch to dark

    def toggle_mode(self):
        self.user_settings.settings['mode'] = 'dark' if self.user_settings.settings['mode'] == 'light' else 'light'
        self.load_stylesheet()
        if not self.user_settings.settings['day/night auto']:
            self.user_settings.save_settings()

    def get_system_theme(self):
        theme = darkdetect.theme()
        return theme.lower() if theme else 'light'

    def get_current_mode(self):
        if self.user_settings.settings.get('day/night auto', False):
            return self.get_sunrise_sunset_based_mode()
        else:
            return self.get_system_theme()

    # add somewhere else later

    def change_language(self, language):
        self.user_settings.settings['language'] = language
        self.user_settings.save_settings()

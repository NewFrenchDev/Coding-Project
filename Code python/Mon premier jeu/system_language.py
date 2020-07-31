import locale
import ctypes
import pygame

class OsLanguage:

    def __init__(self):
        self.windll = ctypes.windll.kernel32
        self.user_default_language = ''

    def check_user_default_language(self):
        self.user_default_language = locale.windows_locale[self.windll.GetUserDefaultUILanguage()]
        if self.user_default_language == 'fr_FR':
            pygame.K_q = ord('a')
            pygame.K_a = ord('q')
            pygame.K_z = ord('w')
            pygame.K_w = ord('z')

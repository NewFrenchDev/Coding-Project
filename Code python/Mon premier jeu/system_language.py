import locale
import ctypes
import pygame
import platform

class OsLanguage:

    def __init__(self):
        self.windll = ''
        self.user_default_language = ''
        self.user_platform = ''

    def check_user_os(self):
        # Verifier l'OS du joueur
        user_platform = platform.system()
        # Si Window --> Vérifier le language du systeme du joueur
        if user_platform == 'Windows':
            self.check_user_default_language()

    def check_user_default_language(self):
        self.windll = ctypes.windll.kernel32
        self.user_default_language = locale.windows_locale[self.windll.GetUserDefaultUILanguage()]
        if self.user_default_language == 'fr_FR':
            pygame.K_q = ord('a')
            pygame.K_a = ord('q')
            pygame.K_z = ord('w')
            pygame.K_w = ord('z')

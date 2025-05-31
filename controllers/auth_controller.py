from kivy.uix.screenmanager import Screen
from models.user_model import User
from views.auth.login import LoginScreen
from views.auth.register import RegisterScreen

class AuthController:
    def __init__(self, app):
        self.app = app
        self.current_user = None

    def load_views(self):
        """Carga las pantallas de autenticación"""
        self.app.sm.add_widget(LoginScreen(name='login', controller=self))
        self.app.sm.add_widget(RegisterScreen(name='register', controller=self))
        self.app.sm.current = 'login'

    def login(self, username, password):
        """Maneja el proceso de login"""
        if User.verify_password(username, password):
            self.current_user = User.get_by_username(username)
            self.app.character_controller.load_views()
            self.app.favorites_controller.load_views()
            self.app.sm.current = 'characters_list'
            return True
        return False

    def register(self, username, password):
        """Maneja el proceso de registro"""
        if len(username) < 4 or len(password) < 6:
            return False, "Usuario (min 4 chars) y contraseña (min 6 chars)"
            
        if User.create(username, password):
            return True, "Registro exitoso"
        return False, "El usuario ya existe"

    def logout(self):
        """Maneja el proceso de logout"""
        self.current_user = None
        self.app.sm.current = 'login'
        self.app.sm.clear_widgets()
        self.load_views()
        print("[DEBUG] Usuario cerró sesión")

    def is_authenticated(self):
        """Verifica si hay un usuario autenticado"""
        return self.current_user is not None
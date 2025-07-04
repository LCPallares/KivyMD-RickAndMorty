from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty

class LoginScreen(MDScreen):
    error_message = StringProperty('')

    def __init__(self, **kwargs):
        self.controller = kwargs.pop('controller')
        super().__init__(**kwargs)

    def attempt_login(self):
        username = self.ids.username_input.text
        password = self.ids.password_input.text
        
        if self.controller.login(username, password):
            self.error_message = ''
        else:
            self.error_message = 'Usuario o contraseña incorrectos'
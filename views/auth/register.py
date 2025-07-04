from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty

class RegisterScreen(MDScreen):
    error_message = StringProperty('')
    success_message = StringProperty('')

    def __init__(self, **kwargs):
        self.controller = kwargs.pop('controller')
        super().__init__(**kwargs)

    def attempt_register(self):
        username = self.ids.username_input.text
        password = self.ids.password_input.text
        confirm_password = self.ids.confirm_password_input.text
        
        if not username or not password:
            self.error_message = 'Usuario y contraseña son requeridos'
            self.success_message = ''
            return
            
        if password != confirm_password:
            self.error_message = 'Las contraseñas no coinciden'
            self.success_message = ''
            return
            
        if self.controller.register(username, password):
            self.error_message = ''
            self.success_message = 'Registro exitoso! Redirigiendo...'
            # Redirigir después de 1 segundo
            from kivy.clock import Clock
            Clock.schedule_once(lambda dt: self.redirect_to_login(), 1.5)
        else:
            self.error_message = 'El usuario ya existe'
            self.success_message = ''

    def redirect_to_login(self):
        self.manager.current = 'login'
        self.reset_form()

    def reset_form(self):
        self.ids.username_input.text = ''
        self.ids.password_input.text = ''
        self.ids.confirm_password_input.text = ''
        self.error_message = ''
        self.success_message = ''
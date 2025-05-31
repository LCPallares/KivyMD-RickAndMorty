#from kivy.app import App
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from controllers.auth_controller import AuthController
from controllers.character_controller import CharacterController
from controllers.favorites_controller import FavoritesController


#class RickMortyApp(App):
class RickMortyApp(MDApp):
    def build(self):
        self.sm = ScreenManager()
        
        # Inicializar controladores
        self.auth_controller = AuthController(self)
        self.character_controller = CharacterController(self)
        self.favorites_controller = FavoritesController(self)
        
        # Cargar pantallas de autenticación
        self.auth_controller.load_views()
        
        return self.sm

if __name__ == '__main__':
    RickMortyApp().run()

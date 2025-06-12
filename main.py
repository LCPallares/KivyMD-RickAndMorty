from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from controllers.auth_controller import AuthController
from controllers.character_controller import CharacterController
from controllers.favorites_controller import FavoritesController


class RickMortyApp(MDApp):
    def build(self):

        # Configuración específica de MD3
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.material_style = "M3"
        self.theme_cls.dynamic_color = False  # Desactivar si no quieres color dinámico
        
        # Carga el archivo KV principal que define la estructura de la UI
        from kivy.lang import Builder
        self.root_kv = Builder.load_file("views/main.kv")
        # Accede al ScreenManager definido en main.kv usando su ID
        #self.sm = ScreenManager()
        self.sm = self.root_kv.ids.screen_manager
        
        # Inicializar controladores
        self.auth_controller = AuthController(self)
        self.character_controller = CharacterController(self)
        self.favorites_controller = FavoritesController(self)
        
        # Cargar pantallas de autenticación
        self.auth_controller.load_views()
        
        #return self.sm
        # Devuelve el widget raíz de la aplicación
        return self.root_kv

if __name__ == '__main__':
    RickMortyApp().run()

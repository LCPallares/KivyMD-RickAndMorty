from kivymd.uix.imagelist import MDSmartTile
from kivy.properties import NumericProperty, BooleanProperty, StringProperty

from kivy.lang import Builder
Builder.load_file('components/character_tile.kv')

class CharacterTile(MDSmartTile):
    """Versión ultra-minimalista con manejo seguro de IDs"""
    character_id = NumericProperty(0)
    is_favorite = BooleanProperty(False)
    character_name = StringProperty('')
    character_source = StringProperty('')  # kivymd 2.0.1.dev0

    def __init__(self, character, controller, **kwargs):
        super().__init__(**kwargs)
        self.character = character
        self.controller = controller
        self.character_id = character.get('id', 0)
        self.character_name = character.get('name', 'Nombre No Disponible')
        self.character_source = character.get('image', "assets/placeholder_error.png")
        self.is_favorite = self.controller.is_favorite(self.character_id) if self.controller else False
        self.bind(is_favorite=self.update_favorite_icon)

    def on_press(self):
        self.controller.app.sm.current = 'character_detail'
        character_detail_screen = self.controller.app.sm.get_screen('character_detail')
        character_detail_screen.character = self.character
        character_detail_screen.controller = self.controller

        # character_detail_screen.is_favorite = self.is_favorite
        character_detail_screen.character_tile = self
        # character_detail_screen.character_tile.is_favorite = self.is_favorite
        # print(f'self.is_favorite de on_press del tile es: {self.is_favorite}')
        # print(f'self.is_favorite de on_press: {character_detail_screen.character_tile.is_favorite}')

    def toggle_favorite(self, *args):
        """ Alterna el estado de favorito del personaje a través del controlador. """
        success = self.controller.toggle_favorite(self.character)        
        if success:
            self.is_favorite = not self.is_favorite
            print(f"Estado de favorito para {self.character_name} cambiado a: {self.is_favorite}")
        else:
            print(f"Fallo al alternar favorito para {self.character_name}.")

    def toggle_favorite0(self, *args):  # 5b version con controlador retornando boleano
        """ Alterna el estado de favorito del personaje a través del controlador. """
        self.is_favorite = self.controller.toggle_favorite(self.character) # True/False despues de add/delete fav
        print(f"Estado de favorito para {self.character_name} cambiado a: {self.is_favorite}")

    def update_favorite_icon(self, instance, value):
        """Actualiza el estado del ícono basado en la base de datos"""
        if self.controller:
            self.is_favorite = self.controller.is_favorite(self.character_id)
        else:
            self.is_favorite = False



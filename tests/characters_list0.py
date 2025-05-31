

n = 00000000000000000000000000000000000000000000000000000000000000000000000000000000000000


from kivymd.uix.imagelist import MDSmartTile

class CharacterTile1(MDSmartTile):
    """Tile personalizado para cada personaje"""
    def __init__(self, character, controller, **kwargs):
        super().__init__(**kwargs)
        self.character = character
        self.controller = controller
        self.source = character['image']
        self.ids.character_image_text.text = character['name']
        self.update_favorite_icon()

    def update_favorite_icon(self):
        """Actualiza el ícono del corazón según el estado"""
        is_fav = self.controller.is_favorite(self.character['id'])
        self.ids.favorite_icon.icon = "heart" if is_fav else "heart-outline"

    def toggle_favorite(self):
        """Alterna entre favorito/no favorito"""
        success = self.controller.toggle_favorite(self.character)
        if success:
            self.update_favorite_icon()

    def on_press(self):
        """Maneja el clic en el tile"""
        self.toggle_favorite()


 ---------------------------------------------------------------------------------------- self self
n = 00000000000000000000000000000000000000000000000000000000000000000000000000000000000000
 ---------------------------------------------------------------------------------------- self self


 ---------------------------------------------------------------------------------------- self self
n = 00000000000000000000000000000000000000000000000000000000000000000000000000000000000000
 ---------------------------------------------------------------------------------------- self self

from kivy.uix.screenmanager import Screen
from kivy.properties import ListProperty
from kivy.clock import Clock
from kivy.metrics import dp
from utils.api_client import RickMortyAPI
from components.character_tile import CharacterTile


class CharactersListScreen(Screen):
    characters = ListProperty([])
    current_page = 1

    def __init__(self, **kwargs):
        self.controller = kwargs.pop('controller')
        super().__init__(**kwargs)
        Clock.schedule_once(lambda dt: self.load_characters())

    def load_characters(self):
        characters_data = self.controller.get_characters(self.current_page)
        grid = self.ids.characters_grid
        grid.clear_widgets()
        
        for character in characters_data:
            tile = CharacterTile(
                character_id=character['id'],
                character_name=character['name'],
                character_image=character['image'],
                is_favorite=self.controller.is_favorite(character['id']),
                tile_size="180dp",
                overlay_color=[0.2, 0.2, 0.3, 0.6]
            )
            tile.bind(on_favorite_toggled=self.on_favorite_toggled)
            grid.add_widget(tile)

    def on_favorite_toggled(self, instance, character_id, is_favorite):
        """Maneja el evento de favorito"""
        character = next(c for c in self.controller.get_characters(self.current_page) 
                   if c['id'] == character_id)
        self.controller.toggle_favorite(character)

n = 00000000000000000000000000000000000000000000000000000000000000000000000000000000000000
from kivy.uix.screenmanager import Screen
from kivy.properties import ListProperty
from kivy.clock import Clock
from kivy.metrics import dp
from utils.api_client import RickMortyAPI
from components.character_tile import CharacterTile


class CharactersListScreen(Screen):
    characters = ListProperty([])
    current_page = 1

    def __init__(self, **kwargs):
        self.controller = kwargs.pop('controller')
        super().__init__(**kwargs)
        Clock.schedule_once(lambda dt: self.load_characters())

    # def on_enter(self):
    #     self.load_characters()

    def load_characters(self):
        characters_data = self.controller.get_characters(self.current_page)
        grid = self.ids.characters_grid
        grid.clear_widgets()
        
        for character in characters_data:
            print(character['image'], character['name'])
            tile = CharacterTile(
                character_id=character['id'],
                character_name=character['name'],
                character_image=character['image'],
                is_favorite=self.controller.is_favorite(character['id']),
                tile_size=dp(180)
            )
            tile.bind(on_favorite_toggled=self.on_favorite_toggled)
            grid.add_widget(tile)
        
        # for x in range(10):
        #     from kivy.uix.button import Button
        #     #tile = CharacterTile(text="111111")
        #     tile = CharacterTile(character_image='https://rickandmortyapi.com/api/character/avatar/2.jpeg')
        #     tile.ids.inner_button.text = tile.character_image
        #     # tile = CharacterTile(
        #     #     character_id=1,
        #     #     character_name="fjdfjd",
        #     #     character_image='https://rickandmortyapi.com/api/character/avatar/2.jpeg',
        #     #     is_favorite=False,
        #     #     tile_size=dp(180)
        #     # )
        #     #tile.bind(on_favorite_toggled=self.on_favorite_toggled)
        #     grid.add_widget(tile)

    def on_favorite_toggled(self, instance, character_id, is_favorite):
        """Maneja el evento de favorito"""
        character = next(c for c in self.controller.get_characters(self.current_page) 
                   if c['id'] == character_id)
        self.controller.toggle_favorite(character)


***************************************************************************************** self self
n = 00000000000000000000000000000000000000000000000000000000000000000000000000000000000000 
***************************************************************************************** self self
from kivy.uix.screenmanager import Screen
from kivy.properties import ListProperty
from kivy.clock import Clock
from kivy.metrics import dp
from utils.api_client import RickMortyAPI
from components.character_tile import CharacterTile


class CharactersListScreen(Screen):
    characters = ListProperty([])
    current_page = 1

    def __init__(self, **kwargs):
        self.controller = kwargs.pop('controller')
        super().__init__(**kwargs)
        Clock.schedule_once(lambda dt: self.load_characters())
        #print(111, self.ids)

    def load_characters(self):
        characters_data = self.controller.get_characters(self.current_page)
        grid = self.ids.characters_grid
        grid.clear_widgets()
        
        for character in characters_data:
            tile = CharacterTile(
                source=character['image'],
                character_id=character['id'],
                character_name=character['name'],  # Asignamos el nombre directamente
                is_favorite=self.controller.is_favorite(character['id'])
            )
            #tile.ids.name_label.text = character['name']  # Asignamos el texto directamente
            #tile.ids.name_label.text = "Rick Sanchez"  # Asignación directa
            #tile.character_name = "Morty Smith"  # Se actualiza automáticamente
            #print(222, tile.ids)
            tile.bind(on_favorite_toggled=self.on_favorite_toggled)
            grid.add_widget(tile)
        #print(3333, grid.ids)

    def on_favorite_toggled(self, instance, character_id, is_favorite):
        """Maneja el evento de favorito"""
        character = next(c for c in self.controller.get_characters(self.current_page) 
                   if c['id'] == character_id)
        self.controller.toggle_favorite(character)

n = 00000000000000000000000000000000000000000000000000000000000000000000000000000000000000



***************************************************************************************** self self
n = 00000000000000000000000000000000000000000000000000000000000000000000000000000000000000 
***************************************************************************************** self self

# harry_potter_app/views/characters/characters_list_screen.py
from kivy.uix.screenmanager import Screen
from kivy.properties import ListProperty, ObjectProperty # Añadir ObjectProperty para controller
from kivy.clock import Clock
from kivy.metrics import dp
# from kivy.uix.behaviors import ButtonBehavior # No necesario si no usas CharacterTile heredando de él
# from kivy.uix.boxlayout import BoxLayout # No necesario si no usas CharacterTile heredando de él

# Importa tu nuevo componente CharacterTile1
from components.character_tile1 import CharacterTile1 
# from utils.api_client import RickMortyAPI # Asumo que RickMortyAPI está en el controlador

# Elimina las definiciones de CharacterTile y CharacterTile1 de este archivo,
# ya que ahora están en sus propios módulos.
# Si aún necesitas CharacterTile (el ButtonBehavior, BoxLayout), asegúrate de importarlo también.


class CharactersListScreen(Screen):
    characters = ListProperty([])
    current_page = 1
    # Asegúrate de que el controlador se pase a la vista
    controller = ObjectProperty(None) # Define como ObjectProperty

    def __init__(self, **kwargs):
        # Es mejor pasar el controlador en el método 'on_enter' desde el MainController
        # o inyectarlo aquí si el diseño de tu app lo permite.
        # Por ahora, asumo que se pasa como 'controller' en kwargs
        self.controller = kwargs.pop('controller', None) # Asegúrate de que se pase
        super().__init__(**kwargs)
        # Es mejor cargar los personajes cuando la pantalla se vuelve visible (on_enter)
        # o cuando el controlador se asocia, no en __init__ directamente,
        # para asegurar que la UI esté completamente construida.
        # Clock.schedule_once(lambda dt: self.load_characters()) # Puedes quitar esto y usar on_enter

    def on_enter(self):
        """Se llama cuando la pantalla se vuelve visible."""
        if self.controller:
            self.controller.on_enter_characters_list_screen(self) # Le pasas la vista al controlador

    def display_characters(self, characters_data, favorite_ids):
        """
        Método público para que el controlador actualice la vista con los personajes.
        Se llama desde el controlador.
        :param characters_data: Lista de diccionarios de personajes a mostrar.
        :param favorite_ids: Conjunto de IDs de personajes favoritos para el usuario actual.
        """
        if 'characters_grid' not in self.ids:
            print("ERROR: characters_grid no está vinculado en la vista.")
            return

        grid = self.ids.characters_grid
        grid.clear_widgets() # Limpia widgets existentes

        for character in characters_data:
            # Aquí instanciamos tu nuevo componente CharacterTile1
            tile = CharacterTile1(
                character=character,  # Pasa el diccionario completo del personaje
                controller=self.controller, # Pasa la instancia del controlador
                size_hint=(None, None),
                size=(dp(200), dp(220)) # Ajusta el tamaño de cada tile según lo necesites
            )
            grid.add_widget(tile)

    # Puedes mantener o eliminar el método load_characters original si usas on_enter
    # y el display_characters manejado por el controlador.
    def load_characters(self):
        """
        Método para cargar personajes (si no usas la llamada desde el controlador en on_enter).
        Si usas el controlador, este método sería redundante o parte del controlador.
        """
        if not self.controller:
            print("ERROR: Controlador no está disponible para cargar personajes.")
            return
        
        characters_data = self.controller.get_characters(self.current_page) # Asume que el controlador tiene get_characters
        grid = self.ids.characters_grid
        grid.clear_widgets()
        
        for character in characters_data:
            tile = CharacterTile1( # Asegúrate de usar CharacterTile1 aquí
                character=character,
                controller=self.controller,
                size_hint=(None, None),
                size=(dp(200), dp(220))
            )
            grid.add_widget(tile)
















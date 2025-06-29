# app/views/characters/characters_list_screen.py
from kivymd.uix.screen import MDScreen
from kivy.properties import ListProperty, ObjectProperty, NumericProperty, StringProperty, BooleanProperty
from kivy.clock import Clock
from kivy.metrics import dp
from utils.api_client import RickMortyAPI

from components.character_tile import CharacterTile


class CharactersListScreen(MDScreen):
    characters = ListProperty([])
    current_page = 1
    # Asegúrate de que el controlador se pase a la vista
    controller = ObjectProperty(None) # Define como ObjectProperty

    def __init__(self, **kwargs):
        self.controller = kwargs.pop('controller', None) # Asegúrate de que se pase
        super().__init__(**kwargs)
        Clock.schedule_once(lambda dt: self.load_characters()) # Puedes quitar esto y usar on_enter

    def load_characters(self):
        if not self.controller:
            print("ERROR: Controlador no está disponible para cargar personajes.")
            return
        
        characters_data = self.controller.get_characters(self.current_page) # Asume que el controlador tiene get_characters
        print(f"Cargando {len(characters_data)} personajes.")
        grid = self.ids.characters_grid
        grid.clear_widgets()
        
        for character in characters_data:
            tile = CharacterTile( # Asegúrate de usar CharacterTile1 aquí
                character=character,
                controller=self.controller,
                size_hint=(None, None),
                size=(dp(200), dp(220))
            )
            grid.add_widget(tile)

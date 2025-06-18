from kivymd.uix.screen import MDScreen
from kivy.properties import NumericProperty, StringProperty
from kivy.lang import Builder

Builder.load_file('views/characters/character_detail.kv')

class CharacterDetailScreen(MDScreen):
    character_id = NumericProperty(0)
    character_name = StringProperty('')
    character_status = StringProperty('')
    character_species = StringProperty('')
    character_image = StringProperty('')

    def __init__(self, controller, **kwargs):
        self.controller = controller
        super().__init__(**kwargs)

    def on_enter(self):
        self.load_character_data()

    def load_character_data(self):
        character = self.controller.get_character(self.character_id)
        self.character_name = character['name']
        self.character_status = character['status']
        self.character_species = character['species']
        self.character_image = character['image']



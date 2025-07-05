from kivy.uix.screenmanager import Screen
from kivy.properties import ListProperty, ObjectProperty, StringProperty
from kivy.clock import Clock
from kivy.uix.image import AsyncImage
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.card import MDCard

class CharactersCard(MDCard):
    source = StringProperty()
    text = StringProperty()
    favorite = ObjectProperty()

class FavoritesListScreen(Screen):
    favorites = ListProperty([])
    grid = ObjectProperty(None)

    def __init__(self, **kwargs):
        self.controller = kwargs.pop('controller')
        super().__init__(**kwargs)
        Clock.schedule_once(lambda dt: self.load_favorites())

    def on_enter(self):
        self.load_favorites()

    def load_favorites(self):
        if self.controller.app.auth_controller.current_user:
            user_id = self.controller.app.auth_controller.current_user['id']
            self.favorites = self.controller.get_user_favorites(user_id)
            self.update_ui()

    def update_ui(self):
        if not self.ids.get('favorites_grid'):
            return
            
        grid = self.ids.favorites_grid
        grid.clear_widgets()
        
        for fav in self.favorites:
            # Imagen del personaje
            fav_card = CharactersCard(
            source=fav['character_image'],
            text=fav['character_name'],
            favorite=fav
            )
            fav_card.ids.delete_button.bind(on_press=lambda x, f=fav: self.remove_favorite(f))
            grid.add_widget(fav_card)

    def remove_favorite(self, favorite):  # V5b
        if self.controller.remove_favorite(favorite['character_id']):
            print("favorito borrado")
            characters_screen = self.manager.get_screen('characters_list')
            for tile in characters_screen.ids.characters_grid.children:
                if hasattr(tile, 'character_id') and tile.character_id == favorite['character_id']:
                    #definir como False en  el tile de la pantalla personajes
                    tile.is_favorite = False
                    break

        # character_detail_screen = self.manager.get_screen('character_detail')  # V5
        # if character_detail_screen.character and character_detail_screen.character['id'] == favorite['character_id']:
        #     character_detail_screen.is_favorite = False

            self.load_favorites()  # Recargar la lista

    def remove_favorite0(self, favorite, character_tile):
        if self.controller.remove_favorite(favorite['character_id']):
            print("favorito borrado")
            character_tile.is_favorite = False
            self.load_favorites()  # Recargar la lista

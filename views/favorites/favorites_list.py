from kivy.uix.screenmanager import Screen
from kivy.properties import ListProperty, ObjectProperty
from kivy.clock import Clock
from kivy.uix.image import AsyncImage
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

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
            img = AsyncImage(
                source=fav['character_image'],
                size_hint=(None, None),
                size=(200, 200),
                keep_ratio=True,
                allow_stretch=True
            )
            
            # Nombre del personaje
            name = Label(
                text=fav['character_name'],
                size_hint_y=None,
                height=30
            )
            
            # Botón para eliminar
            btn = Button(
                text='❌',
                size_hint=(None, None),
                size=(50, 50),
                on_press=lambda x, f=fav: self.remove_favorite(f)
            )
            
            grid.add_widget(img)
            grid.add_widget(name)
            grid.add_widget(Label())  # Espaciador
            grid.add_widget(btn)

    def remove_favorite0(self, favorite):
        if self.controller.remove_favorite(favorite['character_id']):
            self.load_favorites()  # Recargar la lista

    def remove_favorite(self, favorite):
        if self.controller.remove_favorite(favorite['character_id']):
            characters_screen = self.manager.get_screen('characters_list')
            for tile in characters_screen.ids.characters_grid.children:
                if hasattr(tile, 'character_id') and tile.character_id == favorite['character_id']:
                    tile.is_favorite = False
                    break
            self.load_favorites()  # Recargar la lista

    def on_favorite_toggled0(self, instance, character_id, is_favorite):
        """Cuando se quita un favorito, actualizar los tiles correspondientes"""
        if not is_favorite:
            if self.controller.remove_favorite(character_id):
                # Buscar y actualizar el tile en la pantalla de personajes
                characters_screen = self.manager.get_screen('characters_list')
                for tile in characters_screen.ids.characters_grid.children:
                    if hasattr(tile, 'character_id') and tile.character_id == character_id:
                        tile.update_favorite_icon()
                        break

    def on_favorite_toggled(self, instance, character_id, is_favorite):
        """Cuando se quita un favorito, actualizar los tiles correspondientes"""
        if not is_favorite:
            if self.controller.remove_favorite(character_id):
                # Buscar y actualizar el tile en la pantalla de personajes
                print("favotito borrado")
                characters_screen = self.manager.get_screen('characters_list')
                for tile in characters_screen.ids.characters_grid.children:
                    if hasattr(tile, 'character_id') and tile.character_id == character_id:
                        print("222")
                        #tile.update_favorite_icon()
                        tile.is_favorite = False  # Actualizar la propiedad is_favorite
                    # No es necesario llamar a update_favorite_icon() explícitamente
                    # ya que la propiedad is_favorite está enlazada a la función update_favorite_icon
                        break


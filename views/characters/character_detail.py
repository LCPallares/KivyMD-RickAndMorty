from kivymd.uix.screen import MDScreen
from kivy.properties import NumericProperty, StringProperty, BooleanProperty, ObjectProperty
from kivy.lang import Builder

Builder.load_file('views/characters/character_detail.kv')


class CharacterDetailScreen(MDScreen):
    character_id = NumericProperty(0)
    character_name = StringProperty('')
    character_status = StringProperty('')
    character_species = StringProperty('')
    character_image = StringProperty('')
    
    character_gender = StringProperty('')
    character_origin = StringProperty('')
    character_location = StringProperty('')
    character_created = StringProperty('')

    is_favorite = BooleanProperty(False)
    controller = ObjectProperty(None)
    character = ObjectProperty(None)

    def __init__(self, controller, **kwargs):
        self.controller = controller
        #self.controller = kwargs.pop('controller', None)
        super().__init__(**kwargs)
        #self.character = character
        #self.controller = controller
        
        #self.controller = self.app.sm.controller
        #self.is_favorite = self.controller.is_favorite(self.character_id) if self.controller else False
        #self.bind(is_favorite=self.update_favorite_icon)

    def on_enter(self):
        self.load_character_data()
        # la version 5b necesita character_id, is_favorite, averiguar porque
        self.character_id = self.character["id"] # 5b
        self.is_favorite = self.controller.is_favorite(self.character_id) if self.controller else False # 5b

    def load_character_data(self):
        # no usar get_character para cargar la info del personaje, ya se obtiene al cargar personajes
        #character = self.controller.get_character(self.character_id)
        character = self.character
        self.character_name = character['name']
        self.character_status = character['status']
        self.character_species = character['species']
        self.character_image = character['image']
        self.character_gender = character['gender']
        self.character_origin = character['origin']['name']
        self.character_location = character['location']['name']
        self.character_created = character['created']

    def toggle_favorite5(self, *args):
        """ Alterna el estado de favorito del personaje a través del controlador. """
        success = self.controller.toggle_favorite(self.character)        
        if success:
            self.is_favorite = not self.is_favorite
            self.tile.is_favorite = self.is_favorite  # Actualiza la propiedad is_favorite de CharacterTile
            print(f"Estado de favorito para {self.character_name} cambiado a: {self.is_favorite}")
        else:
            print(f"Fallo al alternar favorito para {self.character_name}.")

    def toggle_favorite5b0(self, *args):
        """ Alterna el estado de favorito del personaje a través del controlador. """
        self.is_favorite = self.controller.toggle_favorite(self.character)
        print(f"Estado de favorito para {self.character_name} cambiado a: {self.is_favorite}")
        characters_screen = self.manager.get_screen('characters_list')
        if self.is_favorite:
            characters_screen.is_favorite = False
        else: 
            characters_screen.is_favorite = False

    def toggle_favorite5b1(self, *args): # funciona pero no es optimo por el for
        """ Alterna el estado de favorito del personaje a través del controlador. """
        self.is_favorite = self.controller.toggle_favorite(self.character)
        print(f"Estado de favorito para {self.character_name} cambiado a: {self.is_favorite}")
        characters_screen = self.manager.get_screen('characters_list')
        for tile in characters_screen.ids.characters_grid.children:
            if hasattr(tile, 'character_id') and tile.character_id == self.character_id:
                tile.is_favorite = self.is_favorite
                break

    def toggle_favorite(self, *args):
        """ Alterna el estado de favorito del personaje a través del controlador. """
        self.is_favorite = self.controller.toggle_favorite(self.character)
        print(f"Estado de favorito para {self.character_name} cambiado a: {self.is_favorite}")
        self.character_tile.is_favorite = self.is_favorite  # Actualizar directamente el CharacterTile
        #self.tile.is_favorite = self.is_favorite  # Actualiza la propiedad is_favorite de CharacterTile

    def update_favorite_icon(self, instance, value):
        """Actualiza el estado del ícono basado en la base de datos"""
        if self.controller:
            self.is_favorite = self.controller.is_favorite(self.character_id)
        else:
            self.is_favorite = False



    '''
    def update_favorite_icon1(self):
        self.ids.favorite_btn.icon = "heart" if self.is_favorite else "heart-outline"
        self.ids.favorite_btn.icon_color = (1, 0, 0, 1) if self.is_favorite else (1, 1, 1, 1)

    @property
    def is_favorite1(self):
        if self.controller and self.character:
            return self.controller.is_favorite(self.character['id'])
        return False

    def on_is_favorite(self, instance, value):
        self.ids.favorite_btn.icon = "heart" if value else "heart-outline"
        self.ids.favorite_btn.icon_color = (1, 0, 0, 1) if value else (1, 1, 1, 1)

    def update_favorite_icon2(self, instance, value):
        if self.controller and self.character:
            self.is_favorite = self.controller.is_favorite(self.character['id'])
    '''


    '''
    # En CharacterTile
    def on_press(self):
        self.controller.app.sm.current = 'character_detail'
        character_detail_screen = self.controller.app.sm.get_screen('character_detail')
        character_detail_screen.character = self.character
        character_detail_screen.controller = self.controller
        character_detail_screen.character_tile = self  # Agregar esta línea

    # En CharacterDetailScreen
    def toggle_favorite(self, *args):
        """ Alterna el estado de favorito del personaje a través del controlador. """
        self.is_favorite = self.controller.toggle_favorite(self.character)
        print(f"Estado de favorito para {self.character_name} cambiado a: {self.is_favorite}")
        self.character_tile.is_favorite = self.is_favorite  # Actualizar directamente el CharacterTile
    '''


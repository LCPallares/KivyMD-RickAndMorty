from kivy.uix.screenmanager import Screen
from kivy.properties import ListProperty, ObjectProperty
from kivy.clock import Clock
from kivy.uix.image import AsyncImage
from kivy.uix.behaviors import ButtonBehavior

class CharacterImageButton(ButtonBehavior, AsyncImage):
    pass

class CharactersListScreen(Screen):
    characters = ListProperty([])
    current_page = 1

    def __init__(self, **kwargs):
        self.controller = kwargs.pop('controller')
        super().__init__(**kwargs)
        Clock.schedule_once(lambda dt: self.load_characters())

    def load_characters(self):
        self.characters = self.controller.get_characters(self.current_page)

    def toggle_favorite(self, character):
        if self.controller.toggle_favorite(character):
            self.load_characters()  # Recargar para actualizar corazones

'''
<CharacterImageButton>:
    size_hint: None, None
    size: 200, 200
    keep_ratio: True
    allow_stretch: True

<CharactersListScreen>:
    ScrollView:
        GridLayout:
            cols: 2
            size_hint_y: None
            height: self.minimum_height
            spacing: 10
            padding: 10

            AsyncImage:
                source: 'https://rickandmortyapi.com/api/character/avatar/1.jpeg'
                size_hint: None, None
                size: 200, 200
                keep_ratio: True
                allow_stretch: True

            Label:
                text: 'Rick Sanchez'
                size_hint_y: None
                height: 30

            Button:
                text: '❤️' if False else '🤍'
                size_hint: None, None
                size: 50, 50
                on_press: app.root.get_screen('characters_list').toggle_favorite({'id': 1, 'name': 'Rick Sanchez', 'image': 'https://rickandmortyapi.com/api/character/avatar/1.jpeg'})
'''

from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout

class CharacterTile(ButtonBehavior, BoxLayout):
    """Tile personalizado para cada personaje"""
    def __init__(self, character, controller, **kwargs):
        super().__init__(**kwargs)
        self.character = character
        self.controller = controller
        self.ids.character_image.source = character['image']
        self.ids.character_image_text.text = character['name']
        self.update_favorite_icon()

    def update_favorite_icon(self):
        """Actualiza el ícono del corazón según el estado"""
        is_fav = self.controller.is_favorite(self.character['id'])
        self.ids.favorite_icon.text = '❤️' if is_fav else '🤍'

    def toggle_favorite(self):
        """Alterna entre favorito/no favorito"""
        success = self.controller.toggle_favorite(self.character)
        if success:
            self.update_favorite_icon()

    def on_press(self):
        """Maneja el clic en el tile"""
        self.toggle_favorite()
        print(11111)

'''
<CharacterTile>:
    orientation: 'vertical'
    size_hint: None, None
    size: dp(200), dp(220)
    spacing: dp(5)
    padding: dp(5)
    canvas.before:
        # ... (mantén tu diseño actual)

    AsyncImage:
        id: character_image
        source: ''
        size_hint: None, None
        size: dp(180), dp(180)
        keep_ratio: True
        allow_stretch: True
        pos_hint: {'center_x': 0.5}

    BoxLayout:
        size_hint_y: None
        height: dp(30)
        spacing: dp(5)

        Label:
            id: character_text
            text: ''
            halign: 'center'
            text_size: self.width, None

        Label:
            id: favorite_icon
            text: '🤍'
            size_hint_x: None
            width: dp(30)
            font_size: dp(20)
'''

from kivy.event import EventDispatcher
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.animation import Animation
from kivy.properties import (
    StringProperty, 
    NumericProperty,
    BooleanProperty
)
from kivy.uix.button import Button

class CharacterTile(ButtonBehavior, BoxLayout):
    """Componente reusable para mostrar personajes"""
    character_id = NumericProperty(0)
    character_name = StringProperty('')
    character_image = StringProperty('')
    is_favorite = BooleanProperty(False)
    tile_size = NumericProperty(200)
    
    # Definimos el evento correctamente
    __events__ = ('on_favorite_toggled',)

    def on_press(self):
        """Maneja el clic en el tile"""
        self.toggle_favorite()
        #self.animate_heart()

    def toggle_favorite(self):
        """Alterna el estado de favorito"""
        self.is_favorite = not self.is_favorite
        # Disparamos el evento con los parámetros necesarios
        self.dispatch('on_favorite_toggled', self.character_id, self.is_favorite)
    
    def animate_heart0(self):
        """Pequeña animación al hacer clic"""
        anim = Animation(scale=1.2, duration=0.1) + Animation(scale=1.0, duration=0.1)
        anim.start(self.ids.favorite_icon)

    def animate_heart(self):
        """Animación mejorada compatible con Label"""
        heart = self.ids.favorite_icon
        
        # Verificamos si el widget soporta scale
        if hasattr(heart, 'scale'):
            anim = Animation(scale=1.2, duration=0.1) + Animation(scale=1.0, duration=0.1)
            anim.start(heart)
        else:
            # Alternativa para widgets sin scale
            original_size = heart.font_size
            anim = Animation(font_size=original_size*1.4, duration=0.1) + Animation(font_size=original_size, duration=0.1)
            anim.start(heart)
    
    def on_favorite_toggled(self, character_id, is_favorite):
        """Manejador por defecto (puede ser sobrescrito)"""
        pass
    


'''
<CharacterTile>:
    size_hint: None, None
    size: "180dp", "220dp"
    radius: "12dp"
    elevation: 2
    padding: "8dp"
    spacing: "8dp"
    orientation: "vertical"
    
    # Imagen del personaje
    FitImage:
        id: character_image
        source: root.character_image
        size_hint_y: 0.7
        radius: root.radius
        nocache: True  # Evita problemas con imágenes iguales
    
    # Información del personaje
    BoxLayout:
        size_hint_y: 0.3
        spacing: "8dp"
        padding: "4dp"
        
        MDLabel:
            text: root.character_name
            font_style: "Subtitle1"
            theme_text_color: "Primary"
            size_hint_x: 0.8
            halign: "left"
            valign: "center"
            shorten: True
            shorten_from: "right"
        
        MDIconButton:
            id: favorite_btn
            icon: "heart" if root.is_favorite else "heart-outline"
            theme_icon_color: "Custom"
            icon_color: (1, 0, 0, 1) if root.is_favorite else (0.5, 0.5, 0.5, 1)
            size_hint_x: 0.2
            on_release: root.toggle_favorite()
'''

from kivy.properties import ListProperty
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from utils.api_client import RickMortyAPI

class CharacterTile(ButtonBehavior, BoxLayout):
    """Tile personalizado para cada personaje"""
    def __init__(self, character, controller, **kwargs):
        super().__init__(**kwargs)
        self.character = character
        self.controller = controller
        self.ids.character_image.source = character['image']
        self.ids.character_image_text.text = character['name']
        self.update_favorite_icon()

    def update_favorite_icon(self):
        """Actualiza el ícono del corazón según el estado"""
        is_fav = self.controller.is_favorite(self.character['id'])
        self.ids.favorite_icon.text = '❤️' if is_fav else '🤍'

    def toggle_favorite(self):
        """Alterna entre favorito/no favorito"""
        success = self.controller.toggle_favorite(self.character)
        if success:
            self.update_favorite_icon()

    def on_press(self):
        """Maneja el clic en el tile"""
        self.toggle_favorite()

class CharactersListScreen(Screen):
    characters = ListProperty([])
    current_page = 1

    def __init__(self, **kwargs):
        self.controller = kwargs.pop('controller')
        super().__init__(**kwargs)
        Clock.schedule_once(lambda dt: self.load_characters())

    def load_characters(self):
        """Carga los personajes desde la API y crea los tiles"""
        characters_data = self.controller.get_characters(self.current_page)
        grid = self.ids.characters_grid
        grid.clear_widgets()
        
        for character in characters_data:
            tile = CharacterTile(
                character=character,
                controller=self.controller,
                size_hint=(None, None),
                size=(dp(200), dp(220))
            )
            grid.add_widget(tile)

'''
<CharactersListScreen>:
    BoxLayout:
        orientation: 'vertical'
        spacing: 5

        # Barra de navegación - AHORA EN PRIMER PLANO
        BoxLayout:
            size_hint_y: None
            height: 50
            spacing: 10
            padding: 5
            canvas.before:
                Color:
                    rgba: 0.2, 0.2, 0.2, 1
                Rectangle:
                    pos: self.pos
                    size: self.size

            Button:
                text: 'Personajes'
                background_normal: ''
                background_color: 0.3, 0.3, 0.5, 1
                on_press: root.manager.current = 'characters_list'

            Button:
                text: 'Favoritos'
                background_normal: ''
                background_color: 0.3, 0.5, 0.3, 1
                on_press: root.manager.current = 'favorites_list'

            Button:
                text: 'Cerrar Sesión'
                background_normal: ''
                background_color: 0.8, 0.3, 0.3, 1
                on_press: 
                    app.auth_controller.logout()
                    root.manager.current = 'login'

        # Área de contenido con prioridad de espacio
        ScrollView:
            GridLayout:
                cols: 2
                size_hint_y: None
                height: self.minimum_height
                spacing: 10
                padding: 10

                AsyncImage:
                    source: 'https://rickandmortyapi.com/api/character/avatar/1.jpeg'
                    size_hint: None, None
                    size: 200, 200
                    keep_ratio: True
                    allow_stretch: True

                Label:
                    text: 'Rick Sanchez'
                    size_hint_y: None
                    height: 30

                Button:
                    text: '❤️' if False else '🤍'
                    size_hint: None, None
                    size: 50, 50
                    on_press: app.root.get_screen('characters_list').toggle_favorite({'id': 1, 'name': 'Rick Sanchez', 'image': 'https://rickandmortyapi.com/api/character/avatar/1.jpeg'})
'''

from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.animation import Animation
from kivy.properties import (
    StringProperty, 
    NumericProperty,
    BooleanProperty
)

class CharacterTile(ButtonBehavior, BoxLayout):
    """Componente reusable para mostrar personajes"""
    character_id = NumericProperty(0)
    character_name = StringProperty('')
    character_image = StringProperty('')
    is_favorite = BooleanProperty(False)
    tile_size = NumericProperty(200)
    
    def on_press(self):
        """Maneja el clic en el tile"""
        self.toggle_favorite()
        self.animate_heart()

    def toggle_favorite(self):
        """Alterna el estado de favorito"""
        self.is_favorite = not self.is_favorite
        # Disparamos el evento que será manejado por la pantalla padre
        self.dispatch('on_favorite_toggled', self.character_id, self.is_favorite)

    def animate_heart(self):
        """Pequeña animación al hacer clic"""
        anim = Animation(scale=1.2, duration=0.1) + Animation(scale=1.0, duration=0.1)
        anim.start(self.ids.favorite_icon)

    def on_favorite_toggled(self, *args):
        """Evento que se dispara al cambiar favorito"""
        pass

# Registramos el evento
CharacterTile.register_event_type('on_favorite_toggled')

'''
<CharacterTile>:
    orientation: 'vertical'
    size_hint: None, None
    #size: root.tile_size, root.tile_size * 1.1
    spacing: dp(5)
    padding: dp(5)
    canvas.before:
        Color:
            rgba: (0.15, 0.15, 0.2, 1) if self.state == 'normal' else (0.25, 0.25, 0.3, 1)
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [dp(15),]

    AsyncImage:
        source: "https://rickandmortyapi.com/api/character/avatar/1.jpeg" #root.character_image
        size_hint: None, None
        size: root.tile_size * 0.9, root.tile_size * 0.9
        keep_ratio: True
        allow_stretch: True
        pos_hint: {'center_x': 0.5}

    BoxLayout:
        size_hint_y: None
        height: dp(30)
        spacing: dp(5)

        Label:
            text: "root.character_name"
            halign: 'center'
            text_size: self.width, None
            size_hint_x: 0.8
            ellipsis_options: {'color': [1, 1, 1, 1], 'padding': [dp(5), dp(5)]}
            shorten: True
            shorten_from: 'right'

        Label:
            id: favorite_icon
            #text: '❤️' if root.is_favorite else '🤍'
            text: "texto"
            size_hint_x: None
            width: dp(30)
            font_size: dp(20)  # Esto es esencial para la animación
'''




# harry_potter_app/views/characters/characters_list_screen.py
from kivy.uix.screenmanager import Screen
from kivy.properties import ListProperty
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from utils.api_client import RickMortyAPI
from components.character_tile2 import CharacterTile2
from components.character_tile1b import CharacterTile1b
from kivymd.uix.imagelist import MDSmartTile


class CharacterTile(ButtonBehavior, BoxLayout):
    """Tile personalizado para cada personaje"""
    def __init__(self, character, controller, **kwargs):
        super().__init__(**kwargs)
        self.character = character
        self.controller = controller
        self.ids.character_image.source = character['image']
        self.ids.character_image_text.text = character['name']
        self.update_favorite_icon()

    def update_favorite_icon(self):
        """Actualiza el ícono del corazón según el estado"""
        is_fav = self.controller.is_favorite(self.character['id'])
        self.ids.favorite_icon.text = '❤️' if is_fav else '🤍'

    def toggle_favorite(self):
        """Alterna entre favorito/no favorito"""
        success = self.controller.toggle_favorite(self.character)
        if success:
            self.update_favorite_icon()

    def on_long_press(self):
        """Maneja el clic en el tile"""
        self.toggle_favorite()
        print(11111)


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


class CharactersListScreen(Screen):
    characters = ListProperty([])
    current_page = 1

    def __init__(self, **kwargs):
        self.controller = kwargs.pop('controller')
        super().__init__(**kwargs)
        Clock.schedule_once(lambda dt: self.load_characters())

    def load_characters(self):
        """Carga los personajes desde la API y crea los tiles"""
        characters_data = self.controller.get_characters(self.current_page)
        grid = self.ids.characters_grid
        grid.clear_widgets()
        
        for character in characters_data:
            tile = CharacterTile1b(
                character=character,
                controller=self.controller,
                size_hint=(None, None),
                size=(dp(200), dp(220))
            )
            grid.add_widget(tile)


































































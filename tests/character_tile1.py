from kivymd.uix.imagelist import MDSmartTile
from kivy.properties import NumericProperty, BooleanProperty
from kivy.animation import Animation

class CharacterTile(MDSmartTile):
    character_id = NumericProperty(0)
    is_favorite = BooleanProperty(False)
    
    __events__ = ('on_favorite_toggled',)

    def toggle_favorite(self, *args):
        self.is_favorite = not self.is_favorite
        self.ids.favorite_button.icon = "heart" if self.is_favorite else "heart-outline"
        self.animate_heart()
        self.dispatch('on_favorite_toggled', self.character_id, self.is_favorite)

    def animate_heart(self):
        anim = Animation(scale=1.2, duration=0.1) + Animation(scale=1.0, duration=0.1)
        anim.start(self.ids.favorite_button)

    def on_favorite_toggled(self, *args):
        pass

'''
<CharacterTile>:
    # Configuración básica del tile
    radius: 24
    box_radius: [0, 0, 24, 24]
    box_color: [1, 1, 1, .2]
    size_hint: None, None
    size: "200dp", "200dp"
    
    # Botón de favoritos (ya integrado en MDSmartTile)
    MDIconButton:
        id: favorite_button
        icon: "heart-outline"
        theme_icon_color: "Custom"
        icon_color: 1, 1, 1, 1
        pos_hint: {"center_x": .85, "center_y": .85}
    
    # Etiqueta del nombre (ya integrada)
    MDLabel:
        id: name_label
        #text: root.text if hasattr(root, 'text') else ''
        text: "aaaaa"
        bold: True
        color: 1, 1, 1, 1
        halign: "center"
        valign: "bottom"
        size_hint_y: None
        height: "40dp"
'''

from kivymd.uix.imagelist import MDSmartTile
from kivymd.uix.button import MDIconButton
from kivy.properties import (
    NumericProperty,
    StringProperty,
    BooleanProperty,
    ColorProperty
)
from kivy.animation import Animation

class CharacterTile(MDSmartTile):
    """Tile optimizado usando todas las capacidades de MDSmartTile"""
    character_id = NumericProperty(0)
    character_name = StringProperty('')
    character_image = StringProperty('')
    is_favorite = BooleanProperty(False)
    tile_size = NumericProperty("200dp")
    overlay_color = ColorProperty([0, 0, 0, 0.5])
    
    __events__ = ('on_favorite_toggled',)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.radius = 24
        self.box_radius = [0, 0, 24, 24]
        self.box_color = [1, 1, 1, .2]
        self.size_hint = (None, None)
        self.size = (self.tile_size, self.tile_size)
        self.bind(
            character_image=self.update_image,
            character_name=self.update_text,
            is_favorite=self.update_favorite_icon
        )
        
        # Configuración inicial
        self.setup_favorite_button()

    def setup_favorite_button(self):
        """Configura el botón de favoritos"""
        self.favorite_btn = MDIconButton(
            icon="heart-outline",
            theme_icon_color="Custom",
            icon_color=[1, 0, 0, 0.7],
            pos_hint={"center_x": 0.85, "center_y": 0.85},
            on_release=self.toggle_favorite
        )
        self.add_widget(self.favorite_btn)

    def toggle_favorite(self, *args):
        """Alterna el estado de favorito"""
        self.is_favorite = not self.is_favorite
        self.dispatch('on_favorite_toggled', self.character_id, self.is_favorite)
        #self.animate_heart()

    def update_image(self, instance, value):
        """Actualiza la imagen del tile"""
        self.source = value

    def update_text(self, instance, value):
        """Actualiza el texto del tile"""
        if not hasattr(self, 'text_label'):
            self.text_label = MDLabel(
                text=value,
                bold=True,
                color=[1, 1, 1, 1],
                size_hint_y=None,
                height=dp(40),
                halign="center"
            )
            self.add_widget(self.text_label)
        else:
            self.text_label.text = value

    def update_favorite_icon(self, instance, value):
        """Actualiza el ícono de favorito"""
        self.favorite_btn.icon = "heart" if value else "heart-outline"
        self.favorite_btn.icon_color = [1, 0, 0, 1] if value else [1, 1, 1, 0.9]

    def animate_heart0(self):
        """Animación del corazón"""
        anim = Animation(scale=1.2, duration=0.1) + Animation(scale=1.0, duration=0.1)
        anim.start(self.favorite_btn)

    def on_favorite_toggled(self, *args):
        """Evento por defecto"""
        pass


'''
<CharacterTile>:
    id: character_image
    radius: 24
    box_radius: [0, 0, 24, 24]
    box_color: 1, 1, 1, .2
    pos_hint: {"center_x": .5, "center_y": .5}
    size_hint: None, None
    size: "320dp", "320dp"

    MDIconButton:
        icon: "heart-outline"
        theme_icon_color: "Custom"
        icon_color: 1, 0, 0, 1
        pos_hint: {"center_y": .5}
        on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"

    MDLabel:
        id: character_name
        bold: True
        color: 1, 1, 1, 1
'''







from kivymd.uix.imagelist import MDSmartTile
from kivy.properties import NumericProperty, BooleanProperty
from kivy.animation import Animation

class CharacterTile(MDSmartTile):
    """Versión simplificada usando MDSmartTile nativo"""
    character_id = NumericProperty(0)
    is_favorite = BooleanProperty(False)
    
    __events__ = ('on_favorite_toggled',)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.radius = 24
        self.box_radius = [0, 0, 24, 24]
        self.box_color = [1, 1, 1, .2]
        self.size_hint = (None, None)
        self.size = ("200dp", "200dp")
        
        # Configuración del botón de favoritos
        self.favorite_btn = self.ids.favorite_button
        self.favorite_btn.bind(on_release=self.toggle_favorite)
        self.update_favorite_icon()

    def toggle_favorite(self, *args):
        """Alterna el estado de favorito con animación"""
        self.is_favorite = not self.is_favorite
        self.update_favorite_icon()
        self.animate_heart()
        self.dispatch('on_favorite_toggled', self.character_id, self.is_favorite)

    def update_favorite_icon(self):
        """Actualiza el ícono basado en el estado"""
        self.favorite_btn.icon = "heart" if self.is_favorite else "heart-outline"
        self.favorite_btn.icon_color = [1, 0, 0, 1] if self.is_favorite else [1, 1, 1, 1]

    def animate_heart(self):
        """Animación simple del corazón"""
        anim = Animation(scale=1.2, duration=0.1) + Animation(scale=1.0, duration=0.1)
        anim.start(self.favorite_btn)

    def on_favorite_toggled(self, *args):
        """Evento que se dispara al cambiar favorito"""
        pass




































# harry_potter_app/components/character_tile1.py
from kivymd.uix.imagelist import MDSmartTile
from kivy.properties import ObjectProperty

class CharacterTile1b(MDSmartTile):
    character = ObjectProperty(None)
    controller = ObjectProperty(None)

    def __init__(self, character, controller, **kwargs):
        super().__init__(**kwargs)
        self.character = character
        self.controller = controller
        print(f"CharacterTile1 __init__: Character data received: {self.character}")
        
        self.source = character['image']

    def on_kv_post(self, base_widget):
        super().on_kv_post(base_widget) # Llama al método base de MDSmartTile
        #self.source = self.character['image'] 
        #self.ids.character_image_text.text = self.character['name']
        self.update_favorite_icon()

    def update_favorite_icon(self):
        """Actualiza el ícono del corazón según el estado de favorito."""
        is_fav = self.controller.is_favorite(self.character['id'])
        
        # Es buena práctica verificar si el ID existe antes de acceder
        if 'favorite_icon' in self.ids:
            self.ids.favorite_icon.icon = "heart" if is_fav else "heart-outline"
            self.ids.favorite_icon.icon_color = (1, 0, 0, 1) if is_fav else (1, 1, 1, 1)
        else:
            print("Advertencia: El ID 'favorite_icon' no se encontró en el KV de CharacterTile1.")


    def toggle_favorite(self):
        """Alterna entre favorito/no favorito a través del controlador."""
        success = self.controller.toggle_favorite(self.character)
        if success:
            self.update_favorite_icon()

    def on_press(self):
        self.toggle_favorite()
        print(f"Toque corto en el tile de {self.character['name']} - Alternando favorito.")


'''
# harry_potter_app/components/character_tile1.kv
# Esto define la estructura y apariencia para la clase CharacterTile1
<CharacterTile1b>:
    # Estas propiedades se pueden pasar desde Python o definir aquí como valores predeterminados
    # id: character_image # Este id en el root puede ser redundante si ya usas self.source
    radius: 24
    box_radius: [0, 0, 24, 24]
    box_color: 1, 1, 1, .2 # Color de la caja de fondo (para el MDSmartTile)
    # source: "D:/Programacion/Python/GUI/Kivy/codigos/rickmorty/assets/img4.png" # Se setea en Python __init__
    pos_hint: {"center_x": .5, "center_y": .5} # Puedes omitir esto si el tile se agrega a un GridLayout
    size_hint: None, None
    size: "320dp", "320dp" # El tamaño puede ser ajustado por el layout padre

    # Contenedor para el icono de favorito
    MDIconButton:
        id: favorite_icon # ID necesario para acceder desde Python
        icon: "heart-outline" # Se actualizará desde Python
        theme_icon_color: "Custom"
        icon_color: 1, 0, 0, 1 # Se actualizará desde Python
        pos_hint: {"x": 0.75, "y": 0.75} # Posición en la esquina superior derecha del tile
        # on_release: root.toggle_favorite() # Puedes volver a habilitar si quieres que el botón también haga la acción.
                                            # Actualmente, on_press del tile lo hace.

    # Contenedor para el texto del nombre del personaje
    MDLabel:
        id: character_image_text # ID necesario para acceder desde Python
        text: "Nombre del Personaje" # Se actualizará desde Python
        bold: True
        color: 1, 1, 1, 1
        halign: 'center' # Centrar el texto
        pos_hint: {'center_x': 0.5, 'y': 0} # Posicionar en la parte inferior del tile
'''

from kivymd.uix.imagelist import MDSmartTile
from kivy.properties import NumericProperty, BooleanProperty, StringProperty

class CharacterTile2(MDSmartTile):
    """Versión ultra-minimalista con manejo seguro de IDs"""
    character_id = NumericProperty(0)
    is_favorite = BooleanProperty(False)
    character_name = StringProperty('')
    #self.ids.name_label.text = character_name.text
    
    __events__ = ('on_favorite_toggled',)

    def toggle_favorite(self, *args):
        """Maneja el cambio de estado de favorito"""
        self.is_favorite = not self.is_favorite
        self.dispatch('on_favorite_toggled', self.character_id, self.is_favorite)

    def on_character_name(self, instance, value):
        """Actualiza el nombre cuando cambia la propiedad"""
        if 'name_label' in self.ids:
            self.ids.name_label.text = value

    def on_favorite_toggled(self, *args):
        pass

'''
<CharacterTile2>:
    radius: 24
    box_radius: [0, 0, 24, 24]
    size_hint: None, None
    size: "200dp", "200dp"
    
    box_color: 1, 1, 1, .2
    pos_hint: {"center_x": .5, "center_y": .5}
    size_hint: None, None
    #size: "320dp", "320dp"

    # Botón de favoritos
    MDIconButton:
        id: favorite_button
        icon: "heart" if root.is_favorite else "heart-outline"
        theme_icon_color: "Custom"
        icon_color: (1, 0, 0, 1) if root.is_favorite else (1, 1, 1, 1)
        pos_hint: {"center_x": .85, "center_y": .85}
        on_release: root.toggle_favorite()
    
    # Label para el nombre
    MDLabel:
        id: name_label
        text: "root.character_name"
        bold: True
        color: 1, 1, 1, 1
        #halign: "center"
        #valign: "bottom"
        #size_hint_y: None
        #height: "40dp"
'''

from kivymd.uix.imagelist import MDSmartTile
from kivy.properties import NumericProperty, BooleanProperty, StringProperty

from kivy.lang import Builder
#Builder.load_file('character_tile2b.kv')
Builder.load_file('components/character_tile2b.kv')

class CharacterTile2b(MDSmartTile):
    """Versión ultra-minimalista con manejo seguro de IDs"""
    character_id = NumericProperty(0)
    is_favorite = BooleanProperty(False)
    character_name = StringProperty('')

    def __init__(self, character, controller, **kwargs):
        super().__init__(**kwargs)
        self.character = character
        self.controller = controller
        print(f"CharacterTile1 __init__: Character data received: {self.character}")
        
        # Inicializar las propiedades de Kivy con los datos validados
        self.character_id = character.get('id', 0) # Usar .get() para evitar KeyError si la clave no existe
        self.character_name = character.get('name', 'Nombre No Disponible')
        
        # Determinar el estado inicial de favorito usando el controlador
        self.is_favorite = self.controller.is_favorite(self.character_id) if self.controller else False

        # Establecer la fuente de la imagen del MDSmartTile.
        # Ahora es seguro, ya que 'character' ya ha sido validado.
        self.source = character.get('image', "assets/placeholder_error.png")

    
    def toggle_favorite(self, *args):
        """Maneja el cambio de estado de favorito"""
        self.is_favorite = not self.is_favorite
        self.dispatch('on_favorite_toggled', self.character_id, self.is_favorite)

    def on_character_name(self, instance, value):
        """Actualiza el nombre cuando cambia la propiedad"""
        if 'name_label' in self.ids:
            self.ids.name_label.text = value
    

'''
<CharacterTile2b2>:
    radius: 24
    box_radius: [0, 0, 24, 24]
    size_hint: None, None
    size: "200dp", "200dp"
    
    box_color: 1, 1, 1, .2
    pos_hint: {"center_x": .5, "center_y": .5}
    size_hint: None, None
    #size: "320dp", "320dp"

    # Botón de favoritos
    MDIconButton:
        icon: "heart" if root.is_favorite else "heart-outline"
        theme_icon_color: "Custom"
        icon_color: (1, 0, 0, 1) if root.is_favorite else (1, 1, 1, 1)
        pos_hint: {"center_x": .85, "center_y": .85}
        on_release: root.toggle_favorite()
    
    # Label para el nombre
    MDLabel:
        text: root.character_name
        bold: True
        color: 1, 1, 1, 1
        #halign: "center"
        #valign: "bottom"
        #size_hint_y: None
        #height: "40dp"

<CharacterTile2b>:
    radius: 24
    box_radius: [0, 0, 24, 24]
    box_color: 1, 1, 1, .2
    source: "https://rickandmortyapi.com/api/character/avatar/1.jpeg"
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
        text: "Julia and Julie"
        text: root.character_name
        bold: True
        color: 1, 1, 1, 1


<CharacterTile2b3>:
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
        text: root.character_name
        bold: True
        color: 1, 1, 1, 1
        halign: "center"
        valign: "bottom"
        size_hint_y: None
        height: "40dp"

'''













    
from kivymd.uix.imagelist import MDSmartTile
from kivy.properties import NumericProperty, BooleanProperty, StringProperty
class CharacterTile2b(MDSmartTile):
    """Versión ultra-minimalista con manejo seguro de IDs"""
    character_id = NumericProperty(0)
    is_favorite = BooleanProperty(False)
    character_name = StringProperty('')

    def __init__(self, character, controller, **kwargs):
        super().__init__(**kwargs)
        self.character = character
        self.controller = controller
        #print(f"CharacterTile1 __init__: Character data received: {self.character}")
        #self.character_data = None
        
        # Inicializar las propiedades de Kivy con los datos validados
        self.character_id = character.get('id', 0) # Usar .get() para evitar KeyError si la clave no existe
        self.character_name = character.get('name', 'Nombre No Disponible')
        
        # Determinar el estado inicial de favorito usando el controlador
        self.is_favorite = self.controller.is_favorite(self.character_id) if self.controller else False

        # Establecer la fuente de la imagen del MDSmartTile.
        # Ahora es seguro, ya que 'character' ya ha sido validado.
        self.source = character.get('image', "assets/placeholder_error.png")

    def toggle_favorite(self, *args):
        """
        Alterna el estado de favorito del personaje a través del controlador.
        """
        #if self.controller and self.character_data:
            # Llama al controlador para que maneje la lógica de negocio (añadir/quitar de DB)
        #success = self.controller.toggle_favorite(self.character_data)
        success = self.controller.toggle_favorite(self.character)        
        if success:
            # Si la operación en el controlador fue exitosa, actualiza la propiedad local.
            # Kivy detectará este cambio y actualizará el icono en el KV automáticamente.
            self.is_favorite = not self.is_favorite
            print(f"Estado de favorito para {self.character_name} cambiado a: {self.is_favorite}")
        else:
            print(f"Fallo al alternar favorito para {self.character_name}.")
        # else:
        #     print("Error: Controlador o datos de personaje no disponibles para alternar favorito.")

    def on_press(self):
        self.toggle_favorite()
        print(f"Presionado tile de {self.character['name']}")



'''
<CharacterTile2b>:
    radius: 24
    box_radius: [0, 0, 24, 24]
    box_color: 1, 1, 1, .2
    size_hint: None, None
    size: "320dp", "320dp"

    MDIconButton:
        icon: "heart" if root.is_favorite else "heart-outline"
        theme_icon_color: "Custom"
        icon_color: (1, 0, 0, 1) if root.is_favorite else (1, 1, 1, 1)
        pos_hint: {"center_y": .5}
        on_release: root.toggle_favorite()

    MDLabel:
        text: "Julia and Julie"
        text: root.character_name
        bold: True
        color: 1, 1, 1, 1
'''






































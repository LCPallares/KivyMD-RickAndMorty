
# harry_potter_app/components/character_tile1b.py
from kivymd.uix.imagelist import MDSmartTile
from kivy.properties import ObjectProperty # Necesario si quieres usar ObjectProperty para character y controller

class CharacterTile1b(MDSmartTile):
    """Tile personalizado para cada personaje, basado en MDSmartTile."""
    # Opcional: Define character y controller como ObjectProperty para mejor manejo de Kivy
    # Si los dejas como atributos directos (self.character = character), también funciona.
    character = ObjectProperty(None)
    controller = ObjectProperty(None)

    def __init__(self, character, controller, **kwargs):
        super().__init__(**kwargs)
        self.character = character
        self.controller = controller
        
        # MDSmartTile tiene una propiedad 'source' para la imagen principal
        self.source = character['image']
        
        # Acceder directamente a los IDs definidos en el archivo KV de este tile
        # Esto asume que el KV de CharacterTile1 tiene un MDLabel con id: character_image_text
        self.ids.character_image_text.text = character['name']
        
        self.update_favorite_icon()

    def update_favorite_icon(self):
        """Actualiza el ícono del corazón según el estado de favorito."""
        is_fav = self.controller.is_favorite(self.character['id'])
        # Asume que el KV de CharacterTile1 tiene un MDIconButton con id: favorite_icon
        self.ids.favorite_icon.icon = "heart" if is_fav else "heart-outline"
        # También puedes ajustar el color directamente aquí o en el KV
        self.ids.favorite_icon.icon_color = (1, 0, 0, 1) if is_fav else (1, 1, 1, 1)


    def toggle_favorite(self):
        """Alterna entre favorito/no favorito a través del controlador."""
        success = self.controller.toggle_favorite(self.character)
        if success:
            self.update_favorite_icon()

    def on_press(self):
        """
        Maneja el clic (press) en el tile.
        Actualmente, alterna el favorito. Si quieres que un toque corto
        navegue a los detalles y un toque largo alterne el favorito,
        debes implementar la lógica de long press como vimos en la respuesta anterior.
        """
        self.toggle_favorite()
        print(f"Toque corto en el tile de {self.character['name']} - Alternando favorito.")

'''
# harry_potter_app/components/character_tile2.kv
# Este archivo debe ser incluido en tu Builder.load_file en main.py
# y en las pantallas que lo utilicen con #:include.

<CharacterTile2>:
    # Configuración base del MDSmartTile
    radius: 24
    box_radius: [0, 0, 24, 24]
    box_color: 1, 1, 1, .2
    size_hint: None, None
    size: "200dp", "220dp" # Tamaño recomendado para un GridLayout de 3 columnas

    # El 'source' del MDSmartTile se setea en Python en on_kv_post

    # MDLabel para el nombre del personaje
    MDLabel:
        id: character_image_text # ID para acceso desde Python
        text: root.character_name # <-- Vinculado a la propiedad 'character_name'
        bold: True
        color: 1, 1, 1, 1
        halign: 'center'
        pos_hint: {'center_x': 0.5, 'y': 0} # Posición en la parte inferior

    # MDIconButton para el estado de favorito
    MDIconButton:
        id: favorite_icon # ID para acceso desde Python
        icon: "heart" if root.is_favorite else "heart-outline" # <-- Vinculado a la propiedad 'is_favorite'
        theme_icon_color: "Custom"
        icon_color: (1, 0, 0, 1) if root.is_favorite else (1, 1, 1, 1)
        pos_hint: {"x": 0.75, "y": 0.75} # Posición en la esquina superior derecha
        # on_release: root.toggle_favorite() # Puedes habilitarlo si el botón también debe ser interactivo,
                                            # pero el long press del tile ya hace esto.
'''

# harry_potter_app/components/character_tile1.py
from kivymd.uix.imagelist import MDSmartTile
from kivy.properties import ObjectProperty

class CharacterTile1(MDSmartTile):
    """Tile personalizado para cada personaje, basado en MDSmartTile."""
    character = ObjectProperty(None)
    controller = ObjectProperty(None)

    def __init__(self, character, controller, **kwargs):
        super().__init__(**kwargs)
        self.character = character
        self.controller = controller
        
        # self.source = character['image'] # Esto está bien aquí, ya que 'source' es una propiedad de MDSmartTile
                                          # y no depende de los IDs internos.
                                          # Sin embargo, moverlo a on_kv_post también es seguro y a veces preferible.

        # *** ¡IMPORTANTE! NO ACCEDER A self.ids AQUÍ EN EL __init__ ***
        # self.ids.character_image_text.text = character['name'] 
        # self.update_favorite_icon() 
        # Estas llamadas se moverán a on_kv_post para asegurar que los IDs estén cargados.

    def on_kv_post(self, base_widget):
        """
        Este método se llama automáticamente por Kivy después de que las reglas KV
        han sido aplicadas a esta instancia del widget y self.ids está poblado.
        Es el lugar seguro para inicializar widgets hijos por su ID.
        """
        super().on_kv_post(base_widget) # Llama al método base de MDSmartTile

        # Ahora es seguro acceder a los IDs
        # Si no lo setearte en __init__, puedes setear 'source' aquí también
        self.source = self.character['image'] 
        self.ids.character_image_text.text = self.character['name']
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
        """
        Maneja el clic (press) en el tile.
        Actualmente, alterna el favorito con un toque corto.
        """
        self.toggle_favorite()
        print(f"Toque corto en el tile de {self.character['name']} - Alternando favorito.")
























# harry_potter_app/components/character_tile2.py
import time # Necesario para la lógica de long press
from kivy.clock import Clock
from kivy.properties import NumericProperty, BooleanProperty, StringProperty, ObjectProperty
from kivymd.uix.imagelist import MDSmartTile

class CharacterTile2(MDSmartTile):
    """
    Componente de tile para personaje, robusto con propiedades Kivy y manejo de long/short press.
    """
    # Propiedades Kivy para manejar los datos del personaje de forma reactiva
    character_id = NumericProperty(0)
    is_favorite = BooleanProperty(False)
    character_name = StringProperty('')
    
    # Propiedad para almacenar el diccionario completo del personaje (ObjectProperty)
    character_data = ObjectProperty(None) 
    # Propiedad para el controlador (ObjectProperty)
    controller = ObjectProperty(None)

    # Propiedades para la lógica de 'long press'
    _last_touch_time = None
    _long_press_event = None
    _is_long_press_fired = False
    LONG_PRESS_TIME = 0.5 # Duración en segundos para considerar un 'long press'

    def __init__(self, character, controller, **kwargs):
        super().__init__(**kwargs)
        
        # --- Validación de datos de entrada ---
        # Si el 'character' es None o no es un diccionario, manejamos el error.
        if character is None or not isinstance(character, dict):
            print(f"ERROR: CharacterTile2 recibió datos de personaje inválidos: {character}. Estableciendo valores predeterminados.")
            self.character_data = None # Aseguramos que sea None si es inválido
            self.character_id = 0
            self.is_favorite = False
            self.character_name = "Personaje Desconocido"
            # Puedes establecer una imagen de error por defecto
            self.source = "assets/placeholder_error.png" # Asegúrate de tener esta imagen
            return # Salimos del __init__ para evitar más errores con datos nulos
        
        # --- Asignación de datos válidos a las propiedades de Kivy ---
        self.character_data = character
        self.controller = controller
        
        self.character_id = character.get('id', 0) # Usa .get() con valor por defecto
        self.character_name = character.get('name', 'Nombre No Disponible')
        
        # El estado de favorito se verifica con el controlador
        self.is_favorite = self.controller.is_favorite(self.character_id) if self.controller else False

        # NOTA: No accedemos a self.ids.xxx aquí, eso se hace en on_kv_post
        # self.source ya no se asigna aquí; se asigna en on_kv_post o en el KV.
        # En MDSmartTile, 'source' es una propiedad, así que si lo seteas en __init__
        # antes de super().__init__ puede ser problemático o debe ser self.source = character.get('image', '').
        # Lo más seguro es hacerlo en on_kv_post.

    def on_kv_post(self, base_widget):
        """
        Método llamado después de que el archivo KV ha sido aplicado y los IDs están disponibles.
        Este es el lugar seguro para actualizar elementos de la interfaz de usuario que dependen de los IDs.
        """
        super().on_kv_post(base_widget) # Llama al método base de MDSmartTile

        # --- Actualización de la UI basada en las propiedades de Kivy ---
        if self.character_data: # Solo si tenemos datos válidos
            # Asignar la imagen principal del tile
            self.source = self.character_data.get('image', "assets/placeholder_error.png")
            
            # Actualizar el texto del nombre del personaje (vinculado a character_name en KV)
            if 'character_image_text' in self.ids:
                # Ya está vinculado a self.character_name en KV, no se necesita reasignar aquí.
                pass 
            else:
                print("Advertencia: El ID 'character_image_text' no se encontró en el KV de CharacterTile2.")
            
            # Actualizar el icono de favorito (vinculado a is_favorite en KV)
            self._update_favorite_icon_display() # Llamamos a la función auxiliar
        else:
            print("CharacterTile2.on_kv_post: character_data es None, mostrando UI de error.")
            # Si los datos eran inválidos, asegura que la UI muestre el estado de error
            self.source = "assets/placeholder_error.png"
            if 'character_image_text' in self.ids:
                self.ids.character_image_text.text = "Error al cargar"
            if 'favorite_icon' in self.ids:
                self.ids.favorite_icon.icon = "alert-circle-outline" # Ícono de error
                self.ids.favorite_icon.icon_color = (1, 0, 0, 1) # Rojo


    # --- Callbacks de propiedades para actualizaciones automáticas de UI ---
    def on_is_favorite(self, instance, value):
        """
        Este método se llama automáticamente cuando la propiedad 'is_favorite' cambia.
        Actualiza el ícono de favorito en la UI.
        """
        self._update_favorite_icon_display()

    # --- Métodos auxiliares ---
    def _update_favorite_icon_display(self):
        """
        Función auxiliar para actualizar el icono de favorito en el KV.
        """
        if 'favorite_icon' in self.ids:
            self.ids.favorite_icon.icon = "heart" if self.is_favorite else "heart-outline"
            self.ids.favorite_icon.icon_color = (1, 0, 0, 1) if self.is_favorite else (1, 1, 1, 1)
        else:
            print("Advertencia: El ID 'favorite_icon' no se encontró en el KV de CharacterTile2.")

    # --- Lógica de Negocio / Interacción ---
    def toggle_favorite(self):
        """
        Alterna el estado de favorito del personaje a través del controlador.
        """
        if self.controller and self.character_data:
            success = self.controller.toggle_favorite(self.character_data)
            if success:
                # Al cambiar la propiedad 'is_favorite', se disparará on_is_favorite
                self.is_favorite = not self.is_favorite
        else:
            print("Error: Controlador o datos de personaje no disponibles para alternar favorito.")

    # --- Implementación de Long Press/Short Press ---
    def on_touch_down(self, touch):
        """Maneja el inicio de un toque en el tile (para long press)."""
        if self.collide_point(*touch.pos):
            self._last_touch_time = time.time()
            self._is_long_press_fired = False
            # Programa el evento de 'long press'
            self._long_press_event = Clock.schedule_once(
                self._do_long_press, self.LONG_PRESS_TIME
            )
        return super().on_touch_down(touch)

    def on_touch_up(self, touch):
        """Maneja la liberación de un toque en el tile (para long press/short press)."""
        if self.collide_point(*touch.pos):
            if self._long_press_event:
                Clock.unschedule(self._long_press_event) # Cancela el long press si el dedo se levanta antes
                self._long_press_event = None
            
            # Si el 'long press' no se disparó, es un 'short press'
            if not self._is_long_press_fired:
                self.on_short_press() # Llama al método para el short press
            
            # Resetear flags para el próximo toque
            self._last_touch_time = None
            self._is_long_press_fired = False 
        return super().on_touch_up(touch)

    def _do_long_press(self, dt):
        """Método que se ejecuta si se detecta un 'long press'."""
        if self._last_touch_time is not None: 
            self._is_long_press_fired = True # Marca que el long press ocurrió
            self.toggle_favorite() # Ejecuta la acción de favorito
            self._last_touch_time = None # Reset para prevenir acción de short press
        self._long_press_event = None

    def on_short_press(self):
        """
        Maneja un 'short press' en el tile.
        Navega a la pantalla de detalles del personaje.
        """
        if self.controller and self.character_data:
            print(f"Short press en el personaje: {self.character_data['name']}")
            # Asegúrate de que tu controlador tenga este método
            self.controller.navigate_to_character_detail(self.character_data)
        else:
            print("Error: Controlador o datos de personaje no disponibles para navegación de short press.")































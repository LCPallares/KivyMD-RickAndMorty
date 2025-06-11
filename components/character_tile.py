from kivymd.uix.imagelist import MDSmartTile
from kivy.properties import NumericProperty, BooleanProperty, StringProperty

from kivy.lang import Builder
Builder.load_file('components/character_tile.kv')

class CharacterTile(MDSmartTile):
    """Versión ultra-minimalista con manejo seguro de IDs"""
    character_id = NumericProperty(0)
    is_favorite = BooleanProperty(False)
    character_name = StringProperty('')
    character_source = StringProperty('')  # kivymd 2.0.1.dev0

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
        #self.source = character.get('image', "assets/placeholder_error.png")
        self.character_source = character.get('image', "assets/placeholder_error.png")

        #self.update_favorite_icon()

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

    def update_favorite_icon(self):
        """Actualiza el estado del ícono basado en la base de datos"""
        if self.controller:
            self.is_favorite = self.controller.is_favorite(self.character_id)
        else:
            self.is_favorite = False

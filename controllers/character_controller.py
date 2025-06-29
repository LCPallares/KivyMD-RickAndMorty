from utils.api_client import RickMortyAPI
from models.favorite_model import Favorite
from views.characters.characters_list import CharactersListScreen
from views.characters.character_detail import CharacterDetailScreen

class CharacterController:
    def __init__(self, app):
        self.app = app

    def load_views(self):
        views = [
            CharactersListScreen(name='characters_list', controller=self),
            CharacterDetailScreen(name='character_detail', controller=self)
       ]
        for view in views:
            self.app.sm.add_widget(view)

        self.app.sm.current = 'characters_list'
        print("load_views character")

    def get_characters(self, page=1):
        return RickMortyAPI.get_characters(page)

    def get_character(self, character_id):
        print("DEBUG: llamada funcion get_character de controlador")
        return RickMortyAPI.get_character(character_id)

    def toggle_favorite(self, character):
        """Alterna el estado de favorito"""
        if not self.app.auth_controller.current_user:
            return False
            
        user_id = self.app.auth_controller.current_user['id']
        character_id = character['id']
        
        if self.is_favorite(character_id):
            return Favorite.remove_favorite(user_id, character_id)
            # Favorite.remove_favorite(user_id, character_id)
            # return False
        else:
            return Favorite.add_favorite(user_id, character_id, character['name'], character['image'])
            # Favorite.add_favorite(user_id, character_id, character['name'], character['image'])
            # return True

    def is_favorite(self, character_id):
        """Verifica si un personaje es favorito"""
        if not self.app.auth_controller.current_user:
            return False
        user_id = self.app.auth_controller.current_user['id']
        favorites = Favorite.get_user_favorites(user_id)
        return any(fav['character_id'] == character_id for fav in favorites)


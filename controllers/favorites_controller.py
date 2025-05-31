from models.favorite_model import Favorite
from views.favorites.favorites_list import FavoritesListScreen

class FavoritesController:
    def __init__(self, app):
        self.app = app

    def load_views(self):
        self.app.sm.add_widget(
            FavoritesListScreen(name='favorites_list', controller=self)
        )
        #self.app.sm.current = 'favorites_list'
        print("load_views favorites")

    def get_user_favorites(self, user_id):
        return Favorite.get_user_favorites(user_id)

    def remove_favorite(self, character_id):
        if not self.app.auth_controller.current_user:
            return False
            
        user_id = self.app.auth_controller.current_user['id']
        return Favorite.remove_favorite(user_id, character_id)
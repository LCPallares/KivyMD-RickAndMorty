import requests

class RickMortyAPI:
    BASE_URL = 'https://rickandmortyapi.com/api'

    @classmethod
    def get_characters(cls, page=1):
        response = requests.get(f'{cls.BASE_URL}/character?page={page}')
        return response.json().get('results', [])

    @staticmethod
    def get_character(character_id):
        print("DEBUG: llamada funcion get_character de API")
        url = f'https://rickandmortyapi.com/api/character/{character_id}'
        response = requests.get(url)
        return response.json()

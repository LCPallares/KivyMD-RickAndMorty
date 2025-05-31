import requests

class RickMortyAPI:
    BASE_URL = 'https://rickandmortyapi.com/api'

    @classmethod
    def get_characters(cls, page=1):
        response = requests.get(f'{cls.BASE_URL}/character?page={page}')
        return response.json().get('results', [])
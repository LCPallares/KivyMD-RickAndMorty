from models.database import get_db_connection

class Favorite:
    @staticmethod
    def add_favorite(user_id, character_id, character_name, character_image):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                '''INSERT INTO favorites 
                (user_id, character_id, character_name, character_image) 
                VALUES (?, ?, ?, ?)''',
                (user_id, character_id, character_name, character_image)
            )
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
        finally:
            conn.close()

    @staticmethod
    def get_user_favorites(user_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM favorites WHERE user_id = ?', (user_id,))
        favorites = cursor.fetchall()
        conn.close()
        return favorites

    @staticmethod
    def remove_favorite(user_id, character_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'DELETE FROM favorites WHERE user_id = ? AND character_id = ?',
            (user_id, character_id)
        )
        conn.commit()
        affected = cursor.rowcount
        conn.close()
        return affected > 0
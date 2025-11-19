import bcrypt
from sqlite3 import connect

class Auth:
    def check_admin_password(self, input_password: str) -> bool:
        try:
            with connect("./Database/voting.db") as conn:
                cursor = conn.cursor()

                cursor.execute("SELECT password_hash FROM auth LIMIT 1")
                row = cursor.fetchone()

                if row is None:
                    return False

                stored_hash = row[0].encode('utf-8')  # Convert DB string to bytes
                return bcrypt.checkpw(input_password.encode('utf-8'), stored_hash)

        except Exception as e:
            print("Auth error:", e)
            return False
        
    def check_user_password(self, userid: str, input_password: str) -> bool:
        try:
            with connect("./Database/voting.db") as conn:
                cursor = conn.cursor()

                cursor.execute("SELECT password_hash FROM VoterList WHERE id = ?", (userid,))
                row = cursor.fetchone()

                if row is None:
                    return False

                stored_hash = row[0].encode('utf-8')  # Convert DB string to bytes
                return bcrypt.checkpw(input_password.encode('utf-8'), stored_hash)

        except Exception as e:
            print("Auth error:", e)
            return False

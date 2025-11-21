import bcrypt
from db import get_conn

ADMIN_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS admin (
id INTEGER PRIMARY KEY AUTOINCREMENT,
password_hash TEXT NOT NULL
);
"""




class Auth:
    def __init__(self):
        # Ensure admin table exists
        with get_conn() as conn:
            conn.execute(ADMIN_TABLE_SQL)
            conn.commit()


    def check_admin_password(self, input_password: str) -> bool:
        try:
            with get_conn() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT password_hash FROM admin LIMIT 1")
                row = cursor.fetchone()
                if row is None:
                    return False
                stored_hash = row[0].encode('utf-8')
                return bcrypt.checkpw(input_password.encode('utf-8'), stored_hash)
        except Exception as e:
            print('Auth error:', e)
            return False


    def set_admin_password(self, plain_password: str):
        pw_hash = bcrypt.hashpw(plain_password.encode('utf-8'), bcrypt.gensalt())
        with get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM admin")
            cursor.execute("INSERT INTO admin (password_hash) VALUES (?)", (pw_hash.decode('utf-8'),))
            conn.commit()

    def check_user_password(self, userid: int, input_password: str) -> bool:
        try:
            with get_conn() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT password_hash FROM VoterList WHERE id = ?", (userid,))
                row = cursor.fetchone()
                if row is None:
                    return False
                stored_hash = row[0].encode('utf-8')
                return bcrypt.checkpw(input_password.encode('utf-8'), stored_hash)
        except Exception as e:
            print('Auth error:', e)
            return False
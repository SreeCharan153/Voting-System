import bcrypt
from db import get_conn


class VoterManager:
    def create_voter(self, name: str, password: str) -> dict:
        password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        with get_conn() as conn:
            cursor = conn.cursor()
            try:
                cursor.execute("INSERT INTO VoterList (name, password_hash) VALUES (?, ?)", (name, password_hash))
                conn.commit()
                return {"ok": True, "message": f"Voter '{name}' created", "voter_id": cursor.lastrowid}
            except Exception as e:
                return {"ok": False, "message": str(e)}
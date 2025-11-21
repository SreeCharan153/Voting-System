from db import get_conn


class PartyManager:
    def create_party(self, name: str, president: str, candidate: str) -> dict:
        with get_conn() as conn:
            cursor = conn.cursor()
            try:
                cursor.execute("SELECT id FROM parties WHERE name = ?", (name,))
                if cursor.fetchone():
                    return {"ok": False, "message": f"Party '{name}' already exists"}
                cursor.execute(
                "INSERT INTO parties (name, party_president, party_candidate) VALUES (?, ?, ?)",
                (name, president, candidate)
                )
                conn.commit()
                return {"ok": True, "message": f"Party '{name}' created", "party_id": cursor.lastrowid}
            except Exception as e:
                return {"ok": False, "message": str(e)}
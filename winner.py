from db import get_conn


def winner():
    with get_conn() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT name, votes FROM parties ORDER BY votes DESC LIMIT 1")
        result = cursor.fetchone()
        if result:
            name, votes = result
            return {"ok": True, "winner": name, "votes": votes}
        else:
            return {"ok": False, "message": "No parties found"}
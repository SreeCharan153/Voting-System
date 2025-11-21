from db import get_conn


class Parties:
    def get_parties(self):
        result = []
        with get_conn() as conn:
            cursor = conn.cursor()
            try:
                cursor.execute("SELECT id, name, votes, party_president, party_candidate FROM parties")
                parties = cursor.fetchall()
                for party in parties:
                    pid, name, votes, president, candidate = party
                    result.append({"id": pid, "name": name, "votes": votes, "president": president, "candidate": candidate})
            except Exception as e:
                return {"ok": False, "message": str(e)}
        return {"ok": True, "parties": result}
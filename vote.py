from db import get_conn


class Voting:
    def add_vote(self, party_id: int, voter_id: int) -> dict:
        with get_conn() as conn:
            cursor = conn.cursor()
            try:
                cursor.execute("BEGIN IMMEDIATE")
                cursor.execute("SELECT voting_state FROM VoterList WHERE id = ?", (voter_id,))
                r = cursor.fetchone()
                if not r:
                    conn.rollback()
                    return {"ok": False, "message": "Voter not found"}
                if r[0] == 1:
                    conn.rollback()
                    return {"ok": False, "message": "Voter already voted"}

                cursor.execute("SELECT id FROM parties WHERE id = ?", (party_id,))
                if cursor.fetchone() is None:
                    conn.rollback()
                    return {"ok": False, "message": "Party not found"}

                cursor.execute("UPDATE parties SET votes = votes + 1 WHERE id = ?", (party_id,))
                cursor.execute("UPDATE VoterList SET voting_state = 1 WHERE id = ? AND voting_state = 0", (voter_id,))
                if cursor.rowcount == 0:
                    conn.rollback()
                    return {"ok": False, "message": "Concurrent vote detected"}
                conn.commit()
                return {"ok": True, "message": "Vote added"}
            except Exception as e:
                conn.rollback()
                return {"ok": False, "message": str(e)}

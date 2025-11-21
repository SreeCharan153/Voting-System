from db import get_conn


class Voting:
    def add_vote(self, party_id: int, voter_id: int) -> dict:
        with get_conn() as conn:
            cursor = conn.cursor()


            # Check voter exists
            cursor.execute("SELECT id, voting_state FROM VoterList WHERE id = ?", (voter_id,))
            voter = cursor.fetchone()
            if voter is None:
                return {"ok": False, "message": "Voter does not exist"}


            if voter[1] == 1:
                return {"ok": False, "message": "Voter has already voted"}

            # Check party exists
            cursor.execute("SELECT id FROM parties WHERE id = ?", (party_id,))
            party = cursor.fetchone()
            if party is None:
                return {"ok": False, "message": "Party does not exist"}


            # Add vote
            try:
                cursor.execute("UPDATE parties SET votes = votes + 1 WHERE id = ?", (party_id,))
                cursor.execute("UPDATE VoterList SET voting_state = 1 WHERE id = ?", (voter_id,))
                conn.commit()
                return {"ok": True, "message": "Vote added successfully"}
            except Exception as e:
                return {"ok": False, "message": str(e)}
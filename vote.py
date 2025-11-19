from sqlite3 import connect

class Voting:
    def add_vote(self, partyid, voterid):
        with connect("./Database/voting.db") as conn:
            cursor = conn.cursor()

            # Check voter
            cursor.execute("SELECT id, VoteingState FROM VoterList WHERE VoterID = ?", (voterid,))
            voter = cursor.fetchone()

            if voter is None:
                return "Voter does not exist"

            if voter[1] == 1:  # already voted
                return "Voter has already voted"

            # Update party votes
            cursor.execute("UPDATE parties SET votes = votes + 1 WHERE id = ?", (partyid,))

            # Mark voter as voted
            cursor.execute("UPDATE VoterList SET VoteingState = 1 WHERE VoterID = ?", (voterid,))

            conn.commit()

        return "Vote added successfully"

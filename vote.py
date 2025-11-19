from sqlite3 import connect
class voting:
    def add_vote(self,id):
        with connect("voting_system.db") as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE parties SET votes = votes + 1 WHERE id = ?", (id,))
            conn.commit()

        return "Vote added successfully"
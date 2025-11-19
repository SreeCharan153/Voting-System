from sqlite3 import connect

class AddVoter:
    def __init__(self, voter_name):
        self.voter_name = voter_name

        with connect("./Database/voting.db") as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS VoterList(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    voteingstate BLOB NOT NULL DEFAULT 'False'
                );
            """)
            conn.commit()

    def create_voter(self):
        with connect("./Database/voting.db") as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO VoterList (name) VALUES (?)", (self.voter_name,))
            conn.commit()

        return f"Voter '{self.voter_name}' created successfully."
    


v = AddVoter("John Doe")
print(v.create_voter())


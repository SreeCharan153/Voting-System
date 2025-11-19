from sqlite3 import connect
class addparty:
    def __init__(self, party_name):
        self.party_name = party_name
        with connect("./Database/voting.db") as conn:
            self.cursor = conn.cursor()
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS parties
                                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT NOT NULL,
                                votes INTEGER DEFAULT 0,
                                partypresident TEXT NOT NULL,
                                partycandidate TEXT NOT NULL

                                )''')
            conn.commit()
    
    def create_party(self,party_prisident, party_candidate):
        with connect("./Database/voting.db") as conn:
            self.cursor = conn.cursor()
            self.cursor.execute("INSERT INTO parties (name, partypresident, partycandidate) VALUES (?, ?, ?)", (self.party_name, party_prisident,party_candidate))
            conn.commit()
        return f"Party '{self.party_name}' created successfully."
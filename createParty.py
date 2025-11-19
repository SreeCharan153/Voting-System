from sqlite3 import connect
class addparty:
    def __init__(self, party_name):
        self.party_name = party_name
        with connect("voting_system.db") as conn:
            self.cursor = conn.cursor()
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS parties
                                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT NOT NULL,
                                votes INTEGER DEFAULT 0)''')
            conn.commit()
    
    def create_party(self,party_prisident, party_candidate):
        with connect("voting_system.db") as conn:
            self.cursor = conn.cursor()
            self.cursor.execute("INSERT INTO parties (PartyName, PartyPresident, PartyCandadit) VALUES (?, ?, ?)", (self.party_name, party_prisident,party_candidate))
            conn.commit()
        return f"Party '{self.party_name}' created successfully."
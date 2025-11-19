from sqlite3 import connect

class Parties:
    def get_parties(self):
        result = []
        with connect("./Database/voting.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, name FROM parties")
            parties = cursor.fetchall()
            for party in parties:
                party_id, party_name = party
                result.append(f"{party_id}:{party_name}")
        return "\n".join(result)
    

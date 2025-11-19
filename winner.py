from sqlite3 import connect
def winner():
    with connect("voting_system.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT name, votes FROM parties ORDER BY votes DESC LIMIT 1")
        result = cursor.fetchone()
        if result:
            name, votes = result
            return f"The winning party is {name} with {votes} votes."
        else:
            return "No parties found."


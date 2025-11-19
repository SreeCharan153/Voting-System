class addparty:
    def __init__(self, party_name):
        self.party_name = party_name

    
    def create_party(self,party_prisident, party_candidate):
        with open("./partys/parties.txt", "r+") as file:
            lines = file.readlines()
            last_line = lines[-1]
            parts = last_line.strip().split(":")
            party_id = int(parts[0]) + 1
            file.write(f"{party_id}:{self.party_name}:0\n")
        with open(f"./partys/{self.party_name}.txt", "w") as file:
            file.write(f"Party President:{party_prisident}\n")
            file.write(f"Party Candidate:{party_candidate}\n")
        return f"Party '{self.party_name}' created successfully."
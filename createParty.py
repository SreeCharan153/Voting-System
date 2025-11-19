class addparty:
    def __init__(self, party_name):
        self.party_name = party_name

    
    def create_party(self):
        with open("./partys/parties.txt", "a") as file:
            file.write(f"{self.party_name}\n")
        with open(f"./partys/{self.party_name}.txt", "w") as file:
            file.write(f"Votes: {self.party_name} : 0\n")
        return f"Party '{self.party_name}' created successfully."
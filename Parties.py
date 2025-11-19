def get_parties():
    parties = []
    id = []
    with open("./partys/parties.txt", "r") as f:
        id = f.readlines().strip().split(":")
        id = [identity.strip() for identity in id]
        parties = f.readlines().strip().split(":")
        parties = [party.strip() for party in parties]
    return f"{parties}, {id}"
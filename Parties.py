def get_parties():
    result = []
    with open("./partys/parties.txt", "r") as f:
        lines = f.readlines()
        for l in lines:
            party = l.strip().split(":")
            party_id = party[0]
            party_name = party[1]
            result.append(f"{party_id}:{party_name}")
    return "\n".join(result)
print(get_parties())
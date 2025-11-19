from createParty import addparty
with open("password.txt", "r") as f:
    stored_password = f.read().strip().split(":")[1]
password = input("Enter Password: ")
if password != stored_password:
    print("Incorrect Password. Access Denied.")
    exit()
val = int(input("Enter a number: "))
match val:
    case 1:
        party_name = input("Enter Party Name: ")
        party = addparty(party_name)
        result = party.create_party()
        print(result)
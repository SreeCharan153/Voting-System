from createParty import addparty
with open("password.txt", "r") as f:
    stored_password = f.read().strip().split(":")[1]
password = input("Enter Password: ")
if password != stored_password:
    print("Incorrect Password. Access Denied.")
    exit()
val = int(input("Enter a number: "))
match val:
    case 0:
        from Parties import Parties
        parties = Parties()
        result = parties.get_parties()
        print(result)
    case 1:
        party_name = input("Enter Party Name: ")
        party_prisident = input("Enter Party President: ")
        party_candidate = input("Enter Party Candidate: ")
        party = addparty(party_name)
        result = party.create_party(party_prisident, party_candidate)
        print(result)
    case 2:
        from vote import Voting
        party_id = int(input("Enter Party ID to vote for: "))
        voter_id = int(input("Enter your Voter ID: "))
        vote = Voting()
        result = vote.add_vote(party_id, voter_id)
        print(result)
    case _:
        print("Invalid Input")
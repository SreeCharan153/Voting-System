Refactored Voting Backend


How to run:
1. Create & activate a Python venv
python -m venv .venv
source .venv/bin/activate # Linux/Mac
.venv\Scripts\activate # Windows


2. Install requirements:
pip install fastapi uvicorn pydantic bcrypt


3. Run app:
uvicorn main:app --reload --port 8000


Example flows (curl):


# Set admin password
curl -X POST http://127.0.0.1:8000/auth/set_admin_password -H 'Content-Type: application/json' -d '{"input_password":"secret123"}'


# Create party
curl -X POST http://127.0.0.1:8000/create_party -H 'Content-Type: application/json' -d '{"party_name":"Alpha","party_president":"Alice","party_candidate":"Bob"}'


# Register voter
curl -X POST http://127.0.0.1:8000/register_voter -H 'Content-Type: application/json' -d '{"name":"John","password":"hunter2"}'


# Vote
curl -X POST http://127.0.0.1:8000/vote -H 'Content-Type: application/json' -d '{"party_id":1,"voter_id":1}'


# Get winner
curl http://127.0.0.1:8000/winner


Notes:
- All DB files are created under ./Database/voting.db
- The refactor focuses on consistent schema, defensive programming, and clear separation of responsibilities.

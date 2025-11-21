from fastapi import FastAPI, HTTPException
from models import Party, Vote, VoterRegister, AdminPasswordCheck, VoterPasswordCheck
from createParty import PartyManager
from createvoter import VoterManager
from Parties import Parties
from vote import Voting
from auth import Auth
from winner import winner as get_winner

app = FastAPI(title='Refactored Voting API')
@app.get('/health')
def health():
    return {'status': 'ok'}


@app.post('/auth/set_admin_password')
def set_admin_password(payload: AdminPasswordCheck):
    a = Auth()
    a.set_admin_password(payload.input_password)
    return {'ok': True, 'message': 'Admin password set'}


@app.post('/auth/check_admin_password')
def check_admin_password(payload: AdminPasswordCheck):
    a = Auth()
    valid = a.check_admin_password(payload.input_password)
    return {'ok': valid}


@app.post('/auth/check_user_password')
def check_user_password(payload: VoterPasswordCheck):
    a = Auth()
    valid = a.check_user_password(payload.voter_id, payload.input_password)
    return {'ok': valid}


@app.post('/create_party')
def api_create_party(p: Party):
    pm = PartyManager()
    res = pm.create_party(p.party_name, p.party_president, p.party_candidate)
    if not res.get('ok'):
        raise HTTPException(status_code=400, detail=res.get('message'))
    return res


@app.get('/parties')
def api_get_parties():
    p = Parties()
    return p.get_parties()


@app.post('/register_voter')
def api_register_voter(v: VoterRegister):
    vm = VoterManager()
    res = vm.create_voter(v.name, v.password)
    if not res.get('ok'):
        raise HTTPException(status_code=400, detail=res.get('message'))
    return res


@app.post('/vote')
def api_vote(v: Vote):
    voting = Voting()
    res = voting.add_vote(v.party_id, v.voter_id)
    if not res.get('ok'):
        raise HTTPException(status_code=400, detail=res.get('message'))
    return res

@app.get('/winner')
def api_winner():
    return get_winner()
from pydantic import BaseModel, Field


class Party(BaseModel):
    party_name: str = Field(..., min_length=1)
    party_president: str = Field(..., min_length=1)
    party_candidate: str = Field(..., min_length=1)


class Vote(BaseModel):
    party_id: int
    voter_id: int


class VoterRegister(BaseModel):
    name: str = Field(..., min_length=1)
    password: str = Field(..., min_length=6)


class AdminPasswordCheck(BaseModel):
    input_password: str

class VoterPasswordCheck(BaseModel):
    voter_id: int
    input_password: str
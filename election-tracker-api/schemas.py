from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


# Politician Schemas
class PoliticianBase(BaseModel):
    name: str
    vote: int = 0
    party: str
    area_id: int


class PoliticianCreate(PoliticianBase):
    pass


class PoliticianUpdate(BaseModel):
    name: Optional[str] = None
    vote: Optional[int] = None
    party: Optional[str] = None
    area_id: Optional[int] = None


class PoliticianResponse(BaseModel):
    id: int
    name: str
    party: str
    vote: int
    area: int

    class Config:
        from_attributes = True


# Constituency Schemas
class ConstituencyBase(BaseModel):
    election_area: str


class ConstituencyCreate(ConstituencyBase):
    pass


class ConstituencyUpdate(BaseModel):
    election_area: Optional[str] = None


class ConstituencyResponse(BaseModel):
    id: int
    election_area: str

    class Config:
        from_attributes = True


class ConstituencyWithCandidates(BaseModel):
    id: int
    election_area: str
    candidates: List[PoliticianResponse]

    class Config:
        from_attributes = True


# Rankings Response Schema
class RankingsResponse(BaseModel):
    id: int
    updated_time: str
    data: List[ConstituencyWithCandidates]

    class Config:
        from_attributes = True

from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime

from database import engine, get_db, Base
from models import Politician, Constituency
import crud
from schemas import (
    PoliticianCreate, PoliticianUpdate, PoliticianResponse,
    ConstituencyCreate, ConstituencyUpdate, ConstituencyResponse,
    ConstituencyWithCandidates, RankingsResponse
)

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Election Tracker API",
    description="API for tracking election results across constituencies",
    version="1.0.0"
)

# CORS middleware for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ==================== POLITICIAN ENDPOINTS ====================

@app.get("/politicians", response_model=List[PoliticianResponse], tags=["Politicians"])
def get_politicians(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all politicians"""
    politicians = crud.get_politicians(db, skip=skip, limit=limit)
    return [
        PoliticianResponse(
            id=p.id,
            name=p.name,
            party=p.party,
            vote=p.vote,
            area=p.area_id
        ) for p in politicians
    ]


@app.get("/politicians/{politician_id}", response_model=PoliticianResponse, tags=["Politicians"])
def get_politician(politician_id: int, db: Session = Depends(get_db)):
    """Get a single politician by ID"""
    politician = crud.get_politician(db, politician_id)
    if politician is None:
        raise HTTPException(status_code=404, detail="Politician not found")
    return PoliticianResponse(
        id=politician.id,
        name=politician.name,
        party=politician.party,
        vote=politician.vote,
        area=politician.area_id
    )


@app.post("/politicians", response_model=PoliticianResponse, tags=["Politicians"])
def create_politician(politician: PoliticianCreate, db: Session = Depends(get_db)):
    """Create a new politician"""
    # Check if constituency exists
    constituency = crud.get_constituency(db, politician.area_id)
    if constituency is None:
        raise HTTPException(status_code=400, detail="Constituency not found")
    
    new_politician = crud.create_politician(db, politician)
    return PoliticianResponse(
        id=new_politician.id,
        name=new_politician.name,
        party=new_politician.party,
        vote=new_politician.vote,
        area=new_politician.area_id
    )


@app.patch("/politicians/{politician_id}", response_model=PoliticianResponse, tags=["Politicians"])
def update_politician(politician_id: int, politician: PoliticianUpdate, db: Session = Depends(get_db)):
    """Update an existing politician"""
    updated_politician = crud.update_politician(db, politician_id, politician)
    if updated_politician is None:
        raise HTTPException(status_code=404, detail="Politician not found")
    return PoliticianResponse(
        id=updated_politician.id,
        name=updated_politician.name,
        party=updated_politician.party,
        vote=updated_politician.vote,
        area=updated_politician.area_id
    )


# ==================== CONSTITUENCY ENDPOINTS ====================

@app.get("/constituencies", response_model=List[ConstituencyResponse], tags=["Constituencies"])
def get_constituencies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all constituencies"""
    return crud.get_constituencies(db, skip=skip, limit=limit)


@app.get("/constituencies/{constituency_id}", response_model=ConstituencyWithCandidates, tags=["Constituencies"])
def get_constituency(constituency_id: int, db: Session = Depends(get_db)):
    """Get a single constituency with its candidates"""
    constituency = crud.get_constituency(db, constituency_id)
    if constituency is None:
        raise HTTPException(status_code=404, detail="Constituency not found")
    
    # Get top 3 candidates ordered by votes
    candidates = crud.get_politicians_by_area(db, constituency_id)[:3]
    
    return ConstituencyWithCandidates(
        id=constituency.id,
        election_area=constituency.election_area,
        candidates=[
            PoliticianResponse(
                id=c.id,
                name=c.name,
                party=c.party,
                vote=c.vote,
                area=c.area_id
            ) for c in candidates
        ]
    )


@app.post("/constituencies", response_model=ConstituencyResponse, tags=["Constituencies"])
def create_constituency(constituency: ConstituencyCreate, db: Session = Depends(get_db)):
    """Create a new constituency"""
    # Check if constituency already exists
    existing = crud.get_constituency_by_name(db, constituency.election_area)
    if existing:
        raise HTTPException(status_code=400, detail="Constituency already exists")
    
    return crud.create_constituency(db, constituency)


@app.patch("/constituencies/{constituency_id}", response_model=ConstituencyResponse, tags=["Constituencies"])
def update_constituency(constituency_id: int, constituency: ConstituencyUpdate, db: Session = Depends(get_db)):
    """Update an existing constituency"""
    updated_constituency = crud.update_constituency(db, constituency_id, constituency)
    if updated_constituency is None:
        raise HTTPException(status_code=404, detail="Constituency not found")
    return updated_constituency


# ==================== RANKINGS ENDPOINT ====================

@app.get("/rankings", response_model=RankingsResponse, tags=["Rankings"])
def get_rankings(db: Session = Depends(get_db)):
    """Get rankings of all constituencies with top 3 candidates each"""
    constituencies = crud.get_all_rankings(db)
    
    data = []
    for constituency in constituencies:
        # Get top 3 candidates ordered by votes
        candidates = crud.get_politicians_by_area(db, constituency.id)[:3]
        
        data.append(ConstituencyWithCandidates(
            id=constituency.id,
            election_area=constituency.election_area,
            candidates=[
                PoliticianResponse(
                    id=c.id,
                    name=c.name,
                    party=c.party,
                    vote=c.vote,
                    area=c.area_id
                ) for c in candidates
            ]
        ))
    
    return RankingsResponse(
        id=1,
        updated_time=datetime.now().strftime("%H:%M:%S"),
        data=data
    )


# ==================== ROOT ENDPOINT ====================

@app.get("/", tags=["Root"])
def read_root():
    """Root endpoint"""
    return {
        "message": "Welcome to Election Tracker API",
        "docs": "/docs",
        "endpoints": {
            "politicians": "/politicians",
            "constituencies": "/constituencies",
            "rankings": "/rankings"
        }
    }

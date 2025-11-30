from sqlalchemy.orm import Session
from sqlalchemy import desc
from models import Politician, Constituency
from schemas import (
    PoliticianCreate, PoliticianUpdate,
    ConstituencyCreate, ConstituencyUpdate
)


# ==================== POLITICIAN CRUD ====================

def get_politicians(db: Session, skip: int = 0, limit: int = 100):
    """Get all politicians"""
    return db.query(Politician).offset(skip).limit(limit).all()


def get_politician(db: Session, politician_id: int):
    """Get a single politician by ID"""
    return db.query(Politician).filter(Politician.id == politician_id).first()


def get_politicians_by_area(db: Session, area_id: int):
    """Get all politicians in a constituency, ordered by votes descending"""
    return db.query(Politician).filter(
        Politician.area_id == area_id
    ).order_by(desc(Politician.vote)).all()


def create_politician(db: Session, politician: PoliticianCreate):
    """Create a new politician"""
    db_politician = Politician(
        name=politician.name,
        vote=politician.vote,
        party=politician.party,
        area_id=politician.area_id
    )
    db.add(db_politician)
    db.commit()
    db.refresh(db_politician)
    return db_politician


def update_politician(db: Session, politician_id: int, politician: PoliticianUpdate):
    """Update an existing politician"""
    db_politician = db.query(Politician).filter(Politician.id == politician_id).first()
    if db_politician:
        update_data = politician.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_politician, key, value)
        db.commit()
        db.refresh(db_politician)
    return db_politician


def delete_politician(db: Session, politician_id: int):
    """Delete a politician"""
    db_politician = db.query(Politician).filter(Politician.id == politician_id).first()
    if db_politician:
        db.delete(db_politician)
        db.commit()
        return True
    return False


# ==================== CONSTITUENCY CRUD ====================

def get_constituencies(db: Session, skip: int = 0, limit: int = 100):
    """Get all constituencies"""
    return db.query(Constituency).offset(skip).limit(limit).all()


def get_constituency(db: Session, constituency_id: int):
    """Get a single constituency by ID"""
    return db.query(Constituency).filter(Constituency.id == constituency_id).first()


def get_constituency_by_name(db: Session, election_area: str):
    """Get constituency by area name"""
    return db.query(Constituency).filter(Constituency.election_area == election_area).first()


def create_constituency(db: Session, constituency: ConstituencyCreate):
    """Create a new constituency"""
    db_constituency = Constituency(election_area=constituency.election_area)
    db.add(db_constituency)
    db.commit()
    db.refresh(db_constituency)
    return db_constituency


def update_constituency(db: Session, constituency_id: int, constituency: ConstituencyUpdate):
    """Update an existing constituency"""
    db_constituency = db.query(Constituency).filter(Constituency.id == constituency_id).first()
    if db_constituency:
        update_data = constituency.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_constituency, key, value)
        db.commit()
        db.refresh(db_constituency)
    return db_constituency


def delete_constituency(db: Session, constituency_id: int):
    """Delete a constituency"""
    db_constituency = db.query(Constituency).filter(Constituency.id == constituency_id).first()
    if db_constituency:
        db.delete(db_constituency)
        db.commit()
        return True
    return False


# ==================== RANKINGS ====================

def get_all_rankings(db: Session):
    """Get all constituencies with their top 3 candidates"""
    constituencies = db.query(Constituency).all()
    return constituencies

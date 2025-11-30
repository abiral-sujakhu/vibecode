"""
Script to seed the database with initial data for Kathmandu constituencies
"""
from database import SessionLocal, engine, Base
from models import Constituency, Politician

# Create tables
Base.metadata.create_all(bind=engine)


def seed_database():
    db = SessionLocal()
    
    try:
        # Check if data already exists
        existing = db.query(Constituency).first()
        if existing:
            print("Database already has data. Skipping seed.")
            return
        
        # Seed data for Kathmandu constituencies
        constituencies_data = [
            {
                "election_area": "Kathmandu-1",
                "candidates": [
                    {"name": "Prakashman Singh", "vote": 7143, "party": "Nepali Congress"},
                    {"name": "Rabindra Mishra", "vote": 7018, "party": "Rastriya Prajatantra Party"},
                    {"name": "Pukar Bam", "vote": 4115, "party": "Rastriya Swatantra Party"},
                ]
            },
            {
                "election_area": "Kathmandu-2",
                "candidates": [
                    {"name": "Keshav Sthapit", "vote": 8234, "party": "CPN-UML"},
                    {"name": "Sirjana Singh", "vote": 7650, "party": "Nepali Congress"},
                    {"name": "Ramesh Kharel", "vote": 5420, "party": "Maoist Centre"},
                ]
            },
            {
                "election_area": "Kathmandu-3",
                "candidates": [
                    {"name": "Rajendra Prasad Pandey", "vote": 9120, "party": "Nepali Congress"},
                    {"name": "Deepak Bohara", "vote": 8540, "party": "CPN-UML"},
                    {"name": "Sunita Dangol", "vote": 6780, "party": "Rastriya Swatantra Party"},
                ]
            },
            {
                "election_area": "Kathmandu-4",
                "candidates": [
                    {"name": "Gagan Thapa", "vote": 12500, "party": "Nepali Congress"},
                    {"name": "Sarita Giri", "vote": 9800, "party": "CPN-UML"},
                    {"name": "Bijay Kumar Gachchadar", "vote": 7600, "party": "Loktantrik Samajwadi Party"},
                ]
            },
            {
                "election_area": "Kathmandu-5",
                "candidates": [
                    {"name": "Bhim Rawal", "vote": 11200, "party": "CPN-UML"},
                    {"name": "Minendra Rijal", "vote": 10500, "party": "Nepali Congress"},
                    {"name": "Durga Poudel", "vote": 8300, "party": "Maoist Centre"},
                ]
            },
            {
                "election_area": "Kathmandu-6",
                "candidates": [
                    {"name": "Pradip Gyawali", "vote": 10800, "party": "CPN-UML"},
                    {"name": "Dila Sangraula", "vote": 9650, "party": "Nepali Congress"},
                    {"name": "Narayan Kaji Shrestha", "vote": 8200, "party": "Maoist Centre"},
                ]
            },
            {
                "election_area": "Kathmandu-7",
                "candidates": [
                    {"name": "Ishwor Pokhrel", "vote": 11500, "party": "CPN-UML"},
                    {"name": "Nabindra Raj Joshi", "vote": 10200, "party": "Nepali Congress"},
                    {"name": "Bimala Rai", "vote": 7800, "party": "Rastriya Swatantra Party"},
                ]
            },
            {
                "election_area": "Kathmandu-8",
                "candidates": [
                    {"name": "Madhav Kumar Nepal", "vote": 13200, "party": "CPN (Unified Socialist)"},
                    {"name": "Pushpa Bhusal", "vote": 11800, "party": "CPN-UML"},
                    {"name": "Rajan Bhattarai", "vote": 9500, "party": "Nepali Congress"},
                ]
            },
            {
                "election_area": "Kathmandu-9",
                "candidates": [
                    {"name": "Ram Kumari Jhakri", "vote": 10500, "party": "Maoist Centre"},
                    {"name": "Mahesh Basnet", "vote": 9800, "party": "CPN-UML"},
                    {"name": "Arjun Narsingh KC", "vote": 8600, "party": "Nepali Congress"},
                ]
            },
            {
                "election_area": "Kathmandu-10",
                "candidates": [
                    {"name": "Subas Nembang", "vote": 14200, "party": "CPN-UML"},
                    {"name": "Pushpa Kamal Dahal", "vote": 12800, "party": "Maoist Centre"},
                    {"name": "Sher Bahadur Deuba", "vote": 11500, "party": "Nepali Congress"},
                ]
            },
        ]
        
        # Insert data
        for const_data in constituencies_data:
            # Create constituency
            constituency = Constituency(election_area=const_data["election_area"])
            db.add(constituency)
            db.flush()  # Get the ID
            
            # Create candidates
            for candidate_data in const_data["candidates"]:
                politician = Politician(
                    name=candidate_data["name"],
                    vote=candidate_data["vote"],
                    party=candidate_data["party"],
                    area_id=constituency.id
                )
                db.add(politician)
        
        db.commit()
        print("Database seeded successfully!")
        print(f"Created {len(constituencies_data)} constituencies with candidates.")
        
    except Exception as e:
        print(f"Error seeding database: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    seed_database()

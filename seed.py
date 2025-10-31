
import os
from app.database import SessionLocal, engine
from app.models.student import Student
from sqlalchemy import text

db = SessionLocal()

samples = [
    {"name": "Alice Johnson", "age": 20, "group": "CS101", "email": "alice@example.com", "avatar_url": "https://i.pravatar.cc/150?img=1"},
    {"name": "Bob Smith", "age": 22, "group": "CS101", "email": "bob@example.com", "avatar_url": "https://i.pravatar.cc/150?img=2"},
    {"name": "Charlie Lee", "age": 19, "group": "MATH202", "email": "charlie@example.com"},
    {"name": "Diana King", "age": 23, "group": "MATH202", "email": "diana@example.com"},
    {"name": "Evan Wright", "age": 21, "group": "ENG150", "email": "evan@example.com"},
    {"name": "Fatima Noor", "age": 24, "group": "ENG150", "email": "fatima@example.com"},
    {"name": "George Hall", "age": 18, "group": "PHY200", "email": "george@example.com"},
    {"name": "Hannah Cruz", "age": 20, "group": "PHY200", "email": "hannah@example.com"},
    {"name": "Ivan Petrov", "age": 25, "group": "CS101", "email": "ivan@example.com"},
    {"name": "Jin Park", "age": 26, "group": "MATH202", "email": "jin@example.com"},
]

def main():
    if db.query(Student).first():
        print("Seed skipped: students already exist.")
        return
    for s in samples:
        db.add(Student(**s))
    db.commit()
    print("Seed inserted: {} students".format(len(samples)))

if __name__ == "__main__":
    main()

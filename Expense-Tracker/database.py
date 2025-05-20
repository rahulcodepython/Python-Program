from conf import DATABASE
from models import Lend, Borrow

MODELS = [Lend, Borrow]

db = DATABASE


def initialize_db():
    db.connect()
    print("Connected to database")
    db.create_tables(MODELS, safe=True)
    print("Created tables")


def disconnect_db():
    db.close()
    print("Disconnected from database")

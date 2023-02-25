import os

os.environ['DB_URL'] = 'sqlite:///basic_db.sqlite3'
DB_URL = os.getenv("DB_URL")
USERNAME = os.getenv("USERNAME")


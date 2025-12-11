import os
# Default to local SQLite file; override via env var DATABASE_URL.
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./library_db.db")
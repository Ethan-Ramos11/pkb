import sqlite3
import os
from datetime import datetime
from pathlib import Path
import logging
from typing import Dict, Any, Optional

logger = logging.getLogger(__name__)


def dict_factory(cursor: sqlite3.Cursor, row: tuple) -> Dict[str, Any]:
    """Convert a SQLite row to a dictionary.

    Args:
        cursor: The SQLite cursor object
        row: The row data from the database

    Returns:
        A dictionary where keys are column names and values are row values
    """
    return {col[0]: row[idx] for idx, col in enumerate(cursor.description)}


def get_db_path() -> str:
    """Get the path to the SQLite database file.

    The database path is determined by:
    1. KNOWKEEPER_HOME environment variable if set
    2. Default location in user's home directory (~/.knowkeeper/knowkeeper.db)

    Returns:
        str: The absolute path to the database file
    """
    kk_home = os.environ.get("KNOWKEEPER_HOME", None)

    if kk_home is None:
        kk_home = os.path.join(Path.home(), '.knowkeeper')
    os.makedirs(kk_home, exist_ok=True)
    db_path = os.path.join(kk_home, "knowkeeper.db")

    return db_path


def get_db_connection(db_path=None):
    if db_path is None:
        db_path = get_db_path

    conn = sqlite3.connect(db_path)
    conn.row_factory = dict_factory
    conn.execute("PRAGMA foreign_keys=ON")

    cursor = conn.cursor()
    return conn, cursor

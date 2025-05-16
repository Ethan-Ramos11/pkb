import sqlite3
import os
from datetime import datetime
from pathlib import Path
import logging

logger = logging.getLogger(__name__)


def dict_factory(cursor, row):
    return {col[0]: row[idx] for idx, col in enumerate(cursor.description)}

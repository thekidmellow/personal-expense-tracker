import json
import os
from datetime import datetime
from typing import List, Dict, Any


class DataHandler:
    """Handles all file operations for expense data"""

    def __init__(self, filename: str = "expenses.json"):
        self.filename = filename
        self.ensure_file_exists()
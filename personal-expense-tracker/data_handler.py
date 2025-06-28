import json
import os
from datetime import datetime
from typing import List, Dict, Any


class DataHandler:
    """Handles all file operations for expense data"""

    def __init__(self, filename: str = "expenses.json"):
        self.filename = filename
        self.ensure_file_exists()

    def ensure_file_exists(self) -> None:
        """Create the data file if it doesn't exist"""
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as file:
                json.dump([], file)
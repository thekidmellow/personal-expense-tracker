from datetime import datetime
from typing import List, Dict, Any, Optional
from data_handler import DataHandler

class ExpenseManager:
    """Manages expense operations and business logic"""
    
    def __init__(self):
        self.data_handler = DataHandler()
        self.categories = [
            "Food", "Transportation", "Entertainment", "Shopping",
            "Bills", "Healthcare", "Education", "Other"
        ]
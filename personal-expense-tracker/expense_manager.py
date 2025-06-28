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

    def add_expense(self, amount: float, category: str, description: str) -> bool:
        """Add a new expense"""
        if amount <= 0:
            raise ValueError("Amount must be positive")
        
        if category not in self.categories:
            raise ValueError(f"Invalid category. Choose from: {', '.join(self.categories)}")
        
        expense = {
            "id": self._generate_id(),
            "amount": round(amount, 2),
            "category": category,
            "description": description.strip(),
            "date": datetime.now().isoformat()
        }
        
        expenses = self.data_handler.load_expenses()
        expenses.append(expense)
        return self.data_handler.save_expenses(expenses)
    
    def get_all_expenses(self) -> List[Dict[str, Any]]:
        """Get all expenses"""
        return self.data_handler.load_expenses()
    
    def get_expenses_by_category(self, category: str) -> List[Dict[str, Any]]:
        """Get expenses filtered by category"""
        expenses = self.get_all_expenses()
        return [exp for exp in expenses if exp['category'].lower() == category.lower()]
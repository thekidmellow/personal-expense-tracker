#!/usr/bin/env python3
"""
Personal Expense Tracker
A command-line application to manage personal expenses
"""

import sys
from typing import Optional
from expense_manager import ExpenseManager


class ExpenseTrackerApp:
    """Main application class for the expense tracker"""

    def __init__(self):
        self.expense_manager = ExpenseManager()

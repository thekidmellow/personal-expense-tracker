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


def display_menu(self) -> None:
    """Display the main menu"""
    print("\n" + "="*50)
    print("       PERSONAL EXPENSE TRACKER")
    print("="*50)
    print("1. Add New Expense")
    print("2. View All Expenses")
    print("3. View Expenses by Category")
    print("4. View Spending Summary")
    print("5. View Total Spending")
    print("6. Exit")
    print("-"*50)


def get_user_choice(self) -> str:
    """Get and validate user menu choice"""
    while True:
        choice = input("Enter your choice (1-6): ").strip()
        if choice in ['1', '2', '3', '4', '5', '6']:
            return choice
        print("Invalid choice. Please enter a number between 1 and 6.")

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

    def add_expense(self) -> None:
        """Handle adding a new expense"""
        print("\n--- Add New Expense ---")

        try:
            # Get amount
            amount_str = input("Enter amount ($): ").strip()
            amount = float(amount_str)

            if amount <= 0:
                print("Error: Amount must be positive!")
                return

            # Display and get category
            categories = self.expense_manager.get_categories()
            print("\nAvailable categories:")
            for i, category in enumerate(categories, 1):
                print(f"{i}. {category}")

            while True:
                try:
                    cat_choice = int(input(f"Choose category (1-{len(categories)}): "))
                    if 1 <= cat_choice <= len(categories):
                        category = categories[cat_choice - 1]
                        break
                    else:
                        print(f"Please enter a number between 1 and {len(categories)}")
                except ValueError:
                    print("Please enter a valid number")

            # Get description
            description = input("Enter description: ").strip()
            if not description:
                description = "No description"

            # Add the expense
            success = self.expense_manager.add_expense(amount, category, description)

            if success:
                print(f"\n✓ Expense added successfully!")
                print(f"  Amount: ${amount:.2f}")
                print(f"  Category: {category}")
                print(f"  Description: {description}")
            else:
                print("✗ Failed to save expense. Please try again.")

        except ValueError:
            print("Error: Please enter a valid amount!")
        except Exception as e:
            print(f"Error: {e}")

    def view_all_expenses(self) -> None:
        """Display all expenses"""
        print("\n--- All Expenses ---")
        expenses = self.expense_manager.get_all_expenses()

        if not expenses:
            print("No expenses found.")
            return

        print(f"\n{'ID':<4} {'Date':<12} {'Category':<15} {'Amount':<10} {'Description'}")
        print("-" * 70)

        for expense in expenses:
            date_str = expense['date'][:10]  # Get just the date part
            print(f"{expense['id']:<4} {date_str:<12} {expense['category']:<15} "
                f"${expense['amount']:<9.2f} {expense['description']}")

        total = self.expense_manager.calculate_total(expenses)
        print("-" * 70)
        print(f"{'TOTAL:':<41} ${total:.2f}")

    def view_expenses_by_category(self) -> None:
        """Display expenses filtered by category"""
        print("\n--- View by Category ---")

        categories = self.expense_manager.get_categories()
        print("\nAvailable categories:")
        for i, category in enumerate(categories, 1):
            print(f"{i}. {category}")

        try:
            choice = int(input(f"Choose category (1-{len(categories)}): "))
            if not (1 <= choice <= len(categories)):
                print("Invalid choice!")
                return

            selected_category = categories[choice - 1]
            expenses = self.expense_manager.get_expenses_by_category(selected_category)

            if not expenses:
                print(f"No expenses found for category: {selected_category}")
                return

            print(f"\n--- {selected_category} Expenses ---")
            print(f"{'Date':<12} {'Amount':<10} {'Description'}")
            print("-" * 50)

            for expense in expenses:
                date_str = expense['date'][:10]
                print(f"{date_str:<12} ${expense['amount']:<9.2f} {expense['description']}")

            total = self.expense_manager.calculate_total(expenses)
            print("-" * 50)
            print(f"Total for {selected_category}: ${total:.2f}")

        except ValueError:
            print("Please enter a valid number!")

            
# app.py
from flask import Flask, render_template, request, redirect, url_for
from expense_manager import ExpenseManager

app = Flask(__name__)
manager = ExpenseManager()


@app.route('/')
def index():
    expenses = manager.get_all_expenses()
    total = manager.calculate_total(expenses)
    return render_template('index.html', expenses=expenses, total=total)

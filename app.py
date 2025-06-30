# app.py
from flask import Flask, render_template, request, redirect, url_for
from personal_expense_tracker.expense_manager import ExpenseManager


app = Flask(__name__)
manager = ExpenseManager()


@app.route('/')
def index():
    expenses = manager.get_all_expenses()
    total = manager.calculate_total(expenses)
    return render_template('index.html', expenses=expenses, total=total)


@app.route('/add', methods=['POST'])
def add_expense():
    amount = float(request.form['amount'])
    category = request.form['category']
    description = request.form['description']
    manager.add_expense(amount, category, description)
    return redirect(url_for('index'))


@app.route('/summary')
def summary():
    summary = manager.get_category_summary()
    return render_template('summary.html', summary=summary)


if __name__ == '__main__':
    app.run(debug=True)

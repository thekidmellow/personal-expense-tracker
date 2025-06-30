# app.py
from flask import Flask, render_template, request, redirect, url_for
from expense_manager import ExpenseManager

app = Flask(__name__)
manager = ExpenseManager()
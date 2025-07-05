# Personal Expense Tracker 💰
A command-line Python application to track your daily expenses efficiently, with features to categorize spending, generate summaries, and store everything locally in JSON.

<br>

## **Purpose**
This application helps users track their daily expenses by providing an easy-to-use command-line interface to:
- Add new expenses with categories and descriptions
- View and filter expenses
- Generate spending reports and summaries
- Store data persistently

<br>

## **Value to Users**
- **Simple Expense Management**: Quick and easy way to log daily expenses
- **Category Organization**: Organize expenses into predefined categories
- **Spending Insights**: View summaries and totals to understand spending patterns
- **Data Persistence**: All data is saved locally and persists between sessions
- **No Internet Required**: Works completely offline

<br>

## **Features** ✨
- 📝 Add expenses with categories, amounts, and descriptions
- 📊 View all expenses in a clean tabular format
- 🔍 Filter expenses by category or date range
- 📈 Generate spending summaries and category breakdowns
- 💾 Persistent data storage (JSON format)
- 🏷️ Built-in expense categories:
  - ##### Food 🍔
  - ##### Transportation 🚗
  - ##### Entertainment 🎬
  - ##### Shopping 🛍️
  - ##### Bills 💳
  - ##### Healthcare 🏥
  - ##### Education 📚
  - ##### Other ✨

<br>

## **Project Structure** 📁
personal-expense-tracker/

├── run.py # Main application entry point

├── expense_manager.py # Business logic and expense management

├── data_handler.py # File operations and data persistence

├── requirements.txt # Project dependencies

├── Procfile # Heroku deployment configuration

├── expenses.json # Data storage (auto-created)

└── README.md # Documentation

<br>

## **Application Flowchart** 📈

![Application Flowchart](/img/flowchart_1.png)

<br>

## 1. System Flow

The application follows a **3-layer architecture**:

#### 1. User Interface (CLI)
&rightarrow; Handles input/output via command line  
&rightarrow; Displays menus and collects user choices

#### 2. Application Logic
&rightarrow; Processes commands and validates data  
&rightarrow; Performs calculations and generates reports

#### 3. Data Storage
&rightarrow; Manages reading/writing to `expenses.json`

<br>

## 2. Component Breakdown

<br>

#### A. User Interface Layer (`run.py`)

- Menu System

![Menu system](../personal-expense-tracker/flowchart_2.png)

&nbsp;&nbsp;&nbsp;&nbsp;∘ **Paths:**
  1. **Add Expense**: Collects amount, category, description  
  2. **View Expenses**: Shows table/list views  
  3. **Reports**: Generates summaries/totals

- **Input Validation**
  - Rejects invalid amounts (negative/zero values)
  - Validates category selections (1–8)

<br>

#### B. ExpenseManager (Business Logic)

- **Core Functions:**

![Core functions](../personal-expense-tracker/flowchart_3.png)

&nbsp;&nbsp;&nbsp;&nbsp;∘ **Validation:**
  - Checks amount > 0
  - Verifies category exists

&nbsp;&nbsp;&nbsp;&nbsp;∘ **Calculations:**
  - Sums totals
  - Computes category percentages
  - Averages spending

&nbsp;&nbsp;&nbsp;&nbsp;∘ **Filtering:**
  - Filters by date/category
  - Sorts results

<br>

#### C. DataHandler (Persistence)

- **File Operations:**

![File operations](../personal-expense-tracker/flowchart_4.png)

&nbsp;&nbsp;&nbsp;&nbsp;∘ **Auto-Creation:** Makes expenses.json if missing

&nbsp;&nbsp;&nbsp;&nbsp;∘ **Error Handling:**
- Recovers from corrupt files
- Handles permission errors

<br>

## 3. Key Workflows

<br>

**Adding an Expense**

1. User selects "Add Expense"
2. CLI prompts for:
   - Amount (validated as positive number)
   - Category (selected from numbered list)
   - Description (optional)

3. *ExpenseManager* creates expense object with:

![Expense manager](../personal-expense-tracker/flowchart_5.png)

4. *DataHandler* appends to *expenses.json*

**Viewing Expenses**

1. User selects "View All"
2. System:
   - Loads data from JSON
   - Formats as table:

   ![Viewing expenses](../personal-expense-tracker/flowchart_6.png)

   &nbsp;&nbsp;&nbsp;&nbsp;∘ Displays total at bottom

**Generating Reports**

1. User selects "Spending Summary"
2. ExpenseManager:
   - Groups expenses by category
   - Calculates totals/percentages
3. Output:

![Generating reports](../personal-expense-tracker/flowchart_7.png)

<br>

## 4. Error Handling

<br>

- **Common Scenarios:**

| Error Type  | Handling    |
| ----------- | ----------- |
| Invalid Amount | Retry prompt |
| File Corruption | Auto-reset JSON |
| Missing Data | Default values |

- **Recovery Flow:**

![Recovery flow](../personal-expense-tracker/flowchart_8.png)

<br>

## 5. Data Flow Example

<br>

**Scenario:** User adds a $20 "Transport" expense

1. *main.py* → Collects input
2. *ExpenseManager* → Validates amount/category
3. *DataHandler* → Saves to JSON:

![Scenario](../personal-expense-tracker/flowchart_9.png)

<br>

## **Screenshots** 📷

<br>

**MAIN SCREEN**

![Main screen](../personal-expense-tracker/ss_main.png)

<br>

**NEW EXPENSE ADDED**

![New expense](../personal-expense-tracker/ss_new_expense_added.png)

<br>

**CATEGORIES**

![Categories](../personal-expense-tracker/ss_categories.png)

<br>

**SPENDING SUMMARY**

![Summary](../personal-expense-tracker/ss_spending_summary.png)

<br>

**TOTAL SPENDING**

![Total](../personal-expense-tracker/ss_total_spending.png)

<br>

**EXIT**

![Exit](../personal-expense-tracker/ss_exit.png)

<br>

## **Technical Details** 🧩
- Language: Python 3.9+
- Data Storage: JSON file format (expenses.json)
- Architecture: Modular design with separation of concerns
- Error Handling: Comprehensive input validation and error messages

<br>

## **Development & Best Practices** 📝
- Follows PEP 8 code formatting
- Uses type hints for better code documentation
- Modular design with clear separation of concerns
- Comprehensive error handling and input validation
- Clear function and variable names

<br>

## **Data Architecture** 🗂️
- **main.py:** App interface, user menu, input/output
- **expense_manager.py:** Business logic, data validation, calculations
- **data_handler.py:** File operations, JSON handling, error management
- **expenses.json:** Persistent data storage

<br>

## **Error Handling Strategy** 🛡️
- **Input Validation:** Ensures valid amounts, categories, and menu choices
- **File Operations:** Handles missing/corrupt files gracefully
- **System Errors:** Graceful exit on keyboard interrupt or unexpected exceptions

<br>

## **Development Workflow** 🧑‍💻
1. **Local Development:** Setup, code, test, validate
2. **Version Control:** Git for tracking changes, GitHub for remote backup
3. **Deployment:** Heroku for cloud execution

<br>

## **Learning Outcomes** 📚 
- Implements algorithms for data management and calculations
- Combines file handling, data processing, and user interface
- Uses functions, classes, loops, conditionals, lists, and dictionaries
- Comprehensive README explains program functionality
- Includes error handling and input validation
- Uses JSON for data persistence
- Complete data model for expense management
- Uses Git and GitHub for version control
- Deploys to Heroku cloud platform

<br>

## **License** 📢
This project is for educational purposes.

<br>

## **Acknowledgement**

This is a Python-based command-line project optimized for desktop environments. While it may work on mobile terminals, it is best experienced on a PC or laptop.













import mysql.connector
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Database connection
connection = mysql.connector.connect(
    host=os.getenv('DB_HOST', 'localhost'),
    user=os.getenv('DB_USER', 'root'),
    password=os.getenv('DB_PASSWORD', ''),
    database=os.getenv('DB_NAME', 'finance_db')
)

cursor = connection.cursor()

# Update category names
updates = [
    # Replace / with or
    ('Salary or Wages', 'Salary/Wages'),
    ('Bonuses or Commissions', 'Bonuses/Commissions'),
    ('Pension or Retirement Funds', 'Pension/Retirement Funds'),
    
    # Replace & with and
    ('Food and Groceries', 'Food & Groceries'),
    ('Personal and Household', 'Personal & Household'),
    ('Entertainment and Leisure', 'Entertainment & Leisure'),
    ('Debt and Financial Obligations', 'Debt & Financial Obligations'),
    ('Savings and Investments', 'Savings & Investments')
]

for new_name, old_name in updates:
    cursor.execute("UPDATE categories SET name = %s WHERE name = %s", (new_name, old_name))
    print(f"Updated '{old_name}' to '{new_name}'")

connection.commit()
cursor.close()
connection.close() 
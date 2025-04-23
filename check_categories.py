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

cursor = connection.cursor(dictionary=True)

# Get all categories
cursor.execute("SELECT name FROM categories ORDER BY name")
categories = cursor.fetchall()

print("\nCurrent Categories in Database:")
print("------------------------------")
for category in categories:
    print(category['name'])

cursor.close()
connection.close() 
# Simple program for company registration

import sqlite3

# Create a database connection and cursor
connection = sqlite3.connect("company_registrations.db")
cursor = connection.cursor()


def create_table():
  # Create a table to store registered companies if it doesn't exist yet
  cursor.execute('''CREATE TABLE IF NOT EXISTS registrations (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        full_name TEXT NOT NULL,
                        email TEX NOT NULL,
                        company_name TEXT NOT NULL,
                        company_type INTEGER NOT NULL,
                        price INTEGER NOT NULL
                    )''')


def register_company():
  print("Company Registration")
  full_name = input("Full Name: ")
  email = input("Email: ")
  company_name = input("Company Name: ")

  # Inside the register_company() function, after processing the user input:
  company_name_lower = company_name.lower()

  # Check if the company name is already registered in the database
  cursor.execute('''SELECT company_name FROM registrations''')
  registered_companies_lower = [name[0].lower() for name in cursor.fetchall()]
  if company_name_lower in registered_companies_lower:
    print("Sorry, the company name '{}' is already registered.".format(
        company_name))
    return

  print("Type of Company:")
  print("1 - X Corporation ($1000)")
  print("2 - LLC ($500)")
  print("3 - Pte. Ltd. ($500)")
  print("4 - Trust ($500)")
  print("5 - DAO ($500)")

  while True:
    try:
      company_type = int(input("Select a company type (1-5): "))
      if company_type in [1, 2, 3, 4, 5]:
        break
      else:
        print("Invalid input. Please select 1-5.")
    except ValueError:
      print("Invalid input. Please enter a number.")

  if company_type == 1:
    company_type_name = "Inc."
    price = 1000
  elif company_type == 2:
    company_type_name = "LLC"
    price = 500
  elif company_type == 3:
    company_type_name = "Pte. Ltd."
    price = 500
  elif company_type == 4:
    company_type_name = "Trust"
    price = 500
  else:
    company_type_name = "DAO"
    price = 500

  print(
      "\nThank you, we have registered {} {} on our corporate ledger.".format(
          company_name, company_type_name))
  print("Total registration cost: ${}".format(price))

  # Insert the company name (converted to lowercase) into the database
  cursor.execute(
      '''INSERT INTO registrations (full_name, email, company_name, company_type, price)
                      VALUES (?, ?, ?, ?, ?)''',
      (full_name, email, company_name_lower, company_type_name, price))


if __name__ == "__main__":
  create_table()

  # Main loop for company registration
  while True:
    # Run the company registration function
    register_company()

    # Commit the changes after each registration
    connection.commit()

    # Ask the user if they want to register another company
    another_registration = input(
        "Do you want to register another company? (yes/no): ")
    if another_registration.lower() != "yes":
      break

  # Close the database connection after all registrations are done
  connection.close()

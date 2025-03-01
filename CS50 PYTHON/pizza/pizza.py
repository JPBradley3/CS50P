import sys
import csv
from tabulate import tabulate

def main():
    # Ensure exactly one argument is passed
    if len(sys.argv) != 2:
        sys.exit("Usage: python script.py filename.csv")

    menu_file = sys.argv[1]

    # Ensure the file is a CSV
    if not menu_file.endswith('.csv'):
        sys.exit("Error: File must be a CSV.")

    # Try to open and read the CSV file
    try:
        print_csv_as_menu(menu_file)
    except FileNotFoundError:
        sys.exit("Error: File not found.")
    except Exception as e:
        sys.exit(f"Error: {e}")

def print_csv_as_menu(menu):
    with open(menu, 'r') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        data = list(reader)
    # Use print here directly as tabulate returns a formatted string
    print(tabulate(data, headers=header, tablefmt='grid'))

main()

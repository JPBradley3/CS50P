## provide two command line arguments sys.arg[1] sys.arg[2]
import sys
import csv

def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python script.py filename.csv")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Ensure the file is a CSV
    if not input_file.endswith('.csv'):
        sys.exit("Error: File must be a CSV.")

    # Try to open and read the CSV file
    try:
        convert_table(input_file, output_file)
    except FileNotFoundError:
        sys.exit("Error: File not found.")
    except Exception as e:
        sys.exit(f"Error: {e}")

def convert_table(input, output):
        try:
            with open(input) as input:
                reader = csv.DictReader(input)
                with open(output, "w") as output:
                    header = ["first", "last", "house"]
                    writer = csv.DictWriter(output, fieldnames = header)
                    writer.writeheader()
                    for student in reader:
                        last, first = student["name"].split(", ")
                        house = student["house"]
                        writer.writerow({"first": first, "last": last, "house": house})
        except FileNotFoundError:
            sys.exit(f"Could not read {input}")





## split original csv into three fields a line instead of two to address the next requirement...



main()



## puts the new data into the new csv

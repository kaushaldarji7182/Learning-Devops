
# Create a program that reads a large CSV file and processes its data.

import csv

def process_large_csv(file_path):
    """Reads a large CSV file and processes its data row by row."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            header = next(reader)  # Read the header row
            print(f"CSV Columns: {header}")

            total_rows = 0
            column_sum = 0  # Example: Sum values in the second column (if numeric)

            for row in reader:
                total_rows += 1
                if len(row) > 1 and row[1].isdigit():  # Process second column if numeric
                    column_sum += int(row[1])

            print(f"Total Rows Processed: {total_rows}")
            print(f"Sum of Column 2: {column_sum}")

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    file_path = "C:\\Users\\Administrator\\Python\\ASSIGNMENTS\\industry.csv"  # Change to your CSV file path
    process_large_csv(file_path)

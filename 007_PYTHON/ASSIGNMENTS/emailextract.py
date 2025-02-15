# Implement a regular expression to search for email addresses in a text file.

import re

def extract_emails(file_path):
    """Extracts and prints all email addresses from a text file."""
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'  # Regex for emails
    
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            emails = re.findall(email_pattern, content)  # Find all matches

            if emails:
                print("Emails found:")
                for email in set(emails):  # Remove duplicates
                    print(email)
            else:
                print("No emails found in the file.")

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    file_path = "C:\\Users\\Administrator\\Python\\ASSIGNMENTS\\email.txt"  # Change to your text file path
    extract_emails(file_path)

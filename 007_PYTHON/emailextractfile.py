import re

# Function to extract emails from a file
def extract_emails_from_file(file_path):
    # Regular expression pattern for matching email addresses
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    

    # Open the file and read the content
    try:
        with open(file_path, 'r') as file:
            file_content = file.read()

        # Find all emails using the regular expression
        emails = re.findall(email_pattern, file_content)

        # Return the list of emails found
        return emails
    except FileNotFoundError:
        print(f"Error: The file at '{file_path}' was not found.")
        return []

# Take file path as input from the user
file_path = input("Enter the path of the text file: ")

# Extract emails from the file
emails = extract_emails_from_file(file_path)

# Print the extracted emails
if emails:
    print("Extracted emails:", emails)
else:
    print("No emails found or an error occurred.")

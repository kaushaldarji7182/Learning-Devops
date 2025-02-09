
min_passing_marks = 35
subjects = ["Math", "Science", "English", "History", "Geography"]

for subject in subjects:
    marks = int(input(f"Enter marks for {subject} (out of 100): "))
    
    # Determine grade based on marks
    if marks >= 80 and marks <= 100:
        print(f"You're passed with Grade A in {subject}.")
    elif marks >= 50 and marks < 80:
        print(f"You're passed with Grade B in {subject}.")
    elif marks >= 35 and marks < 50:
        print(f"You're passed with Grade C in {subject}.")
    elif marks < 35:
        print(f"You're failed in {subject}.")

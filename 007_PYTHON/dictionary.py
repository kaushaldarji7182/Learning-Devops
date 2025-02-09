# person = {
#     "name": "John Doe",
#     "age": 30,
#     "gender": "Male",
#     "email": "john.doe@example.com",
#     "address": {
#         "street": "123 Main St",
#         "city": "Anytown",
#         "state": "Anystate",
#         "zip": "12345"
#     },
#     "skills": {
#         "backend_skills": ["node.js", "ruby"],
#         "databases": ["node", "mysql", "spring"]
#     }
# }

# print(person)
# print(len(person))
# print(person.get("address").get("street"))
# print(person.get("skills").get("backend_skills"))
# print ("address" in person)
# print(person.pop("address"))
# print(len(person))
# del person["name"]
# print(len(person))
# print(person["skills"]["backend_skills"])
# person["skills"]["databases"].append("mongo")
# print(person["skills"]["databases"])
# print(person.items())

# person_cp=person.copy()
# del person
# print(person_cp)
# # print(person)

# print(person_cp.keys())

# keys=person_cp.keys()

# for i in keys:
#     print(person_cp[i])
#     print("\n")

# num= int(input("please enter a number"))
# if num>10:
#     print ("no is gt than 10")

# elif num<10:
#     print ("no is less than 10")
# else:
#     print ("no is out of range")



# num = int(input("Enter a number to generate its multiplication table: "))
# # Set the initial value for the counter
# i = 1
# while i <= 10:
#     print(f"{num} x {i} = {num * i}")
#     i += 1
# else:
#     print("printing done")




# # Example using the pass keyword in a for loop
# for i in range(5):
#     if i == 3:
#         pass  # Do nothing when i is 3
#     else:
#         print(i)



# for i in range(6):
#     if i == 1:
#         pass  # Do nothing when i is 1
#     elif i == 2:
#         continue  # Skip the rest of the loop when i is 2
#     elif i == 3:
#         break  # Exit the loop entirely when i is 4
#     elif i == 5:
#         raise ValueError("I reached 3!")  # Raise an error when i is 3
#     else:
#         print(f"Processing number: {i}")

# Using pass to leave a placeholder for future code
# for i in range(1, 6):
#     if i == 3:
#         # pass does nothing but keeps the loop going
#         print("Skipping logic for i =", i)
#         pass  # Placeholder for future code
#     else:
#         print(f"Processing number {i}")


# # Using continue to skip over specific items
# for i in range(1, 6):
#     if i == 4:
#         # Skips the current iteration when i is 4
#         print("Skipping number 4")
#         continue
#     print(f"Processing number {i}")


# # Using break to exit the loop
# for i in range(1, 6):
#     if i == 3:
#         # Exits the loop when i is 3
#         print("Breaking the loop at i =", i)
#         break
#     print(f"Processing number {i}")


# # Using raise to raise an exception when a condition is met
# for i in range(1, 6):
#     if i == 2:
#         # Raises an exception when i is 2
#         print(f"Raising error when i = {i}")
#         raise ValueError("Something went wrong at i = 2")
#     print(f"Processing number {i}")




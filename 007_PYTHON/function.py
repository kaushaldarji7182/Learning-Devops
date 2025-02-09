# def hello_world():
#     print("hello world")

# hello_world()


# def hello_world(message):
#     print(message)

# hello_world("hello world")



# def hello_world(num1,num2):
#     print(num1+num2)

# hello_world(4,5)



# def hello_world(nums):
#     sum=0
#     for i in nums:
#         sum+=i
#     print(sum)

# hello_world([1,2,3,4,5,6,7,8])


# def checkfprime(num):
#     if num <= 1:
#         print("not prime")
#         return  # Negative numbers and 1 are not prime
#     for i in range(2, num//2 + 1):
#         if num % i == 0:
#             print("not prime")
#             return  # Exit the function if a divisor is found
#     print("prime")  # Print once if no divisors were found

# checkfprime(7)  # This will correctly print "prime"



# def first_report(nums):
#     store = set()
#     for i in nums:
#         if i in store:  # If the number is already in the set, it’s the first duplicate
#             return i
#         store.add(i)  # Add the number to the set

# print(first_report([1, 2, 3, 4, 6, 5]))  # Output: None (no duplicates)
# print(first_report([1, 2, 3, 4, 6, 5, 3]))  # Output: 3 (first duplicate)


# def first_report(nums):
#     store = set()
#     for i in nums:
#         if i in args[0]:  # If the number is already in the set, it’s the first duplicate
#             return i
#         store.add(i)  # Add the number to the set

# print(first_report([1, 2, 3, 4, 6, 5]))  # Output: None (no duplicates)
# print(first_report([1, 2, 3, 4, 6, 5, 3]))  # Output: 3 (first duplicate)

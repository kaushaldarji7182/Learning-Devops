

Introduction to Python programming, Why Python?, 
Python Latest Version Installation, 
Run Code in Python Terminal, 
Write Code in a Text Editor,
Practice in IDE (VS Code Setup & Run), 
Work with Numbers, Strings & Variables, 
Conditional Logic (if, elif, else), 
Functions, Loops (while, for), 
Import Libraries, 
Troubleshooting Code, 
Jupyter Notebooks, Handling Exceptions, Object-Oriented Concepts, Using Regular Expressions



Python for DevOps-
	Automating Files & Filesystem (os module, os.path, os.walk), 
  Managing Files/Directories, 
  Regular Expressions for Text Search,
  Handling Large Files, 
  Hashing with Hashlib, 
  Encryption with Cryptography,
  Introduction to Popular Python Libraries (Pandas, Selenium, Requests, Scapy, etc.), 
  Python Virtual Environments, 
  Python Collections (List, Set, Tuple), 
  Unit Testing & Mocking (unittest, mock, pytest, fixtures)
  
  
Install the latest version of Python and verify the installation.
Write a simple Python script that prints "Hello, World!" to the console.
Create a script to perform basic arithmetic operations (addition, subtraction, etc.).
Write a program that uses conditional statements to check if a number is positive or negative.
Define a function that takes a list and returns its sum.
Create a for loop that prints numbers 1 to 10.
Use Jupyter Notebooks to document a Python project with explanations.
Implement error handling using try/except blocks.


Write a script to automate file creation and deletion in a specified directory.
Use the os module to list all files in a directory and display their sizes.
Implement a regular expression to search for email addresses in a text file.
Create a program that reads a large CSV file and processes its data.
Write a hashing script using the hashlib library to secure passwords.
Create a virtual environment, install a package, and save dependencies to requirements.txt.
Implement unit tests for a sample function using the unittest framework.
Mock a function in a unit test to simulate behavior without executing the actual code.



import boto3
def create_ec2_instance():
    try:
        print("creating ec2 instance")
        resource_ec2 = boto3.client("ec2")
        resource_ec2.run_instances(
            ImageId = "ami-085ad6ae776d8f09c",
            MaxCount = 1,
            MinCount = 1,
            InstanceType = "t2.micro",
            KeyName = "first_instance"
        )
    except Exception as e:
        print(e)

create_ec2_instance()

# import datetime
# print (dir(datetime))

from datetime  import datetime
now = datetime.now()
day = now.day
month = now.month
year = now.year
hr = now.hour
mn = now.minute
sc = now.second

print(day,month,year,hr,mn,sc)

try:
    # print(10+50)
    # print(10+'50')
    print(50/0)

except TypeError:
    print("something went wrong")

except ValueError:
    print("something went wrong")

except ZeroDivisionError:
    print("this is zero division error")
    
    
    
def sum_num(x):
    return sum(x)
def higher_orderfunction (f,lis):
    var = f(lis)
    return var
result = higher_orderfunction(sum_num,[1,2,3,4,5])
print(result)


def square(x):
    return x**2
def cube(a):
    return a**3
def absolute(b):
    if b >= 0:
        return b
    else:
        return -(b)
    

def hof(type):
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    else:
        return absolute

res=hof('absolute')
print(res(-5))

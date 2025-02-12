import re
string = "Good morning"
# match = re.match("good", string, re.I)
# if match:
#     print("Match found:", match.group())
# else:
#     print("No match found.")
# match=re.findall("(?i)morning",string)
# print(match)
# match2=re.findall("good morning",string,re.I | re.DOTALL)
# print(match2)
# match3=re.search("good morning",string,re.I | re.DOTALL)
# print(match3)
# myspan=match3.span()
# print(myspan)

# l=[]
# for i in re.finditer(re.escape("good"),string,re.I):
#     l.append(i.span())
#     print(i)
# print(l)

# match5=re.sub("[Gg]ood","awesome",string,re.IGNORECASE)
# print(match5)
# print(string)

# string='''Hi 
# hello 
# welcome'''
# match6=re.split("\n",string)
# print(match6)


pattern = '[K].*'
match7=re.findall(pattern.string)
print(match7)
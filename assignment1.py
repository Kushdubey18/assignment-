# q1...........

name = "Kush"


print("First character:", name[0])
print("Last character:", name[-1])
print("Length of string:", len(name))
print("Uppercase:", name.upper())
print("Lowercase:", name.lower())
print("Reversed string:", name[::-1])

# q 2...............


text = "PythonProgramming"
print("First four characters:", text[:4])
print("Characters from index 2 to 5:", text[2:6])
print("Reverse string:", text[::-1])



#  q3..........

numbers = [10, 20, 30, 40, 20]

numbers.append(50)
print("After append(50):", numbers)
numbers.insert(2, 25)   
print("After insert(2, 25):", numbers)
numbers.remove(20)      
print("After remove(20):", numbers)
numbers.pop()
print("After pop():", numbers)
numbers.reverse()
print("After reverse():", numbers)
numbers.sort()
print("After sort():", numbers)
print("Length of the list:", len(numbers))
print("Occurrence of 20:", numbers.count(20))


# q4.............

tpl=(1,2,2,4)
print(len(tpl))
print(tpl[0])
print(tpl[-1])
print(tpl[0:4])
print(max(tpl))
print(min(tpl))
print(sum(tpl))

#q5...........

# Tuple Packing and Unpacking

t = (10, 20, 30, 40)   # Packing

a, b, c, d = t         # Unpacking

print(a)
print(b)
print(c)
print(d)


#q6...........


# Student Details Dictionary

student = {
    "Name": "Kush",
    "Age": 20,
    "Course": "B.Tech",
    "Address": "Jaipur"
}

#  all keys
print("Keys:", student.keys())

#  all values
print("Values:", student.values())

#  all items
print("Items:", student.items())

#  Address
student["Address"] = "Patna"

# Add new key Branch
student["Branch"] = "CSE"

print("\nUpdated Dictionary:")
print(student)


#q7.............


lst = [1, 2, 3, 4, [2, 5], 7]

print(lst[4][1])

#q8..............


num = int(input("Enter a number: "))

num += 10

print("Updated value:", num)

#q9..........


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Multiplication =", a * b)


#q10..........


student = {
    "Name": "Kush",
    "Age": 20,
    "Course": "B.Tech"
}

print(student.get("Name"))   
print(student.keys())        
print(student.values())      
print(student.items())      


#q11..........


list1 = [10, 20, 30, 40, 50]

list2 = list1.copy()

print("Original List:", list1)
print("Copied List:", list2)












#Q1_01
print(1+2+3+4+5)
#Q2_01
n = 1
s = 0
while n <= 100:
    s = s + n
    n = n + 2
print(s)
#Q2_02
num = int(input("Enter a positive integer: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number") 
#Q3_01
print('*' * 5)
print('# ' * 5)
#Q4_01
name = "John Doe"
address = "123 Main Street"
print(name)
print(address)
#Q5_01
x=1
y=0
print(x and y)
print(x or y)
print(not x)
print(not y)
#Q6_01
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a < b:
    print(a, b)
else:
    print(b, a)
#Q7_01
adult = int(input("Are you an adult? (1 if you are an adult, 0 if you are minor): "))
married = int(input("Are you married? (1 if you are married, 0 if you are single): "))

if adult == 1 and married == 1:
    print("You are an adult who is married.")
elif adult == 1 and married == 0:
    print("You are an adult who is single.")
elif adult == 0 and married == 1:
    print("You are a minor who is married.")
else:
    print("You are a minor who is single.")
#Q8_01
for num in range(2, 13):
    is_prime = True
    
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(num, ": Prime number")
    else:
        print(num, ": Composite number")
#Q9_01
for num in range(100, 1000):
    a = num // 100
    b = (num // 10) % 10
    c = num % 10
    
    if num == a**3 + b**3 + c**3:
        print(num)
#Q10_01
l1 = ['I like', 'I love']
l2 = [' pancake.', ' kiwi juice.', ' espresso.']

for i in l1:
    for j in l2:
        print(i + j)
#Q11_01
person = {'Name': 'David Doe', 'Age': 26, 'Weight': 82, 'Job': 'Data scientist'}

person['Father'] = 'John Doe'

print(person)
#Q12_02
lst = [5, 6, 3, 9, 2, 12, 3, 8, 7]


max_index = 0
for i in range(len(lst)):
    if lst[i] > lst[max_index]:
        max_index = i


lst[max_index], lst[-1] = lst[-1], lst[max_index]

print(lst)
#Q13_01
arr = [[1, 2], [3, 4], [5, 6]]

new_arr = []

for sub in arr:
    for num in sub:
        new_arr.append(num)

print(new_arr)
#Q14_01
maria = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}

average = sum(maria.values()) / len(maria)

print(average)
#Q15_01
import copy

school = {
    'kim': {'age': 16, 'hei': 170, 'grade': 3},
    'lee': {'age': 15, 'hei': 168, 'grade': 2},
    'choi': {'age': 14, 'hei': 173, 'grade': 1}
}

school2 = copy.deepcopy(school)

print(school is school2)
#Q16_01
scores = (('Hyun', 88, 95, 90),
          ('Kang', 85, 90, 95),
          ('Park', 70, 90, 80),
          ('Hong', 90, 90, 95))


names, english, math, science = zip(*scores)


average = sum(math) / len(math)

print(average)                               
                               
                               

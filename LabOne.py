# Q2 

name = 'Youssef Alaa Youssef'
count = 0
for x in name:

    if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
        count += 1
print(count)

# Q4 

name = 'Youssef iti Alaa iti Youssef'
x = name.count("iti")
print(x)

# Q5 

name = 'Youssef Alaa Youssef'
for x in name:
    if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
        name = name.replace(x, "")
print(name)

# Q6 
name = 'Youssefi Alaia Youssef'

for x in range(len(name)):
    if name[x] == "i":
        print(x)

# Q8 

star = int(input('Enter the number: '))
for x in range(1, star+1):
    print(" "*(star-x), '*'*x)

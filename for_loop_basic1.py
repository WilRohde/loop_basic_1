# question 1
print("Question 1")
for x in range (0,151):
    print(x)
# question 2
print("Question 2")
for y in range (5,1001,5):
    print(y)
# question 3
print("Question 3")
j = 1
while j <= 100:
    if (j % 10) == 0:
        print("Coding Dojo")
    elif (j % 5) == 0:
        print("Coding")
    else:
        print(f"{j}")
    j = j + 1
# question 4
print("Question 4")
k = 0
sum = 0
while k <= 500000:
    if (k % 2) != 0:
        #print(f"{sum} + {k}")
        sum = sum + k
    k = k + 1
print(str(sum))
# Question 5
print("Question 5")
t = 2018
for t in range(2018,0,-4):
    print(str(t))
# Question 6
print("Question 6")
lowNum = 0
highNum = 3270
mult = 7
for n in range(lowNum,(highNum + 1)):
    if (n % mult) == 0:
        print(str(n))
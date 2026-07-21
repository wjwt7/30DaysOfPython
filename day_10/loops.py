#Exercise level 1
#1
for i in range(11):
    print(i)
#2
for i in range(10, -1, -1):
    print(i)
#3
hashtag = "#"
for i in range(1, 8):
    print(hashtag * i)
#4
for i in range(8):
    for j in range(8):
        print("#", end=" ")
    print()
#5
for i in range(11):
    print(f"{i} x {i} = {i * i}")
#6
program = ["Python", "Numpy", "Pandas", "Django", "Flask"]
for item in program:
    print(item)
#7
for i in range(101):
    if i % 2 == 0:
        print(i)
#8
for i in range(101):
    if i % 2 != 0:
        print(i)

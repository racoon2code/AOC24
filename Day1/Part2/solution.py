data = open("input.txt", "r")


list1 = []
list2 = []

for line in data:
    #modified_string = ''.join('*' if not char.isdecimal() else char for char in line)
    line = line.split()
    
    list1.append(int(line[0]))
    list2.append(int(line[1]))


list1.sort()
list2.sort()

result = 0

for i in list1:
    i2 = list2.count(i)
    if i2 > 0:
        temp = i * i2
        result += temp

print(result)  


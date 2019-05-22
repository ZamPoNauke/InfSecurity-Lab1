#f = open('User_Info.txt', 'r')

#i = 0
#a = []
#b = []
#for line in f:
#    for
#    b.clear()
#    b.append(line)
#    a.append(b)
#    
#print(a)

data = []
with open("User_Info.txt") as f:
    for line in f:
        data.append([str(x) for x in line.split()])

for i in data:
    if i[0] == 'ADMIN': print('OK!')
    print(i[0])    


    
print(data)
print()
print(data[0])
print()
print(data[0][0])
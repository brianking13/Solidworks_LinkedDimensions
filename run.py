import time
import sys



# open file
file = open('equations.txt','r')
content = file.read().splitlines()
file.close()

for x in range(0,len(content)):
    content[x] = content[x].replace('ï»¿', "")
print(content)


# select variable/value pair to change
variable = input("Which variable would you like to update? ")
value = input("New {} value (inches): ".format(variable))
count = 0

for x in range(0,len(content)):
    content[x] = content[x].split(" = ")
    if variable == content[x][0].replace('"', ""):
        content[x][1] = value
    else:
        count += 1
if count == len(content):   # terminate program if variable not found
    print("error: variable not found")
    time.sleep(3)
    sys.exit()




# turn new variable back into Solidworks readable format
for x in range(0,len(content)):
    content[x] = " = ".join([content[x][0],content[x][1]])

file = open('equations.txt','w')
content = "\n".join(content)
file.write(content)
file.close()
time.sleep(.5)
print('update successful; rebuild document to see changes')
time.sleep(3)

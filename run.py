import time

# file = open('equations.txt','r')
# content = file.readlines()
# file.close()

variable = input("Which variable would you like to update? ")
input = input("New {} value (inches): ".format(variable))

file = open('equations.txt','w')
file.write('"{}"= {}'.format(variable, input))
file.close()

time.sleep(.5)
print('update successful; rebuild document to see changes')
time.sleep(3)

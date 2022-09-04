from functions import get_ip
import os


list = []

while  :
    command = input("Insert a Command >>")
    if command == "exit":
        break
    list.append(command)
print(list)

for n in list:
    output = os.popen(n).read()
    print(output)


print(get_ip())


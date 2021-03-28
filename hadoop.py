import os
print("Hadoop")
print("Press 1: for launch Master node")
print("Press 2: for launch Data node")
while True:
    x = int(input("Press number"))
    if x == 1:
        os.system("ansible-playbook {}".format("master.yml"))
    elif x == 2:
        os.system("ansible-playbook {}".format("data.yml"))

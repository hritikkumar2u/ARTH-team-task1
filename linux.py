import os
print("\t\t\t\t\t\t Basic linux command")
print("\t\t\t\t\t\t ---------------------")
print("Press 1:  To show date")
print("Press 2:  To show calendar")
print("Press 3:  To show the ip address of the os")
print("Press 4:  To show the details of CPU")
print("Press 5:  To make a folder in linux")
print("Press 6:  To check how many disk are added")
print("Press 7:  To check drive size")
print("Press 8:  To know how many ports are running in os")
while True:
   x = int(input("Press number:"))
   if x == 1:
       os.system("date")
   elif x == 2:
       os.system("cal")
   elif x == 3:
       os.system("ifconfig")
   elif x == 4:
       os.system("lscpu")
   elif x == 5:
       os.system("mkdir {}".format("/xyz"))
   elif x == 6:
       os.system("fdisk {}".format("-l"))
   elif x == 7:
       os.system("df {}".format("-h"))
   elif x == 8:
       os.system("netstat {}".format("-tnlp"))
   elif x == 9:
       break

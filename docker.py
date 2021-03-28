import os
print("\t\t\t\t\t Docker")
print("\t\t\t\t\t ------")
print("Press 1:  To launch new docker container")
print("Press 2:  To know the present docker images in the os")
print("Press 3:  To check how many docker os exist")
print("Press 4:  To start docker os")
print("Press 5:  To delete docker os")
while True:
	x=int(input("Press number:"))
	if x == 1:
		os.system("docker {} {} {} {} {}".format("run","-it","--name","web1","centos:latest"))
	elif x == 2:
		os.system("docker {}".format("images"))
	elif x == 3:
		os.system("docker {} {}".format("ps","-a"))
	elif x == 4:
		os.system("docker {} {}".format("start","web1"))
	elif x == 5:
		os.system("docker {} {} {}".format("rm","-f","web1"))
	elif x == 6:
		break

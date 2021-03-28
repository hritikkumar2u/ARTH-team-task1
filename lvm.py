import os
print("\t\t\t\t LVM AUTOMATION")
print("\t\t\t\t --------------")
print("Press 1: To check present disk")
print("Press 2: To create physical volumes of disk 1")
print("Press 3: To create physical volumes of disk 2")
print("Press 4: To create volume group")
print("Press 5: To create a logical volume of 25GB out of 30GB")
print("Press 6: To display the created volume group of 25GB")
while True:
	x=int(input("Press number: "))
	if x == 1:
		os.system("fdisk -l")
	elif x == 2:
		os.system("pvcreate {}".format("/dev/sdb"))
	elif x == 3:
		os.system("pvcreate {}".format("/dev/sdc"))
	elif x == 4:
		os.system("vgcreate {} {} {}".format("myvg1","/dev/sdb","/dev/sdc"))
	elif x == 5:
		os.system("lvcreate --size {} {} {}   {}".format("25G","--name","mylv1","myvg1"))
	elif x == 6:
		os.system("vgdisplay")
    

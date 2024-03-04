# Author:Keshav Ghimire
"""a python script that will prompt the user for the path to an interface file. If the file exists, 
it will be modified to make the interface obtain its address through DHCP.  
If the file does not exist, it will inform use, gracefully handle any errors it may encounter in this process."""
import os
# asking for sudo privilige
currentuser = os.popen('whoami')
if currentuser.read().strip() != 'root':
    print("You must be root")
    exit()

else:

        interface=input("Please enter the name of an interface: ")
        try:
                f = open('/etc/sysconfig/network-scripts/ifcfg-'+interface, 'r') #Editing interface configuration file
                if True:
                        f = open('/etc/sysconfig/network-scripts/ifcfg-' + interface, 'w')
                        MAC = str(os.system("more /sys/class/net/" + interface + "/address"))
                        print("Changing interface into DHCP")
                        f.write("DEVICE=" + interface + "\n")
                        f.write("ONBOOT=yes\n")
                        f.write("HWADDR=" + MAC + "\n")
                        f.write("BOOTPROTO=DHCP\n")
                        f.write("NM_CONTROLLED=yes\n")
                        f.write("IPV6INIT=no\n")
                        f.close()
                else:
                        exit()


        except:                                 #Handling errors
                print("Interface doesnot Exist!!")
                exit(2)



import optparse  

parse_object = optparse.OptionParser()  
parse_object.add_option("-i","--interface", dest="interface", help="interface to changer")   
parse_object.add_option("-m","--mac",dest="mac_address",help="new mac address")

print(parse_object.parse_args())  
print("MyMacChanger started!")

python MacChangerAdress.py(sample file name) -i eth0 -m 00:00:00:00:00:00 (example)

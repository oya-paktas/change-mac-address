import subprocess

print("MyMacChanger started!")

subprocess.call(["ifconfig","eth0","down"])
subprocess.call(["ifconfig","eth0","hw","ether","00:00:00:00:00:00"])
subprocess.call(["ifconfig","eth0","up"])
İfconfig (Has the Mac Address Changed?)

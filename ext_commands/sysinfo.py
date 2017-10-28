import os, sys, getpass, platform

print("OS Name: " + os.name)
print("System Platform: " + sys.platform)
print("System Executable: " + sys.executable)
print("Python Version: " + sys.version)
print("Current User: "+ getpass.getuser())
print("Platform Architecture: " + platform.machine())
print("Operating System: " + platform.platform())
print("Processor Info: " + platform.processor())

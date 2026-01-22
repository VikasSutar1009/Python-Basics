import platform

def system_info():
    print("OS: ", platform.system())
    print("Processor:", platform.processor())

system_info()
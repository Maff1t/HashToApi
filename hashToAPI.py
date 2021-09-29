import csv
import sys
import inspect
from IHashingFunc import IHashingFunc
import importlib


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print (f"Usage: {sys.argv[0]} path_to_hashing_func.py hash_result\n",
                f"Example: {sys.argv[0]} hashingFunctions.BlackEnergy 0x58FE7AA8)")
        exit(1)
    dlls = [] # Use it if you want to search faster in only few dlls!

    # Read CSV containing API Dataset
    reader = csv.DictReader (open("WindowsAPI.csv", "r"))
    
    #Init class relative to hashing function
    module = importlib.import_module(sys.argv[1])
    hashingClass = None
    for name, obj in inspect.getmembers(module, inspect.isclass):
        if not inspect.isabstract(obj) and isinstance(obj(), IHashingFunc):
            hashingClass = obj()
            break
    
    if hashingClass == None:
        print ("Error retrieving class from specified module")
        exit(1)


    apiCounter = 0
    for row in reader:
        if not len(dlls) or row["dllName"] in dlls:
            apiName = row["apiName"].replace("b'", "").replace("'", "")
            apiHash = hashingClass.hashString(apiName)
            apiCounter += 1
            if apiHash == int(sys.argv[2], 16):
                print (f"API Found: {apiName}")
                exit(0)
    
    print (f"Hash not found, tried {apiCounter} APIs")
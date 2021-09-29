# This script parse the exported functions from all dlls inside System32 and SysWOW64
# And build a windows APIs dataaset that is needed to find the hashes


import os
import csv
import pefile

dllPaths = ["C:\\Windows\\System32\\", "C:\\Windows\\SysWOW64\\"]


rows = []
for dir in dllPaths:
    dlls = [f for f in os.listdir(dir) if f.lower().endswith("dll")]
    print (dlls)
    for dll in dlls:
        try:
            print (f"Elaborating {dll}")
            dllPath = os.path.join(dir, dll)
            pe =  pefile.PE(dllPath)
            for exp in pe.DIRECTORY_ENTRY_EXPORT.symbols:
                rows.append({
                    "dllPath" : dllPath,
                    "dllName" : dll,
                    "apiName" : exp.name,
                    "apiOrdinal" : exp.ordinal
                })
        except:
            print (f"Error in {dll}")

writer = csv.DictWriter (open("WindowsAPI.csv", "w+"), fieldnames=rows[0].keys())
writer.writeheader()
writer.writerows(rows)
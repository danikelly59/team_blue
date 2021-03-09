"""
CSE 5408
"""

import datetime

def convert_to_24(stra):
    if (stra[-2:] == "AM" and stra[:2] == "12"):
        return "00" + stra[2:-2]
    elif (stra[-2:] == "AM"):
        return stra[:-2]
    elif (stra[-2:] == "PM" and stra[:2] == "12"):
        return stra[:-2]
    else:
        return str(int(stra[:2]) + 12) + stra[2:8]
    
dt =datetime.datetime.now()
print("Conversion of time : ", convert_to_24(dt.strftime("%H:%M:%S")))
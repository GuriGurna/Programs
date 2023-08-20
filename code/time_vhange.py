# TODO
# [] - Break with colon
# [] - Check AM or PM from last index
# [] - if PM then plus hours (first index) with 12
# [] - Remove AM or PM from seconds (last index)
# [] - Join and return

def timeConversion(s):
    # Write your code here
    words = s.split(":")
    x = list(words[2])

    hours = words[0]
    gu = int(hours)
    if x[2] == "P":
        a = gu+12
    x[2]=""
    x[3]="" 
    "".join(x)   
    "".join(words)
        
        
    print(words)
    #if "PM" in words[2]:
    #    print(words)
    #else:
    #    print("no")
    

   
timeConversion("07:05:45AM")
timeConversion("07:05:45PM")
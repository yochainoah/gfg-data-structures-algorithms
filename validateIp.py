

def valIpAddress(ip):
    ## we assume the ip is of type string 
    ## because its a string its minimum length cna be 7
    n = len(ip)
    if n < 7:
        return False
    ## define an array to store the 4 sections of the ip address
    four_sections = ip.split('.')
    if len(four_sections) > 4:
        return False
    ## define a loop and traverse through the array
    for section in four_sections:

         if not section.isdigit():
             return False
         
         if int(section) > 1 and section[0] == '0':
             return False

         if len(section) > 3:
             return False

         if int(section) < 0 or int(section) > 255:
             return False

    return True

s1 = "128.0.0.1"
s2 = "125.16.100.1"
s3 = "125.512.100.1"
s4 = "125.512.100.abc"

print("Valid" if valIpAddress(s1) else "Not valid")
print("Valid" if valIpAddress(s2) else "Not valid")
print("Valid" if valIpAddress(s3) else "Not valid")
print("Valid" if valIpAddress(s4) else "Not valid")  
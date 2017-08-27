#Programs to display all binary strings of n-bits

#function to append digits
def appendtofront(x,l):
    return [x + i for i in l]

#Function to select and return strings
def bitstring(n):
    if n==0:return []
    if n==1:return ["0","1"]
    else:
        return ( appendtofront("0" , bitstring(n-1)) + appendtofront("1", bitstring(n-1)))

print(bitstring(3))
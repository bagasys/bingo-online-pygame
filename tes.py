# Function to convert   
def listToString(s):  
    str1 = " " 
    return (str1.join(s)) 
        
        
# Driver code     
s = ['Geeks', 'for', 'Geeks'] 
print(listToString(s))  

halo = [['ulala'],4,2,3,7]
hai = listToString(halo[0])
if hai == 'ulala':
    print(hai)
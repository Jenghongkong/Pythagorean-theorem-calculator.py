import math
print("a^2 + b^2 = c^2")
choose = input("Which side[a,b,c] do you want to count ?:")

if(choose == "a"):
    b = int(input("length2: "))
    c = int(input("hypotenuse: "))
    print(math.sqrt(c**2 - b**2))

elif(choose == "b"):
    a = int(input("length1: "))
    c = int(input("htpotenuse: "))
    print(math.sqrt(c**2 - a**2))
    
    

if(choose == "c"):
    a = int(input("length1: "))
    b = int(input("length2: "))
    print(math.sqrt(a**2 + b**2))

else:
    print("Error")

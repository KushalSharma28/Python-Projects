from pkg_resources import add_activation_listener


# Precedence Rule 
# Parenthesis = Highest
# Exponent = Right to Left
# *,/,//,% = Left to Right
# +,- = Left to Right 

print (14+16) #Addition
print (14-18) #Subtraction
print (14*16) #Multiplication
print (14/16) #Float Division
print (14//16) #Integer Division
print (14%16) #Modulus Division
print (14**16) #Exponent
print (round(4*5.6,8))
print (14**18+14-16*14/20%10//4)

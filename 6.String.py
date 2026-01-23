str1="one"
str2='\ttwo'
str3='''\nthree'''
print(str1,str2,str3)
#concatenation
str4="one"
str5="two"
str6=str4+" "+str5
print(str6)
#Length of the string
print (len(str5))
print (len(str6)) #space is counted as length
#Indexing
print(str4[0])
print(str4[2])
#Slicing:Accessing parts of the string.
str7="Faisal naik"
print(str7[0:4])
print(str7[0:])
print(str7[0:len(str7)])
print(str7[:])
print(str7[:len(str7)])
print(str7[-4:-2]) #negative slicing

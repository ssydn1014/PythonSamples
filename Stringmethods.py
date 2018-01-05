str1 = "python number string examples"
str2 ="num"
str3 = "this abc is really a string example ... wow!!!"
str4 = "is"

#find() method
print("find()")
print(str1.find(str2))
print(str1.find(str2,10))
print(str1.find(str2,15,20))

#len() method
print("len()")
print(len(str1))

#index() method
print("index()")
print(str1.index(str2))
print(str1.index(str2, 0))
#print(str1.index(str2,12,len(str1)))



#rfind() method
print("rfind()")
print(str3.rfind(str4))
print(str3.rfind(str4,0 ,10))
print(str3.rfind(str4, 10,0))
print(str3.rfind(str4, 10 , 30))


#rindex() method
print("rindex()")
print(str1.rindex(str2))
print(str1.rindex(str2, 0))
#print(str1.rindex(str2,len(str1),12))


#join() method
print("join()")
joiner = "-"
tittle = "10 20 30 ABC"
strLower = "abc"
print(joiner.join(tittle))


#capatalize() method
print("capatalize()")
abc_string = "welcome to python world"
abc_STRING = "python world"
abc_s = "to python world"
print(abc_STRING.capitalize())
print(abc_string.capitalize())
print(abc_s.capitalize())

#upper_lower() method
print("upper(),lower() methods")
str_5 = "abcDEFghij"
print(str_5.upper())
print(str_5.lower())
print(str_5.isupper())
print(str_5.islower())

#replace() method
str6 = "python is scripting is and is programming is language"
print(str6.replace("is","was"))
print(str6.replace("is","was",3))

#split() method
str7 ="ABC123 ABC123 ABC123"
print(str7.split())
print(str7.split('A'))
print(str7.split('123'))
print(str7.split('ABC'))

#ljust(),rjust methods










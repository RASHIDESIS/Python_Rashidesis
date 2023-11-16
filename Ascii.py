Name = "Mushfiq"


for i in range(len(Name)):
    print(Name[i] )

# char = "a"
# print("the ascii value of ", char,"is" ,ord(char))

character = Name[0]
for j in range(len(Name)):
     print (character , ord(character))
character = character + j

sum = ord(character)
result = ord(Name[0])+ord(Name[1])+ord(Name[2])+ord(Name[3])
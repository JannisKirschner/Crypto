key = []
cyphertext = input("Enter Cyphertext: ")

print(cyphertext)
while(True): 
   let  =  input("Enter letter to substitute: " )
   if(let == "quit"):
       exit()

   sub = input("Enter substitution: " )
   key.append(let + "=" + sub + "; ")
   print(key)
   cyphertext = cyphertext.replace(let,sub + "1")
   cyphershow = cyphertext.replace("1", "")
   print(cyphershow)


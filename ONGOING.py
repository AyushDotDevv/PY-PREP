xyz = ["ayush","amey","lucid", "bilauta"]
print (xyz[2])
print (xyz[0:4])
#modification
xyz.append("tipsy")
xyz.insert(1,"dok")
xyz.remove("amey")
print(xyz)
print(xyz.sort()) 
print(xyz.reverse())
print(len(xyz))

#TUPLES (basically list that cant be edited)
TUP= ("AYUSH", 19 , "BCA")
print(TUP[1])
name , age , degree = TUP
print(name)
print (degree)

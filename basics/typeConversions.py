file = open('/home/shlok/Desktop/Stuff/dsa/python_dsa/data.txt','w')
file.write("Hello World")
file.write("\n")
file.write("This is our new text file")
file.close()

print("file created successfully",file.name)
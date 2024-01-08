"""
Open a file in read mode
and print the content
"""
f = open("somefile.txt","r")
data_s = f.read()
print(data_s)
f.close()

"""
Now write the contents of previously opened file
into 
"""
f2 = open("newfile.txt","a")
f2.write(data_s)
#print(data_s)
f2.close()

"""
Read file via open
"""
print("**********************")
print("Read a file using with")
print("**********************")
with open("newfile.txt") as f3:
    d3 = f3.read(200)
    print(f3.read())
print(d3)
#program to copy contents of one file to another
file1=input("Enter the name of file to copy from")
file2=input("Enter the name of file to copy to")

try:
    #opening first file in read mode
    f1=open(file1,'r')
    #reading content of the file
    content=f1.read()

    #opening second file in write mode
    f2=open(file2,'w')
    #reading content of the file
    f2.write(content)

    print("File copied successfully")

except FileNotFoundError:
    print("File not found")


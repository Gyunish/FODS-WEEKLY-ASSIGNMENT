#program to find and replace
file=input("Enter file name")   #taking user input
find=input("Enter word to find")
replace=input("Enter word to replace")
try:
    fr=open(file,'r')   #opening file in read mode
    content=fr.read()   #reading file contents
    fr.close()

    fw=open(file,'w')
    fw.write(content.replace(find,replace))     #replacing
    fw.close()

except FileNotFoundError:
    print("File not found")


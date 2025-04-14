#program to count characters, lines and word in a file
try:
    #opening file in read mode
    f=open("file.txt",'r')
    #reading content of the file
    content=f.read()

    #couting characters
    char_count=len(content)

    #reseting file pointer to beginning to count lines and words
    f.seek(0)

    #counting lines
    lines=f.readlines()
    line_count=len(lines)

    #couting words by splitting the content by whitespace
    word_count=len(content.split())
    f.close()

except FileNotFoundError:
    print("The file was not found.")

print("Character count=",char_count)
print("Line count=",line_count)
print("Word count",word_count)
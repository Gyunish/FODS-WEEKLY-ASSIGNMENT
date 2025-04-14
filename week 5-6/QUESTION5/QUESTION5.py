import string
file=open('file.txt','r')
text=file.read()
file.close()

words=text.split()
word_count={}

for word in words:
    if word in word_count:
        word_count[word]+=1
    else:
        word_count[word]=1

print("Word Frequency:")
for word,count in sorted(word_count.items()):
    print(word,":",count)
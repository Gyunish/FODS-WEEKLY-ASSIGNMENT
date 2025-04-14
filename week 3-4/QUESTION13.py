#making a function that finds common letters in two words
def word_intersection():
    word1=input("Enter the first word:")    #taking user input
    word2=input("Enter the second word:")

    common_letters=set(word1.lower())&set(word2.lower())      #converting the letters into lowercase and storing it in set and finding intersection
    print("Common letters between the two words:",common_letters)

word_intersection()
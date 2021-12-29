string = input("enter string")
charcterCount = 0
WordCount = 0
for i in string:
    charcterCount=charcterCount+1
    if (i ==' '):
        WordCount=WordCount+1

print("number of words in a string")
print(WordCount)
print("number of charcters in a string")
print(charcterCount)
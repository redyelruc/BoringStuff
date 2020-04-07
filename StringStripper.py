def mysplit(strng):
    strng = strng.lstrip()
    mylist = []
    word = ''
    for character in range(len(strng)):
        if strng[character].isalpha():
            word = word + strng[character]
        else:
            mylist.append(word)
            word = ''
    mylist.append(word)
    return mylist
# put your code here
#

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
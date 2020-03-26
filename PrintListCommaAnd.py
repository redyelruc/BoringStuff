#  Write a function that takes a list value as
#  an argument and returns a string with all
#  the items separated by a comma and a space,
#  with and inserted before the last item.
#  For example, passing the previous spam
#  list to the function would return 'apples,
#  bananas, tofu, and cats'.Write your code here :-)


def latest_function(mylist):
    if len(mylist) == 0:
        print('Sorry, your list is empty.')
    else:
        for x in range(len(mylist)-1):
            print(str(mylist[x]) + ", ", end="")
        print("and " + str(mylist[len(mylist)-1]))


spam = [1,2,3,4]
corned_beef = []
print(len(corned_beef))
latest_function(corned_beef)
latest_function(spam)

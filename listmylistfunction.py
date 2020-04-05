def list(lst):
    del lst[3]
    lst[3] = 'ram'
    return lst

list = ['Mary','had','a','little','lamb']
print(list(list))
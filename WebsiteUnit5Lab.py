def readint(prompt, min, max):
    while True:
        print(prompt)
        try:
            val = int(input())
            if val < -10 or val >10:
                print('That is outside of the specified range.')
                continue
            return val
            break
        except ValueError:
            print('That is not a number')
            continue

v = readint("Enter a number from -10 to 10: ", -10, 10)
print("The number is:", v)
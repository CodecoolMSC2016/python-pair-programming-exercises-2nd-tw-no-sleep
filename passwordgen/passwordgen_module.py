import string
import random


def passwordgen():
    lowerCaseChar = string.ascii_lowercase[:26]
    upperCaseChar = string.ascii_uppercase[:26]
    num = string.digits[:10]
    specChar = "!@#$%^&*()?"
    theList = [lowerCaseChar, upperCaseChar, num, specChar]
    pw = ""
    for i in range(0, 3):
        for b in theList:
            randChar = random.randint(0, len(b) - 1)
            randPw = random.randint(0, len(pw))
            pw += b[randChar]
    print(pw)
    return pw


def main():
    return


if __name__ == '__main__':
    main()

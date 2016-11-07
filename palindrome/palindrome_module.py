def palindrome(str):

    str = str.replace(" ", "")
    str = str.upper()
    str2 = str[::-1]
    if str == str2:
        return True
    else:
        return False

def main():
    return


if __name__ == '__main__':
    main()

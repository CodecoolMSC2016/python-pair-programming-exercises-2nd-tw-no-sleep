import datetime


def years(age):
    year = datetime.date.today().year
    years_left=(year - age) + 100
    
    return years_left

def main():
    return


if __name__ == '__main__':
    main()

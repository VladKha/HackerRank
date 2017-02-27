if __name__ == '__main__':
    year = int(input())
    if year == 1918:
        daysInFebruary = 28 - 13
    elif year < 1918:
        if year % 4 == 0:
            daysInFebruary = 29
        else:
            daysInFebruary = 28
    else:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            daysInFebruary = 29
        else:
            daysInFebruary = 28
    day = 256 - 31 - daysInFebruary - 31 - 30 - 31 - 30 - 31 - 31
    assert (1 <= day <= 30)

    if day < 10:
        day = '0' + str(day)
    print('{}.09.{}'.format(day, year))


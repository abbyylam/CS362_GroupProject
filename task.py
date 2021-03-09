import re


def conv_num(num_str):  # noqa: C901
    def dec_hex(x):
        decimal = 0
        for i, d in enumerate(x):
            hexa = "0123456789ABCDEF"
            val = hexa.index(d)  # 0 to 15
            y = (len(x) - (i+1))  # power of 16
            decimal = (val*16**y) + decimal
        return decimal

    def dec_str():
        count = 0
        for i in num_str:
            if i == '.':  # check for fp num; if yes increment count
                count += 1
        if count > 1:
            return None
        num = 0
        res = 0
        fpres = 0  # floating-point result

        if count == 0:
            num = num_str
        if count == 1:
            # https://stackoverflow.com/questions/6681743/splitting-a-number-into-the-integer-and-decimal-parts
            num, fp = num_str.split('.')
            for digit in fp[::-1]:
                fpres /= 10
                for d in '0123456789':
                    fpres += digit > d
        if count == 0 or count == 1:
            for digit in num:
                res *= 10
                for d in '0123456789':
                    res += digit > d

        if count == 1:
            res = res + (fpres / 10)
        return res

    negative = False
    if num_str.startswith('-'):
        negative = True
        num_str = num_str[1:]
    if num_str.startswith('0x'):
        num_str = num_str[2:]  # https://stackoverflow.com/questions/47268595/when-to-use-re-compile
        hexpattern = re.compile("^[A-F0-9]+$")
        if hexpattern.match(num_str):
            result = dec_hex(num_str)
        else:
            return None
    else:  # https://stackoverflow.com/questions/40953460/redundant-escape-character-in-pattern
        nums_calc = re.compile("^[0-9\\.]+$")
        if nums_calc.match(num_str):
            result = dec_str()
        else:
            return None
    if negative:  # for negative results
        return result*-1
    return result


# determine how many days in a year (leap year or not)
def leap_year_check(year):
    # leap year if year number is divisible
    # by 4 or  400 except if by 100
    if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
        return 366
    elif year % 100 == 0:
        return 365
    # all other years are not leap years
    else:
        return 365


# determine year using num_sec
def get_year(days):
    # epoch year
    year = 1970
    # initial days
    days = days + 1

    while days > 0:
        # check for about of days in year
        days_in_year = leap_year_check(year)
        if days > days_in_year:
            # subtract days in year from initial days
            days = days - days_in_year
        # if less than a year, break
        else:
            break
        # increment year
        year = year + 1
    return year, days


# determine month and day from get_year function
def get_month(days, year):
    # if zero days left, first of month
    if days == 0:
        days = 1
    # if leap year, February has 29 days
    if leap_year_check(year) == 366:
        months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # if not leap year
    else:
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # epoch month
    month_num = 1

    for x in months:
        if x < days:
            # subtract num of days of each month from remaining days
            days = days - x
            # each month, increment month
            month_num = month_num + 1
        # if not enough days for month
        else:
            break
    return month_num, days


def my_datetime(num_sec):
    # 1 day = 86400 seconds
    num_days = num_sec // 86400
    # get year from get_year function
    year, days = get_year(num_days)
    # get month and day from get_month function
    month, days = get_month(days, year)
    # date formatting
    date = "%02d-%02d-%d" % (month, days, year)
    return date


def conv_endian(num, endian='big'):

    # validate input arguements
    assert type(num) == int, "Incorrect input"
    assert type(endian) == str, "Incorrect input"

    negativeNum = False

    # variables to store the output string,
    # and the bytes in a list in big endian order
    outputStr = ''
    bigEndianByteList = []

    # remove minus sign if negative number, set negativeNum
    if num < 0:
        negativeNum = True
        num = num * -1

    # return '00' byte
    if num == 0:
        return '00'

    rawHex = calc_raw_hex(num)

    # counters and formmating string variables
    i = len(rawHex) - 1
    charsInString = 0
    currentByteStr = ''
    while(i >= 0):
        # add a space after every byte but not before the first byte
        if (charsInString % 2 == 0) and outputStr != '':
            # add space character after byte
            outputStr = outputStr + ' '
            bigEndianByteList.append(currentByteStr)
            # reset byte string
            currentByteStr = ''
        outputStr = outputStr + rawHex[i]
        currentByteStr = currentByteStr + rawHex[i]
        charsInString = charsInString + 1
        i = i - 1

    # append last byte
    bigEndianByteList.append(currentByteStr)

    if endian == 'big':
        return make_neg(outputStr) if negativeNum else outputStr
    elif endian == 'little':
        outputStr = ''
        littleEndianByteList = bigEndianByteList[::-1]
        # reorder outputStr form big to little endian
        for byte in littleEndianByteList:
            outputStr = outputStr + byte
            outputStr = outputStr + ' '
        # remove final space characater
        outputStr = outputStr[:-1]
        return make_neg(outputStr) if negativeNum else outputStr
    else:
        return None


# add minus sign infron of arguement
def make_neg(arg_str):
    return '-' + arg_str


# calculate the hex of num and return it w/out formatting
def calc_raw_hex(num):
    # store the working (raw/unformatted) hex code
    workingHex = []
    while(num != 0):
        # store the remainder
        tmpRemainder = num % 16

        # append a alphanumeric or alphabetic character
        if(tmpRemainder < 10):
            workingHex.append(chr(tmpRemainder + 48))
        else:
            workingHex.append(chr(tmpRemainder + 55))

        # get rid off least significant value
        num = int(num / 16)

    # append a zero if odd numbered nibbles in list
    if len(workingHex) % 2 == 1:
        workingHex.append('0')

    return workingHex

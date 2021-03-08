

def conv_num(num_str):
    characters = "0123456789abcdefghijklmnopqrstuvwxyz"
    x = sum(characters.index(x)*36**i for i, x in enumerate(num_str[::-1]))
    return x


def my_datetime(num_sec):
    def leap_year_check(year):
        if year % 4 == 0:
            days = 366
        elif year % 100 == 0:
            days = 365
        elif year % 400 == 0:
            days = 366
        else:
            days = 365
        return days

    def get_year(days):
        year = 1969
        while days >= 0:
            year = year + 1
            days_in_year = leap_year_check(year)
            if days > days_in_year:
                days = days - days_in_year
            else:
                break
        return year, days

    def get_month(days, year):
        if days == 0:
            days = 1

        month_num = 1
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if leap_year_check(year) == 366:
            months[1] = 29
        for x in months:
            if x < days:
                month_num = month_num + 1
                days = days - x
            else:
                break
        return month_num, days
    num_days = num_sec // 86400

    year, days = get_year(num_days)
    month, days = get_month(days, year)

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
        num = abs_value(num)

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


# remove minus sign if negative number, set negativeNum
def abs_value(num):
    num = str(num)
    num = int(num[1:])
    return num


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

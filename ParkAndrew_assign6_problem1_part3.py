#goes through every month and goes throguh all the days to determine whehter the dates are valid

def valid_date(month, day):
    if month == 1:
        if 1 <= day <= 31:
            return True
        else:
            return False
    elif month == 2:
        if 1 <= day <= 28:
            return True
        else:
            return False
    elif month == 3:
        if 1 <= day <= 31:
            return True
        else:
            return False
    elif month == 4:
        if 1 <= day <= 30:
            return True
        else:
            return False
    elif month == 5:
        if 1 <= day <= 31:
            return True
        else:
            return False
    elif month == 6:
        if 1 <= day <= 30:
            return True
        else:
            return False
    elif month == 7:
        if 1 <= day <= 31:
            return True
        else:
            return False
    elif month == 8:
        if 1 <= day <= 31:
            return True
        else:
            return False
    elif month == 9:
        if 1 <= day <= 30:
            return True
        else:
            return False
    elif month == 10:
        if 1 <= day <= 31:
            return True
        else:
            return False
    elif month == 11:
        if 1 <= day <= 30:
            return True
        else:
            return False
    elif month == 12:
        if 1 <= day <= 31:
            return True
        else:
            return False
    else:
        return False

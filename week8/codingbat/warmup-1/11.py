

def sleep_in(weekday, vacation):
    if weekday is False and vacation is False:
        return True
    elif weekday is True and vacation is False:
        return False
    elif weekday is False and vacation is True:
        return True
    else:
        return True


import re
import datetime


def get_black_list_password():
    return (
        'qwerty123',
        '123',
        'qwe',
        '12qwaszx',
        'Password1',
        'Password',
        'Pass'
    )


def get_campaign_names():
    return (
        'BMW',
        'Mercedes',
        'Ubuntu',
        'Slack'
    )


def password_has_digits(password):
    return re.match(r'\d', password)


def password_has_abc(password):
    return bool(re.search(r'[a-z]', password.lower()))


def password_has_lover_and_upper_symbols(password):
    return bool(re.search(r'[a-z]', password)) and bool(re.search(r'[A-Z]+', password))


def password_has_special_characters(password):
    return bool(re.search(r'[^a-zA-Z0-9]', password))


def str_to_date(password):
    date_value = None
    date_formats = ['%Y%m%d', '%d%m%Y', '%Y.%m.%d', '%d.%m.%Y',
                    '%Y/%m/%d', '%d/%m/%Y', '%Y-%m-%d', '%d-%m-%Y']
    if (len(password) == 8 or len(password) == 10):
        for date_fmt in date_formats:
            try:
                date_value = datetime.datetime.strptime(password, date_fmt).date()
            except ValueError:
                pass
    return date_value


def has_calendar_date(password):
    return str_to_date(password)


def has_phone_number(password):
    if (re.match(r'[8]{1}[9]{1}[0-9]{9}', password) and len(password)) == 11:
        return True
    elif (re.match(r'[+]{1}[7]{1}[9]{1}[0-9]{9}', password) and len(password)) == 12:
        return True
    else:
        return False


def get_password_strength(password):
    strength = 1
    if password in get_black_list_password():
        return strength
    if len(password) < 6:
        return strength
    if password in get_campaign_names():
        return strength
    if has_calendar_date(password):
        return strength
    if has_phone_number(password):
        return strength

    if password_has_digits(password):
        strength += 2
    if password_has_abc(password):
        strength += 2
    if password_has_lover_and_upper_symbols(password):
        strength += 2
    if password_has_special_characters(password):
        strength += 2

    return strength

if __name__ == '__main__':
    password = input('Write your password: ')
    print(get_password_strength(password))

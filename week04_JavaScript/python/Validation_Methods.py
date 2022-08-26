
users = [{'first': 'Dez', 'last': 'Bryan', 'phone': '(706)-301-7063', 'zipcode': '30189', 'email' : 'dezareabryan@gmail.com'}]

#Basic checks for user input
def validator(users: list):
# Checks if the number has all required chars
    if len(users[0].get('phone')) != 14:
        print('ERROR: Invalid phone number entered')
        return False
    # Checks if number has correct number of -
    elif len(users[0].get('phone').split('-')) != 3:
        print('ERROR: Must follow format (xxx)-xxx-xxxx')
        return False
    # Checks if () are in the correct position
    elif users[0].get('phone')[0] != '(' or users[0].get('phone')[4] != ')':
        print('ERROR: () is in wrong position')
        return False
    # Checks if - are in the correct position
    elif users[0].get('phone')[5] != '-' or users[0].get('phone')[9] != '-':
        print('ERROR: - is in wrong position')
        return False
    # Checks if zip code is 5 digits
    elif len((users[0].get('zipcode'))) != 5:
        print('ERROR: zip code must be 5 digits')
        return False
    # Checks if zip codes are in a valid range
    elif (users[0].get('zipcode')) < '00501' or users[0].get('zipcode') > '99950':
        print('ERROR: Not a valid US zip code')
        return False
    elif '@' not in (users[0].get('email')):
        print('ERROR: Not a valid email')
        return False
    elif ('@gmail.com' or "@hotmail.com" or '@yahoo.com') not in (users[0].get('email')):
        return False
    else:
        return True
print(f'Valid?: {validator(users)}')

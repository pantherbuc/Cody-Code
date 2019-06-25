#This program asks the user to set upper and lower limits, then asks the user to input a number within that range.

def divider():
    print('')
    print('---------------------------------------------')
    print('')


def range_check():
    if int(newnumber) <= int(lower_limit):
        print('This value is ' + str(int(lower_limit) - int(newnumber)) + ' below your lower range')
    if int(newnumber) >= int(upper_limit):
        print('This value is ' + str(int(newnumber) - int(upper_limit)) + ' above your upper range')
    if (int(newnumber) <= int(upper_limit)) and (int(newnumber) >= int(lower_limit)):
        print('Success! This value fits within your range.')
        print(str(newnumber) + ' is ' + str(
            int(upper_limit) - int(newnumber)) + ' less than your upper limit, and ' + str(
            int(newnumber) - int(lower_limit)) + ' more than your lower limit.')


upper_limit = input('please input upper limit: ')
while upper_limit:
    if upper_limit.isdigit():
        break
    else:
        upper_limit = input('Invalid. Please input a number for your upper limit: ')

upper_limit = int(upper_limit, 10)

lower_limit = input('please input lower limit: ')
while lower_limit:
    if lower_limit.isdigit() and int(lower_limit, 10) < upper_limit:
        break
    else:
        lower_limit = input(
            'Invalid. Please make sure your lower limit is a numeral that is a lesser value than ' + str(
                upper_limit) + ': ')

divider()
newnumber = 1

while newnumber:
    newnumber = input('Input a value between ' + str(lower_limit) + ' and ' + str(upper_limit) + ': ')
    if newnumber.isdigit:
        range_check()
        divider()
    else:
        print('Please enter a numeral value: ')

divider()
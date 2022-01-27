import pandas as pd


string_to_convert = '2020-02-01'
print ('Your string: {}'.format(string_to_convert))
print ('Your string_to_convert type: {}'.format(type(string_to_convert)))
print ()

# Convert your string
new_date = pd.to_datetime(string_to_convert)

print ('Your new date is: {}'.format(new_date))
print ('Your new type is: {}'.format(type(new_date)))


print ('--------------------------------------')
string_to_convert = '2020-3-6'
print ('Your string: {}'.format(string_to_convert))
print ('Your string_to_convert type: {}'.format(type(string_to_convert)))
print ()

# Convert your string
new_date = pd.to_datetime(string_to_convert)

print ('Your new date is: {}'.format(new_date))
print ('Your new type is: {}'.format(type(new_date)))
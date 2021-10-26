# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
# for requested_topping in requested_toppings:
#     if requested_topping == 'green peppers':
#         print("\tSorry, we are out of green peppers right now.")
#     else:
#         print("\tAdding " + requested_topping + ".")

# print('\nFinished making your pizza. ')

# all_toopings = ['carrot','mushroom','beetroot','cheese','green pepper', 'mushrooms', 'extra paneer', 'extra cheese']
# unavailable_toppings = ['carrot', 'mushroom', 'beetroot']

# for toopings in all_toopings:
#     for unavailable_topping in unavailable_toppings:
#         if toopings == unavailable_topping:
#             print('Sorry, unable to add ', toopings)
#         else:
#             print('Added ', toopings, '.')

# print('\nFinished making your pizza.')


# available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
# requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

# for requested_topping in requested_toppings:
#     if requested_topping in available_toppings:
#         print('Adding ' + requested_topping + '.')
#     else:
#         print("We don't have " + requested_topping + '.')

# print('\nFinished making your pizza.')

# admins = []

# if admins:
#     for x in admins:
#         if x == 'admin':
#             print('Hello Admin, would you like to see a status report?')
#         else:
#             print('Hello ' + x.title() + ', thank you for logging in again.')
# else:
#     print('We need to find some users.')

# current_users = ['Akshit', 'Ashwith', 'Naresh Kumar', 'Sowjanya', 'John', 'SheeTAl']
# new_users = ['Akshit', 'Ashwith', 'ramesh', 'suresh', 'saiesh', 'SheeTAL']

# for new_user in new_users:
#     if new_user in current_users:
#         print(new_user + ' username is unavailable.')
#     else:
#         print(new_user + ' username is available.')

numbers = [1,2,3,4,5,6,7,8,9]
for num in numbers:
    if num == 1:
        print('1st')
    elif num == 2:
        print('2nd')
    elif num == 3:
        print('3rd')
    elif num > 3:
        print(str(num) +'th')

print('\nEnd of ordinal numbers.')

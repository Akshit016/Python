# alien = {'color' : 'green'}
# # print('The color of the alien is ' + alien['color'] + '.')

# # alien['color'] = 'yellow'
# # print('The color of the alien is ' + alien['color'] + '.')

# alien = {'x_position' : 0, 'y_position' : 25, 'speed' : 'medium'}

# # Move the alien to the right.
# # Determine how far to move the alien based on its current speed.

# if alien['speed'] == 'slow':
#     x_increment = 1
# elif alien['speed'] == 'medium':
#     x_increment = 2
# else:
#     x_increment = 3
# # old position of the alien
# print('Old Postion: ' + str(alien['x_position']))
# # the new position is the old position plus the increment
# alien['x_position'] = alien['x_position'] + x_increment #this is an integre
# print('New x-position: ' + str(alien['x_position']))

# alien0 = {'color' : 'green', 'points':5}
# print(alien0)

# del alien0['points']
# print(alien0)

# favourite_languages = {
#     'akshit' : 'python',
#     'suresh' : 'java',
#     'ramesh' : 'ruby',
#     'sheetal' : 'python'
# }

# print("Akshit's favourite language is " + favourite_languages['akshit'].title() + '.')

person = {
    'fullname' : 'sai akshit',
    'city' : 'hyderabad',
    'age' : '17'
}

print('My name is ' + person['fullname'].title() + " I'm " + person['age'] + ", I live in " + person['city'].title() + '.')
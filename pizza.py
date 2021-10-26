available_toppings = ['mushrooms', 'panner', 'olives', 'green pepper', 'extra cheese', 'pepperoni']
requested_toppings = ['mushrooms', 'french fries', 'green pepper']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print('Added ' + requested_topping.title())
    else:
        print(requested_topping.title() + ' is unavailable')

print('\nYour pizza is finished.')
# for x in range(1,1000001):
#     print(x)

# milnumbers = [x for x in range(1,1000001)]
# print("The min in 1 mil numbers is:", min(milnumbers))
# print("The max in 1 mil numbers is:", max(milnumbers))
# print("The sum of 1 mil numbers is:", sum(milnumbers))

# for num in range(1,21,2): #printing odd numbers between 1 to 20
#     print(num)

#this prints the multiples of a 3 table
# for x in range(1,11):
#     multiple = 3 * x
#     print("3 x ",x," = ", multiple)

# #printing the cubes from 1 to 10
# for num in range(1,11):
#     print(num**3)

# using list comprehension to print cubes from 1 to 10
# cubes = [value**3 for value in range(1,11)]
# for x in cubes:
#     print(x)

players = ['virat kohli', 'dhoni', 'yuvaraj',
                     'raina', 'sachin tendulakar']
#print(players[0:3]) #printing the elements from index 0 to 2(3-1)

#print(players[:4]) #if we omit the beginning index it takes 0 as default
# print(players[-3:])

#when we create a slice from a list, it creates another list
# print("Here are first 3 players from my team: ")
# for player in players[:3]:
#     print(player.title())

new_players = players[:]
new_players.append('siraj')
new_players.append('chahal')
print(new_players)


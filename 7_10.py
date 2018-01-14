# 7-10. Dream Vacation: Write a program that polls users about their dream
# vacation. Write a prompt similar to If you could visit one place in the world,
# where would you go? Include a block of code that prints the results of the poll.
polling={}
active=True
polling_count=0
while active:
    place=input('If you could visit one place in the world,where would you go?')

    if place=='quit':
        active=False
    else:
        polling_count += 1
        x=polling.get(place,0)+1
        polling[place]=x
print('POLLING RESULT'+' of total '+str(polling_count))
for world_place,val in polling.items():
    print(world_place+':'+str(val))
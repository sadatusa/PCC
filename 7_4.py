
Toppings=0
Pizza_Topping=''
Pizza_Toppings=[]
while Toppings<=5:

    Pizza_Topping = input('Please input topping')
    if Pizza_Topping=="DONE":
        break
    #Pizza_Toppings = Pizza_Toppings+Pizza_Topping+' '
    Pizza_Toppings.append(Pizza_Topping)
    Toppings+=1
    print('You ADDED TOPPING'+Pizza_Topping)
    print('You added toppings ',end='')
for x in range(0,len(Pizza_Toppings)-1):
    print(Pizza_Toppings[x],end='')
print(' and ')
# 7-8. Deli: Make a list called sandwich_orders and fill it with the names of various
# sandwiches. Then make an empty list called finished_sandwiches. Loop
# through the list of sandwich orders and print a message for each order, such
# as I made your tuna sandwich. As each sandwich is made, move it to the list
# of finished sandwiches. After all the sandwiches have been made, print a
# message listing each sandwich that was made.

order_number=0
def sandwich_order(order_list):
    global order_number
    order_number=order_number+1
    finished_sandwiches=[]
    while order_list:
    #finished_sandwiches.append(sandwich_orders.pop())
        finished_sandwiches.insert(0,order_list.pop())
    print('finished_sandwiches ',order_number)
    for finished_sandwich in finished_sandwiches:
        print(finished_sandwich)

sandwich_order(['Sandwich-1','Sandwich-2','Sandwich-3'])
sandwich_order(['Sandwich-a','Sandwich-b','Sandwich-c'])
sandwich_order(['Sandwich-x','Sandwich-y','Sandwich-z'])
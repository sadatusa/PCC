# 5-10. Checking Usernames: Do the following to create a program that simulates
# how websites ensure that everyone has a unique username.
# • Make a list of five or more usernames called current_users.
# • Make another list of five usernames called new_users. Make sure one or
# two of the new usernames are also in the current_users list.
# • Loop through the new_users list to see if each new username has already
# been used. If it has, print a message that the person will need to enter a
# new username. If a username has not been used, print a message saying
# that the username is available.
# • Make sure your comparison is case insensitive. If 'John' has been used,
# 'JOHN' should not be accepted.


current_users = ['aslam', 'sadat', 'aamir', 'saleem', 'kamal']
new_users = ['sami', 'sadat', 'akram', 'jameel', 'areeb']
for x in range(0, len(current_users)):
    current_users[x] = current_users[x].upper()
for x in range(0, len(new_users)):
    new_users[x] = new_users[x].upper()
for new_user in new_users:
    if new_user in current_users:
        print(new_user + " not available")
    else:
        print(new_user + " available")

# 5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elifelse
# chain.
# • If the alien is green, print a message that the player earned 5 points.
# • If the alien is yellow, print a message that the player earned 10 points.
# • If the alien is red, print a message that the player earned 15 points.
# • Write three versions of this program, making sure each message is printed
# for the appropriate color alien.


aliencolor="green"
if aliencolor=="green":
    print("player just earned 5 points")
elif aliencolor=="yellow":
    print("player just earned 10 points")
elif aliencolor=="red":
    print("player just earned 15 points")
else:
    print("")

aliencolor="yellow"
if aliencolor=="green":
    print("player just earned 5 points")
elif aliencolor=="yellow":
    print("player just earned 10 points")
elif aliencolor=="red":
    print("player just earned 15 points")
else:
    print("")

aliencolor="red"
if aliencolor=="green":
    print("player just earned 5 points")
elif aliencolor=="yellow":
    print("player just earned 10 points")
elif aliencolor=="red":
    print("player just earned 15 points")
else:
    print("")



# Assignment to take land off plane

# Driver code
altitude = 53000

if altitude > 10000:
    print("You're {}.ft still flying so don't land you're plane!".format(altitude))
elif altitude <= 5000:
    print("You're {}.ft yeah! you're plane ready to land!!!".format(altitude))
else:
    print("You're {}.ft you landed you're plane successfully".format(altitude))
    print('"Thank - you"')
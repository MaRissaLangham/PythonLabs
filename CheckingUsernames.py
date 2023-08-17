currentUsers = ['john', 'james', 'jane', 'jim', 'joe', 'jerry']
newUsers = ['jim', 'joe', 'jerry', 'josh', 'jake', 'jill']

if newUsers:
    for user in newUsers:
        if user.lower() in currentUsers:
            print("Sorry, the username " + user + " is already taken.")
        else:
            print("The username " + user + " is available.")
            
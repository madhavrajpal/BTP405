def authorize(func):
    profiles = {"Madhav":"maddy"}

    def authorizing_func(*args):
       # print(args)
        if args[0] not in profiles:
            print("no user")
        elif profiles[args[0]] !=  args[1]:
            print("wrong password")
        else: 
            func(args[0],args[1])

    return authorizing_func

@authorize
def tryAuthorize(userName,password):
    print("authorization successfull")

tryAuthorize("Madhav","maddy")
tryAuthorize("Madhav","my")
tryAuthorize("Ma","maddy")

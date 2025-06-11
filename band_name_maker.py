topics = ["color", "shape", "animal", "verb"]
favorites = []
name = input("What is your name? ")
print("Hello " + name.title() + "!")
print("Let's make something fun!")

def get_topic():
    print("Pick a topic from the list below:")
    for t in topics:
        print("\t" + t)
    topic = input("What topic would you like? or enter esc to end. ")
    if topic == "esc":
        list_results()
        return
    else:
        get_fav(topic)

def list_results():
    for i, f in enumerate(favorites):
        print(f"{i+1}. " + f.title())
    print("Your band name is:")
    if len(favorites) == 4:
        print(f"{name.title()}'s {favorites[3].title()} {favorites[0].title()} {favorites[1].title()} "
              f"{favorites[2].title()}")
    if len(favorites) == 3:
        print(f"{favorites[0].title()} {favorites[1].title()} {favorites[2].title()}s")
    elif len(favorites) == 2:
        print(f"The {favorites[0]} {favorites[0]} {favorites[1]}")
    elif len(favorites) == 1:
        print(f"{name.title()} {favorites[0].title()}")
    elif len(favorites) > 4:
        print("The")
        for f in favorites:
            print(f.title())
        print("Band")
    elif len(favorites) == 0:
        print("Not enough information to make your band name. Try again!")
    print("____________________________________________")


def get_fav(x):
    print("Okay, " + x.lower() + "!" )
    fav = input("What is your favorite " + x.lower() + "? ")
    print(fav * 3)
    print(fav.title() + " is your favorite " + x + "!")
    favorites.append(fav)
    confirm = input("Keep going? y or n: ")
    if confirm == "y":
        get_topic()
    else:
        # if you run a method in a print string in pyton,
        # it will run the method before it prints (same behavior for including
        # input in a print statement). Here, I want the function to run after
        # so that it doesn't print:
        # "Zebra Red Circle Your favorites are "
        # so this won't work: print("Your favorites are ", list_results())
        print("Your favorites are:")
        list_results()
        print("Goodbye!")
        return


get_topic()
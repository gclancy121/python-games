from random import randint

lib1 = ['My name is', '. I like', 'and my favorite video game is', '.']
lib2 = ['The best song is', 'by the artist', 'because it makes me feel', '.']
lib3 = ['Dear', 'your application has been rejected because you lack', ". We're sorry, but for now you should", '.']
lib4 = ['My favorite place to go is', ". While I'm there, I like to do", "and", 'everyday!']
lib5 = ["I'm going to the doctor tomorrow to get my", 'examined. It will be', 'but I feel', 'about it.']
lib6 = ['Every time I see you', 'I get down on my', 'and', "I'm waiting for that final", "You say the words I cannot say"]

all_libs = [lib1, lib2, lib3, lib4, lib5, lib6]
option = randint(0, 5)


if option == 0:
    name = input("Enter a name: ")
    noun = input('Enter a plural noun: ')
    vgt = input('Enter a video game title: ')
    print(lib1[0], name, lib1[1], noun, lib1[2], vgt, lib1[3])
elif option == 1:
    title = input('Enter a song title: ')
    artist = input("Enter a song title: ")
    feeling = input("Enter a feeling: ")
    print(lib2[0], title, lib2[1], artist, lib2[2], feeling, lib2[3])
elif option == 2: 
    name = input("Enter a name: ")
    adj = input("Enter an adjective: ")
    activity = input('Enter an activity: ')
    print(lib3[0], name, lib3[1], adj, lib3[2], activity, lib3[3])
elif option == 3:
    loc = input('Enter a location: ')
    act1 = input('Enter an activity: ')
    act2 = input('Enter a second activity: ')
    print(lib4[0], loc, lib4[1], act1, lib4[2], act2, lib4[3])
elif option == 4:
    part = input("Enter a part of the body: ")
    feeling = input("Enter a feeling: ")
    feeling2 = input("Enter a second feeling: ")
    print(lib5[0], part, lib5[1], feeling, lib5[2], feeling2, lib5[3])
elif option == 5: 
    activity = input('Enter an activity: ')
    part = input("Enter a body part: ")
    act2 = input("Enter an activity: ")
    time = input("Enter a measure of time: ")
    print(lib6[0], activity)
    print(lib6[1], part, lib6[2], act2)
    print(lib6[3], time)
    print(lib6[4])
else :
    print("Something went wrong, start the program over.")
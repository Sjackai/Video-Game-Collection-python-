#stanley Jackai
#3/13/25
#comp.163002
#With this program I created a data base where the user can input any game they like, input some info and it will save into a collection.
#The user can also search their list of games by title and platform
user_choice = '' # create an empty string variable to put  users menu pick
game_collection = [] #create empty list to hold game dict

print('Welcome to the Video Game Collection Database!') #welcome message to user
print('\n===== VIDEO GAME COLLECTION DATABASE =====') #print title of program
while user_choice != 5: #while loop will continue  until user picks 5
    print('1. Add a new game') #List all menu options user can pick
    print('2. Display all games')
    print('3. Search by title')
    print('4. Search by platform')
    print('5. Exit')
    print('Enter your choice (1-5): ') #Tells user to enter their choice from menu
    user_input = input() #read user input as a string / ' '

    if user_input.isdigit(): #If the user enters a nummber (isdigit) then the string becomes an int
        user_choice = int(user_input)
    else: #if the user doesnt enter a int then the have to retry
        print("Invalid choice. Please try again.")
        print('\n===== VIDEO GAME COLLECTION DATABASE =====') #reshows title
        continue #will skip the rest of the loop so user can retry

    if user_choice == 1:
        print('----- Add New Game -----') #If user puts 1 then it will display them to add a new game
        user_game_title = input('Enter game title:') #The user will enter the info of the game they want to add
        user_game_release_year = input(' Enter release year:')
        user_game_developer = input(' Enter developer:')
        user_game_platform = input(' Enter platform:')
        user_game_genre = input(' Enter genre:')
        user_game_rating = int(input(' Enter your rating (1-10): '))
        game = { #I created a dict. 'game' to store the users game info
            'title': user_game_title,
            'release_year': user_game_release_year,
            'developer': user_game_developer,
            'platform': user_game_platform,
            'genre': user_game_genre,
            'rating': user_game_rating
        }
        game_collection.append(game) #put that dict. inside the list so we can call it later with append
        print(f'\n{user_game_title} has been added to your collection.') #shows the user we just added their game to their collection of games aka the list
        print('\n===== VIDEO GAME COLLECTION DATABASE =====') #Reshows the tite

    elif user_choice == 2:
        if not game_collection: #If the user puts 2 and their game isnt in the dict. 'game' which is in the game_collelction list it will print this
            print("Your collection is empty.")
            print('\n===== VIDEO GAME COLLECTION DATABASE =====') #Reshow the title to user and loop will end
        else: #if the user puts 2 it will go through the game collection list and will just print the dictionary since thats all thats in the list
            for game in game_collection:
                print('===== YOUR GAME COLLECTION =====') #shows the user what will be displayed
                print(f"1. {game['title']} ({game['release_year']}) - Developed by {game['developer']}\n"
                      f"Platform: {game['platform']}, Genre: {game['genre']}, Your Rating: {game['rating']}/10")
                print()
                print('\n===== VIDEO GAME COLLECTION DATABASE =====')#reshow header and end loop

    elif user_choice == 3: #if the user puts 3 to search for title but their title isnt in the dict.[title] which is in the list then it will say this
        if not game_collection:
            print("Your collection is empty.")
            print('\n===== VIDEO GAME COLLECTION DATABASE =====') #reshow title and end loop
        else:
            print("Enter title to search for: ")#otherwise get the user input and make it a substring
            user_sub_string = input()
            found_count = 0 #I created a counter for each time a word / substring is found
            matches = [] #that title of the game will go inside this new list 'matches'
            for game in game_collection: #it will go thru the list and if the substring/title is in the dict[title]it will add 1 to the counter
                #and add that title to the matches list
                if user_sub_string.lower() in game['title'].lower():
                    found_count += 1
                    matches.append(game)
            if found_count > 0: #after it goes thru loop if the counter goes up at least one then print how many times
                print(f"Found {found_count} matches:")
                for game in matches: #It will go through the list 'matches' which is just all the matching games
                    #It will print the game info
                    print(f"{game['title']} ({game['release_year']}) - Developed by {game['developer']}\n"
                          f"Platform: {game['platform']}, Genre: {game['genre']}, Your Rating: {game['rating']}/10\n")
                print('\n===== VIDEO GAME COLLECTION DATABASE =====')#reshow title and end loop

    elif user_choice == 4: #If the user wants to search by platform
        if not game_collection: #if user choice isnt in game collection list this will print
            print("Your collection is empty.")
            print('\n===== VIDEO GAME COLLECTION DATABASE =====')
        else: #if userchoice is in the game collection list they will get asked which platform to search in and i turned it into a
            #variable user platform string
            user_platform_string = input('Enter platform to search for:\n')
            found_count = 0 #I again created a counter to just keep track of matches
            matches = [] #I again created another match list to track of matches
            for game in game_collection: #It will go thru the game collection list turn the users input into lowercase and see if it matches up
                #with the platform part in the game dict. which I also turned into lowercase
                if user_platform_string.lower() in game['platform'].lower(): #if it does match with it then add 1 to the counter and add it to
                    #the new match list
                    found_count += 1
                    matches.append(game)
            if found_count > 0:
                #after it goes thru loop if the counter goes up at least one then print how many times
                print(f"Found {found_count} matches:") #print how many times the platform was found using the counter
                print()
                for game in matches: #goes thru each matching platform in the game dict. and prints out the info
                    print(f"\n{game['title']} ({game['release_year']}) - Developed by {game['developer']}\n")
                    print(f'Platform: {game['platform']}, Genre: {game['genre']}, Your Rating: {game['rating']}/10')
                    print()
                    print('\n===== VIDEO GAME COLLECTION DATABASE =====')

    elif user_choice == 5: #if the user wants to quit the loop will end
        pass
    elif user_choice < 1 or user_choice > 5: #if the user choice is greater/smaller than whats displayed '1-5' let them
        #know its an invalid choice and to retry
        print("Invalid choice. Please try again.\n===== VIDEO GAME COLLECTION DATABASE =====")

print('Thank you for using the Video Game Collection Database. Goodbye!')
#since the userchoice is 5 the while loop wont work
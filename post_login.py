def post_login_menu(user_mgmt, social_graph, username):
    while True:
        print(f"\nWelcome back, {username}!")
        #we can add all the remaining usecases here, like view profile, edit profile etc.
        print("4. Edit Profile")
        print("9. Friend Recommendations")
        print("12. Logout")

        choice = input("Enter option: ")


        # refactored to use a match case block, as it is more efficient.
        match choice:
            case "4":
                pass
            case 9:
                social_graph.friend_recommendations(username)
            case 12:
                print("Logging out... 👋")
                break

            case _:
                print("Invalid choice. Please try again.")


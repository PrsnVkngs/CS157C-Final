def post_login_menu(user_mgmt, social_graph, username):
    while True:
        print(f"\nWelcome back, {username}!")
        #we can add all the remaining usecases here, like view profile, edit profile etc.
        print("9. Friend Recommendations")
        print("12. Logout")

        choice = input("Enter option: ")

        if choice == "9":
            social_graph.friend_recommendations(username)
        elif choice == "12":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

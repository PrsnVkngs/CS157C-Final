def post_login_menu(user_mgmt, social_graph, username):
    while True:
        print(f"\nWelcome back, {username}!")
        #we can add all the remaining usecases here, like view profile, edit profile etc.
        print("3. View Profile")
        print("7. View Followers/Following")
        print("8. Find Mutual Connections")
        print("9. Friend Recommendations")
        print("10. Search Users")
        print("12. Logout")

        choice = input("Enter option: ")
        if choice == "3":
            social_graph.get_user_info(username)
        elif choice == "7":
            social_graph.get_user_followers(username)
            social_graph.get_user_following(username)
        elif choice == "8":
            other_username = input("Enter the username to find mutual connections with: ")
            social_graph.get_mutual_connections(username, other_username)
        elif choice == "9":
            social_graph.friend_recommendations(username)
        elif choice == "10":
            search_term = input("Enter name or username to search: ")
            social_graph.search_users(search_term)
        elif choice == "12":
            print("Logging out... 👋")
            break
        else:
            print("Invalid choice. Please try again.")

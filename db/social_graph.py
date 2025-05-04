class SocialGraph:
    def __init__(self, connection):
        self.connection = connection

    #we can add the database logic part for remaining usecases here, like view profile, edit profile etc.
    def get_user_info(self, username):
        with self.connection.driver.session() as session:
            result = session.run("""
            MATCH (u:User {username: $username})
            RETURN u.userId AS userId, u.firstName AS firstName, u.lastName AS lastName, 
                   u.username AS username, u.email AS email, u.bio AS bio,
                   u.location AS location, u.country AS country
            """, username=username)
            record = result.single()

            if record:
                print(f"User Info:")
                print(f"User ID: {record['userId']}")
                print(f"Name: {record['firstName']} {record['lastName']}")
                print(f"Username: {record['username']}")
                print(f"Email: {record['email']}")
                print(f"Bio: {record['bio']}")
                print(f"Location: {record['location']}")
                print(f"Country: {record['country']}")
                return record
            else:
                print("User not found.")
                return None
    
    def get_user_followers(self, username):
        with self.connection.driver.session() as session:
            result = session.run("""
            MATCH (u:User {username: $username})<-[:FOLLOWS]-(f:User)
            RETURN f.username AS follower_username
            """, username=username)
            followers = [record["follower_username"] for record in result]
            
            if followers:
                print(f"Followers of {username}:")
                for follower in followers:
                    print(f"- {follower}")
                return followers
            else:
                print(f"{username} has no followers.")
                return []
    
    def get_user_following(self, username):
        with self.connection.driver.session() as session:
            result = session.run("""
            MATCH (u:User {username: $username})-[:FOLLOWS]->(f:User)
            RETURN f.username AS following_username
            """, username=username)
            following = [record["following_username"] for record in result]
            
            if following:
                print(f"{username} is following:")
                for user in following:
                    print(f"- {user}")
                return following
            else:
                print(f"{username} is not following anyone.")
                return []

    #UC 9:
    def friend_recommendations(self, username):
        with self.connection.driver.session() as session:
            result = session.run("""
                MATCH (me:User {username: $username})-[:FOLLOWS]->(friend:User)-[:FOLLOWS]->(rec:User)
                WHERE NOT (me)-[:FOLLOWS]->(rec) AND me <> rec
                RETURN DISTINCT rec.username AS recommended_user
                LIMIT 10
            """, username=username)

            print("\n--- Friend Recommendations ---")
            recommendations = result.values()
            if recommendations:
                for rec in recommendations:
                    print(f"- {rec[0]}")
            else:
                print("No recommendations available.")

    def get_mutual_connections(self, username1, username2):
        """
        Find mutual connections between two users.
        Returns users who are followed by both username1 and username2.
        """
        with self.connection.driver.session() as session:
            result = session.run("""
                MATCH (user1:User {username: $username1})-[:FOLLOWS]->(mutual:User)
                MATCH (user2:User {username: $username2})-[:FOLLOWS]->(mutual)
                RETURN mutual.username AS mutual_friend
            """, username1=username1, username2=username2)
            
            mutual_connections = result.values()
            
            print(f"\n--- Mutual Connections between {username1} and {username2} ---")
            if mutual_connections:
                for connection in mutual_connections:
                    print(f"- {connection[0]}")
                print(f"Total mutual connections: {len(mutual_connections)}")
            else:
                print("No mutual connections found.")

    def search_users(self, search_term):
        """
        Search for users by username or name (firstName/lastName).
        Returns and prints users that match the search criteria.
        """
        with self.connection.driver.session() as session:
            result = session.run("""
                MATCH (u:User)
                WHERE u.username CONTAINS $search_term 
                   OR toLower(u.firstName) CONTAINS toLower($search_term)
                   OR toLower(u.lastName) CONTAINS toLower($search_term)
                RETURN u.userId AS userId, u.firstName AS firstName, u.lastName AS lastName, 
                       u.username AS username, u.location AS location
                LIMIT 10
            """, search_term=search_term)
            
            users = list(result)
            
            print(f"\n--- Search Results for '{search_term}' ---")
            if users:
                for i, user in enumerate(users, 1):
                    print(f"{i}. {user['firstName']} {user['lastName']} (@{user['username']})")
                    if user['location']:
                        print(f"   Location: {user['location']}")
                print(f"\nFound {len(users)} matching users.")
                return users
            else:
                print("No users found matching your search criteria.")
                return []



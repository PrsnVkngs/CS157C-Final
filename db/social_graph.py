class SocialGraph:
    def __init__(self, connection):
        self.connection = connection

    #we can add the database logic part for remaining usecases here, like view profile, edit profile etc.

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

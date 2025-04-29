import hashlib

class UserManagement:
    def __init__(self, connection):
        self.connection = connection

    def register_user(self, name, email, username, password):
        hashed_pw = hashlib.sha256(password.encode('utf-8')).hexdigest()
        with self.connection.driver.session() as session:
            session.run("""
                MERGE (u:User {username: $username})
                ON CREATE SET u.name = $name, u.email = $email, u.password = $password
            """, name=name, email=email, username=username, password=hashed_pw)
        print(f"User '{username}' registered successfully.")

    def login_user(self, username, password):
        with self.connection.driver.session() as session:
            result = session.run("""
                MATCH (u:User {username: $username})
                RETURN u.password AS hashed_password
            """, username=username)
            record = result.single()

            if record:
                stored_hashed = record["hashed_password"]
                hashed_input = hashlib.sha256(password.encode('utf-8')).hexdigest()
                if hashed_input == stored_hashed:
                    print(f"Login successful! Welcome, {username}!")
                    return True
                else:
                    print("Incorrect password.")
                    return False
            else:
                print("Username not found.")
                return False
    
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
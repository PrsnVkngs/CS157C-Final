import bcrypt

class UserManagement:
    def __init__(self, connection):
        self.connection = connection

    def register_user(self, name, email, username, password):
        hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
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
                if bcrypt.checkpw(password.encode('utf-8'), stored_hashed.encode('utf-8')):
                    print(f"Login successful! Welcome, {username}!")
                    return True
                else:
                    print("Incorrect password.")
                    return False
            else:
                print("Username not found.")
                return False



from db import SocialNetworkDB

# Set your credentials
uri = "bolt://localhost:7687"
user = "neo4j"
password = "<your_password>"

db = SocialNetworkDB(uri, user, password)
db.test_connection()
db.close()

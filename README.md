# CS157C-Final

## Database connection setup

1. In local neo4j desktop, create new database called SocialGraph and set password to it.
2. Create python virtual environment in local:
   `python -m venv venv`
   `source venv/bin/activate` (On Windows: `venv\Scripts\activate`)
3. Install dependencies in requirements.txt
4. Run main.py file : `python main.py`
5. You should be able to see 'Neo4j Connected' message.


## Folder Structure
SocialNetwork/
├── db/
│   ├── __init__.py              # (keeps the folder as a package)
│   ├── connection.py            # (Neo4j connection setup only)
│   ├── user_management.py       # (register, login, view profile, edit profile)
│   └── social_graph.py          # (follow, unfollow, recommendations, mutual connections)
├── main.py
├── register.py
├── login.py
├── post_login.py



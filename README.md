## StarNavi Test Task

#### JWT - Authentication
```
Get JWT:
http://127.0.0.1:8000/login

Refresh JWT:
http://127.0.0.1:8000/login/refresh

Verify JWT:
http://127.0.0.1:8000/login/verify
```

#### Posts
```
GET List of Posts:
http://127.0.0.1:8000/posts

GET Post Details:
http://127.0.0.1:8000/posts/slug

POST Create New Post:
http://127.0.0.1:8000/posts

POST Like/Unlike Post
http://127.0.0.1:8000/posts/slug/like
```

#### Users
```
GET Users List
http://127.0.0.1:8000/users/

GET User Details
http://127.0.0.1:8000/users/user_id/

POST Create New User
http://127.0.0.1:8000/users/
```

## Robot Bot
Config: 'botconfig.ini'

#### Run bot activity
run_bot.py
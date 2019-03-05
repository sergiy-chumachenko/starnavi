## Implemented Parts
##### Basic models:
- User
- Post (always made by a user)

##### Basic features:
- user signup
- user login
- post creation
- post like
- post unlike

##### Authentication:
- use Token authentication (JWT)

##### Additional tasks:
- use clearbit.com/enrichment for getting additional data for the user on signup
- use emailhunter.co for verifying email existence on signup

#### Automated Bot creates activity:
- the Bot reads the configuration and create this activity;
- signup users (number provided in config);
- each user creates random number of posts with any content (up to max_posts_per_user);
- after creating the signup and posting activity, posts should be liked randomly, posts can be liked multiple times;
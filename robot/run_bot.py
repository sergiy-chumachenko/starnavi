from robot.bot import Bot
import configparser

config = configparser.ConfigParser()
config.read('botconfig.ini')

if __name__ == "__main__":
    number_of_users = config['MAIN']['NUMBER_OF_USERS']
    max_posts_per_user = config['MAIN']['MAX_POSTS_PER_USER']
    max_likes_per_user = config['MAIN']['MAX_LIKES_PER_USER']
    url = config['MAIN']['URL']
    bot = Bot(max_posts_per_user=max_posts_per_user,
              max_likes_per_user=max_likes_per_user,
              number_of_users=number_of_users,
              url=url)
    posts_counter = 0
    like_unlike_actions_counter = 0
    for _ in range(int(number_of_users)):
        auth_data = bot.create_user()
        posts_counter += bot.create_posts(auth_data=auth_data)
        like_unlike_actions_counter += bot.create_likes(auth_data=auth_data)
    print(
        f"---> {number_of_users} users has created\n"
        f"---> {posts_counter} posts has created\n"
        f"---> {like_unlike_actions_counter} actions has done")

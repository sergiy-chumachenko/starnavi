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
    auth_data = bot.create_user()
    bot.create_posts(auth_data=auth_data)

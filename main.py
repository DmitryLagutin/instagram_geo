from instabot import Bot
from pprint import pprint
import time

bot = Bot()
bot.login(username='dmitriipolkov4', password='123qweasdZXC')

# user_followers = bot.get_user_followers('instabotan')
# print(user_followers)
# user_following = bot.get_user_following('instabotan')
# print(user_following)
# print(bot.get_user_following(user_following[0]))

# media_link = 'https://www.instagram.com/p/CJQRFj4Jq1G/?utm_source=ig_web_copy_link'
# media_pk = bot.get_media_id_from_link(media_link)
# users_liked = bot.get_media_likers(media_pk)
# print(users_liked)
# users_commented = bot.get_media_commenters(media_pk)
# print(users_commented)
# comments = bot.get_media_comments(media_pk)
# pprint(comments)


twony_last_medias = bot.get_user_medias('mia_abstractiva', filtration=None)
print(len(twony_last_medias))
# pprint(twony_last_medias)
d = 0
for i in twony_last_medias:
    media_info = bot.get_media_info(i)[0]
    d = d + 1
    try:
        print(d)
        print(media_info['location']['name'])
        print(media_info['location']['lat'])
        print(media_info['location']['lng'])
    except Exception as ex:
        print("Ошибка")
    time.sleep(5)


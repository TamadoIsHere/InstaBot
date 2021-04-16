#this script make by tamado
from instapy import InstaPy

session = InstaPy(username = "USER NAME AKUN LU", password = "ISI PAKE PW AKUN LU JANGAN TAKUT KE HACK")
session.login()

session.set_relationship_bounds(enabled = True, max_followers = 200)

session.set_do_follow(True, percentage=100)
session.like_by_tags(["bmw", "steam"], amount = 3)
session.set_dont_like(["nsfw"])

session.end()
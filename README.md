# instagramBot
NOTE WAJIB PUNYA ```INSTAPY```
cara install? ```pip install instapy```
# How to use:
1. Open insta_bot.py in a text editor and edit Line 4 typing your instagram username and password.
2. Open terminal or cmd again and run bot using this command: ```python insta_bot.py```.


Cara unfollow semua yang kita ikutin gimana bang?

Edit ```insta_bot.py``` 
JADI KAYA DIBAWAH INI =

#this script make by tamado
from instapy import InstaPy

session = InstaPy(username = "USER NAME AKUN LU", password = "ISI PAKE PW AKUN LU JANGAN TAKUT KE HACK")
session.login()

#session.set_relationship_bounds(enabled = True, max_followers = 200)

#session.set_do_follow(True, percentage=100)
#session.like_by_tags(["bmw", "steam"], amount = 3)
#session.set_dont_like(["nsfw"])

session.unfollow_users(amount=10000, allFollowing=True, sleep_delay=60)
session.end()




#Untuk Cmd/Powershell/Gitbash
FOR PC CMD/POWERSHELL/GITBASH =
1.DOWNLOAD PYTHON DI ```python.org/downloads```
2.UNTUK WINDOWS =   ```https://www.python.org/ftp/python/3.9.4/python-3.9.4-amd64.exe```
4.DOWNLOAD GIT DI ```https://git-scm.com/```
5.GIT UNTUK WINDOWS = ```https://git-scm.com/download/win```
6.JALANIN FILE EXE DARI PYTHONNYA SAMPE SELESAI
7.JALANIN FILE EXE DARI GITNYA SAMPE SELESAI
8.BUKA CMD/POWERSHELL
9.Ketik = ```git clone https://github.com/TamadoIsHere/InstaBot```
10.NEXT cd InstaBot
11.NEXT dir
12.LALU python insta_bot.py



#TERMOS ES


BUAT HP
TERLEBIH TERMUX

1.apt-get install git && apt-get install python && apt-get install python2
2.CLONE REPOSITORY ```git clone https://github.com/TamadoIsHere/InstaBot```
3.NEXT cd InstaBot
4.NEXT ls
5.LALU python insta_bot.py

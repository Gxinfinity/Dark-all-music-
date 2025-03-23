import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

 

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "28427321"))
API_HASH = getenv("API_HASH", "1fb91d8a82d660980052d2ba53831231")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "7879372322:AAGavgYNjae5VCv2smunPyavJ2Njlqstds0")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Kirabot:Kirabot@cluster0.9zodk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT",100000))

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "100000")
)
# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002621328058"))

# Get this value from @Hot_Girl_Robot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "7290350162"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Gxinfinity/VenomMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/gxinfinity_support")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/infinitygx_bot_support")


AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", "false")
AUTO_SUGGESTION_TIME = int(
    getenv("AUTO_SUGGESTION_TIME", "5400"))
# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "5"))
# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @Venom_string_robot on Telegram
STRING1 = getenv("STRING_SESSION", "BQGxxDkAp-MtBOr1iYGOqi-XcCmr-DCN0VEpyN4f7lAcuKWIuP2e-1RxSpJ8yCJCmUFIeYLQSO0Nny44T7nmgWuDV4Dl8P898dNvS1oUxmz1iKSzwUJM5VLHZ9RYs4dBv5mTwyCljT03dlAwiPEyud5ebi8BbYENcfz5dGMh2RS4Z0pmy7m51Vv_rs_cmbU3i_cwk9x5bsC2wRLfIeSdYhSpEdncPc6-C9vzQoZrAHfEp3Ki3S70EhVJlvzRP0KAewKhJUYshtL-aWVac2nSQtYndRBR81ASI3vSJI4E0SeVmmB2fLMKJCRu8l6BKy5cHQZZSDKP-qoNyjPBK2LUf5RrWxOsrQAAAAGubcK3AA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
chatstats = {}
userstats = {}
clean = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/f3bdefba73d45f325dc15-78f9eb7cbb04e65aeb.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/66c98a8c0f021226c8f5c-b59746a1c10fc560e8.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/85a4fd2ab53ab8f4834c4-fa8668e98b19385789.jpg"
STATS_IMG_URL = "https://graph.org/file/d8adf15574e956a94b8c8-3121bcfd3808e55b35.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/d19f2060762d8ac8beeb9-27177d3a05ad58af31.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/d19f2060762d8ac8beeb9-27177d3a05ad58af31.jpg"
STREAM_IMG_URL = "https://graph.org/file/89d02f189eb06b9325055-878487305712939fab.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/89d02f189eb06b9325055-878487305712939fab.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/91eacbb41fb471e658dc4-1e95c38b0dcf53112d.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/b888fff9f579c1c91576e-186b1ba95730254397.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/b888fff9f579c1c91576e-186b1ba95730254397.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/b888fff9f579c1c91576e-186b1ba95730254397.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )

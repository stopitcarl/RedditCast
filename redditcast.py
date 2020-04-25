import pychromecast
import time
import sys
import praw
from prawcore.exceptions import BadRequest
import random
from vars import *

exts = ["jpg", "png"]
agent = "python:reddit-cast:v1.0.0"

def main():
    # Find and connect to chromecast
    casts = pychromecast.get_chromecasts()
    if len(casts) == 0:
        print("No chromecasts found in network")
        sys.exit(1)

    try:
        cast = next(cc for cc in casts if cc.device.friendly_name == castDeviceName)
    except StopIteration:
        print("Device not found")
        sys.exit(1)

    print ("Connected to " + cast.device.friendly_name)
    cast.start()

    if not cast.is_idle:
        print("Quitting current running app")
        cast.quit_app()
        time.sleep(5)

    cast.wait()

    # Connect to reddit and choose subreddit
    reddit = praw.Reddit(client_id=id, client_secret=secret, user_agent="android")
    if len(sys.argv) > 1:
        sub = reddit.subreddit(sys.argv[1])
    else:
        sub = reddit.subreddit(random.choice(subs))

    print("Using subreddit " + sub.display_name)

    try:
        print("Starting slideshow")
        for post in sub.hot():
            ext = post.url.split(".")[-1]
            if ext in exts:
                print("Casting: {} ({})".format(post.title, post.url))
                cast.play_media(post.url, "image/" + ext)
                time.sleep(timeout)
    except BadRequest:
        print("Error connecting to Reddit")

    except KeyboardInterrupt:
        pass

    cast.quit_app()
    print("Exiting")

if __name__ == "__main__":
    main()
            

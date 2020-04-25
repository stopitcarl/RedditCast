# RedditCast

A python program to cast images from a certain subreddit on to a google cast device. The subreddit is chosen at random from a user defined pool and the posts are picked from the "hot" tab. Currently supports png and jpg.

## Config

### Install requirements

```
$ pip install -r requirements.txt
```

### Edit configuration file

Rename ```example.vars.py``` to ```vars.py``` and edit the values accordingly. The *client\_id* and *client\_secret* can be obtained by registering an app on the [reddit app preferences page](https://www.reddit.com/prefs/apps).

## Usage

To start the program simply run it with python3:

```
$ python redditcast.py
```

You can also force it to use any other subreddit by supplying it as a command line argument:

```
$ python redditcast.py photos
```

Use CTRL-C to quit.
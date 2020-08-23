import os
import sys
import time
import tweepy

def limit_handled(items):
    while True:
        try:
            yield items.next()
        except tweepy.RateLimitError:
            print("  Rate limit reached. Sleeping for 15 minute...")
            time.sleep(15 * 60)
        except tweepy.error.TweepError:
            print("[ERROR]: Unable to access your Twitter Application. Please check your secrets.txt has valid up to date information.")
            sys.exit()
        except StopIteration:
            break

def readSecrets(path):
    prefs = {}
    for line in open(path, 'r'):
        try:
            # remove comments...
            index = line.find('#')
            if index >= 0:
                line = line[:index]

            key, val = line.split('=')
            key = key.strip()
            val = val.strip()
            prefs[key] = val
        except ValueError:
            continue
    return prefs

def oauthTwatter(secrets):
    auth = tweepy.OAuthHandler(str(secrets['consumer_key']), str(secrets['consumer_secret']))
    auth.set_access_token(str(secrets['access_token']), str(secrets['access_token_secret']))
    api = tweepy.API(auth)

    return api

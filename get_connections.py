#!/usr/bin/python

from ploofylib import *

def getTwitterConnections():
    for account_dir in [ f.path for f in os.scandir("accounts") if f.is_dir() ]:
        try:
            secrets = readSecrets(os.path.join(account_dir, 'secrets.txt'))
            api = oauthTwatter(secrets)
        except FileNotFoundError:
            continue

        me = api.me()
        print("Account '" + str(me.screen_name) + "':")

        followers_count = int(me.followers_count)
        friends_count = int(me.friends_count)

        print("  friends count   = " + str(friends_count))
        print("  followers count = " + str(followers_count))

        print("Retrieving friends list for '" + me.screen_name + "'...")
        try:
            fd = open(os.path.join(account_dir, 'friends.txt'), 'w')
            for friend in limit_handled(tweepy.Cursor(api.friends, screen_name = me.screen_name, count = 200).items()):
                fd.write(friend.screen_name + " = " + str(friend.id) + "\n" )
        except:
            print("[ERROR]: Unable to write friends list to friends.txt.")
            sys.exit()
        finally:
            fd.close()

        print("  Done")

        print("Retrieving followers list for '" + me.screen_name + "'...")
        try:
            fd = open(os.path.join(account_dir, 'followers.txt'), 'w')
            for follower in limit_handled(tweepy.Cursor(api.followers, screen_name = me.screen_name, count = 200).items()):
                fd.write(follower.screen_name + " = " + str(follower.id) + "\n" )
        except:
            print("[ERROR]: Unable to write followers list to followers.txt.")
            sys.exit()
        finally:
            fd.close()

        print("  Done")

getTwitterConnections()

import tweepy
import time
import sys
import yaml
from subprocess import check_output

with open('options.yaml') as yf:
    OP = yaml.load(yf.read())

auth = tweepy.OAuthHandler(OP['consumer-key'], OP['consumer-secret'])
auth.set_access_token(OP['access-key'], OP['access-secret'])
t = tweepy.API(auth)

while True:
    disk_usage = check_output('df -Bm | grep /dev/root | awk \'{print substr($3, 1, length($3)-1)"/"substr($2, 1, length($2)-1)}\'', shell=True).decode().strip()
    try:
        t.update_status('I\'m currently using {} blocks on my SD card.'.format(disk_usage))
    except tweepy.error.TweepError: # Duplicate status, usually
        print('Disk usage has not changed, skipping tweet.')
    time.sleep(60)
    ram_usage = check_output('free -h | grep "Mem:" | awk \'{print substr($3, 1, length($3)-1)"/"substr($2, 1, length($2)-1)}\'', shell=True).decode().strip()
    try:
        t.update_status('I\'m currently using {} MB of my system\'s RAM.'.format(ram_usage))
    except tweepy.error.TweepError: # Duplicate status, usually
        print('RAM usage has already been posted, skipping tweet.')
    time.sleep(60)

import tweepy
import time
import sys
import yaml
import subprocess

with open('options.yaml') as yf:
    OP = yaml.load(yf.read())

auth = tweepy.OAuthHandler(OP['consumer-key'], OP['consumer-secret'])
auth.set_access_token(OP['access-key'], OP['access-secret'])
t = tweepy.API(auth)

while True:
    disk_usage = subprocess.call('df -Bm | grep /dev/root | awk \'{print substr($3, 1, length($3)-1)"/"substr($2, 1, length($2)-1)}\'', shell=True).decode().strip()
    t.update_status('I\'m currently using {} blocks on my SD card.'.format(disk_usage))
    time.sleep(60)
    ram_usage = subprocess.call('free -h | grep "Mem:" | awk \'{print substr($3, 1, length($3)-1)"/"substr($2, 1, length($2)-1)}\'', shell=True).decode().strip()
    t.update_status('I\'m currently using {} MB of my system\'s RAM.'.format(ram_usage))
    time.sleep(60)

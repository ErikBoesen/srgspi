# Twitter bot
This is a simple bot to be run on a Raspberry Pi as an example.

## Setup
Rename or copy `options.yaml-example` to `options.yaml` and add your application credentials. If you need help creating an application for your bot, see [this article](https://dototot.com/how-to-write-a-twitter-bot-with-python-and-tweepy/).

Then run

```sh
pip3 install -r requirements.txt
```

to install the Python dependencies. You may need to run that command as root or append `--user` to the end to install for only your user.

## Running
Simply run the Python script:

```sh
python3 bot.py
```

## Licensing
This software was created by [Erik Boesen](https://github.com/ErikBoesen) and is licensed under the terms of the [MIT License](LICENSE).

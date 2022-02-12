# imports

from instapy import InstaPy
from instapy import smart_run
import random
import os
import json

# login credentials

with open(os.path.join('/code/secrets.json')) as secrets_file:
    secrets = json.load(secrets_file)

insta_username = secrets['USERNAME']
insta_password = secrets['PASSWORD']

# constants

hashtag_list = [
    'aktuality',
    'aktualne',
    'branislav',
    'brano',
    'bratislava',
    'fakty',
    'grohling',
    'info',
    'internat',
    'intrak',
    'intraklife',
    'intraky',
    'matovic',
    'maturanti',
    'maturita',
    'motivacia',
    'nedela',
    'novinky',
    'piatok',
    'politika',
    'pondelok',
    'praca',
    'premier',
    'prezidentka',
    'priroda',
    'protest',
    'refreshersk',
    'skola',
    'skolstvo',
    'sloboda',
    'slovakia',
    'slovaknature',
    'slovensko',
    'sobota',
    'spravy',
    'startitup',
    'streda',
    'studenti',
    'studenstskyzivot',
    'stvrtok',
    'teraz',
    'uni',
    'university',
    'univerzita',
    'univerzity',
    'utorok',
    'zomri',
    'zomriofficial',
    ]
location_list = [
    '213682323/bratislava-slovakia',
    '216965184/kosice-slovakia',
    '261698127/slovakia'
    ]
restricted_hashtag_list = [
    'dick',
    'squirt',
    'gay',
    'homo',
    '#fit',
    '#fitfam',
    '#fittips',
    '#abs',
    '#kids',
    '#children',
    '#child',
    '[nazi',
    'jew',
    'judaism',
    '[muslim',
    '[islam',
    'bangladesh',
    '[hijab',
    '[niqab',
    '[farright',
    '[rightwing',
    '#conservative',
    'death',
    'racist',
    ]
follow_users_list = [
    'aktuality_sk',
    'dennikn',
    'denniksme',
    'emefka_official',
    'nextech.magazin',
    'pravda.sk',
    'refreshersk',
    'rtvs_official',
    'startitup_sk',
    'tvjoj',
    'zomriofficial',
    ]

# login session

session = InstaPy(username=insta_username, password=insta_password,
                  headless_browser=True)

with smart_run(session):

    # shuffle lists

    random.shuffle(location_list)
    random.shuffle(hashtag_list)
    random.shuffle(follow_users_list)

    # settings

    session.set_quota_supervisor(
        enabled=True,
        sleep_after=['likes', 'follows', 'unfollows',
                     'server_calls_h'],
        sleepyhead=True,
        stochastic_flow=True,
        notify_me=False,
        peak_likes_hourly=40,
        peak_likes_daily=600,
        peak_follows_hourly=50,
        peak_follows_daily=500,
        peak_unfollows_hourly=48,
        peak_unfollows_daily=480,
        peak_server_calls_hourly=200,
        peak_server_calls_daily=5000,
        )
    session.set_relationship_bounds(
        enabled=True,
        potency_ratio=None,
        delimit_by_numbers=True,
        max_followers=250000,
        max_following=2000,
        min_followers=50,
        )
    session.set_action_delays(
        enabled=True,
        like=random.randrange(60,240,3),
        follow=random.randrange(60,240,3),
        unfollow=random.randrange(60,240,3),
        story=random.randrange(60,240,3),
        )
    session.set_skip_users(
        skip_private=True,
        skip_no_profile_pic=False,
        skip_business=False,
        skip_non_business=False
        )
    session.set_user_interact(
        amount=3,
        randomize=True,
        percentage=100,
        media='Photo'
        )
    session.interact_user_followers(follow_users_list, amount=10, randomize=True)
    session.set_simulation(enabled=True, percentage=70)
    session.set_mandatory_language(enabled=True, character_set=['LATIN'])
    session.set_do_like(enabled=True, percentage=100)
    session.set_dont_like(restricted_hashtag_list)
    session.set_do_reply_to_comments(enabled=False)
    session.set_do_comment(enabled=False)
    session.set_do_follow(enabled=True, percentage=25, times=1)
    session.set_dont_unfollow_active_users(enabled=True, posts=5)
    session.interact_user_followers(follow_users_list, amount=100)

    # like

    # session.like_by_tags(hashtag_list, amount=3, randomize=True)
    # session.like_by_locations(location_list, amount=3, randomize=True)

    # follow

    # session.follow_by_locations(location_list, amount=3, randomize=True)
    # session.follow_user_followers(follow_users_list, amount=3, randomize=True)

    # unfollow nonfollowers after one day

    session.unfollow_users(
        amount=random.randint(75, 100),
        nonFollowers=True,
        style='FIFO',
        unfollow_after=24 * 60 * 60,
        sleep_delay=(random.randrange(240,600,3))
        )

    # unfollow users after week to keep following list clean

    session.unfollow_users(
        amount=random.randint(75, 100),
        allFollowing=True,
        style='FIFO',
        unfollow_after=168 * 60 * 60,
        sleep_delay=(random.randrange(240,600,3))
        )
    
    # logout
    
    # session.end()

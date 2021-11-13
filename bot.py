# imports

from instapy import InstaPy
from instapy import smart_run
import random
import os
import json

# login credentials

with open(os.path.join('/home/ubuntu/instabot/secrets.json')) as secrets_file:
    secrets = json.load(secrets_file)

insta_username = secrets['USERNAME']
insta_password = secrets['PASSWORD']

# constants

comment_list = [
    u'Zodpovedný protest za univerzitné slobody 👨🏽‍🎓📚',
    u'Novela zákona nezvýši kvalitu vysokých škôl! 👩🏻‍🎓👨🏼‍🎓 Podpor akademickú slobodu podpísaním petície 🖋',
    u'⚠️ Sme proti novele vysokoškolského zákona obmedzujúcej akademické slobody! ⚠️',
    u'Zásadne odmietame predložený návrh novely vysokoškolského zákona, pretože obmedzuje akademické slobody a dáva nebezpečné právomoci politickým nominantom, ktorí by tak mohli úplne ovládnuť vysoké školy ⚠️',
    u'Nechceme návrat do obdobia spred roku 1989. 👨🏻‍🎓📚👩🏽‍🎓'
    ]
hashtag_list = [
    'refreshersk',
    'school',
    'zomri',
    'zomriofficial',
    'news',
    'newz',
    'day',
    'info',
    'study',
    'students',
    'fact',
    'startitup',
    'motivation',
    'slovakia',
    'politika',
    'skolstvo',
    'university',
    'uni',
    'univerzita',
    'univerzity',
    'slovensko',
    'bratislava',
    'praca',
    'work',
    'worklife',
    'pondelok',
    'utorok',
    'streda',
    'stvrtok',
    'piatok',
    'sobota',
    'nedela',
    'slovaknature',
    'priroda',
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
    'zomriofficial',
    'refreshersk',
    'startitup_sk',
    'stubratislava',
    'comenius.university',
    'fiit_nowadays',
    'srvs.eu',
    'emefka_official',
    'rtvs_official',
    'tvjoj',
    'denniksme',
    'dennikn'
    ]

# login session

session = InstaPy(username=insta_username, password=insta_password,
                  headless_browser=True)

with smart_run(session):

    # settings

    session.set_quota_supervisor(
        enabled=True,
        sleep_after=['likes', 'comments_d', 'follows', 'unfollows',
                     'server_calls_h'],
        sleepyhead=True,
        stochastic_flow=True,
        notify_me=True,
        peak_likes_hourly=60,
        peak_likes_daily=600,
        peak_comments_hourly=20,
        peak_comments_daily=200,
        peak_follows_hourly=50,
        peak_follows_daily=500,
        peak_unfollows_hourly=48,
        peak_unfollows_daily=480,
        peak_server_calls_hourly=500,
        peak_server_calls_daily=5000,
        )
    session.set_relationship_bounds(
        enabled=True,
        potency_ratio=None,
        delimit_by_numbers=True,
        max_followers=500000,
        max_following=2000,
        min_followers=100,
        min_following=50,
        )
    session.set_skip_users(skip_private=True, skip_no_profile_pic=True,
                           skip_business=False, skip_non_business=False)
    session.set_user_interact(amount=3, randomize=True, percentage=80,
                              media='Photo')
    session.interact_user_followers(follow_users_list, amount=10,
                                    randomize=True)
    session.set_simulation(enabled=False)
    session.set_mandatory_language(enabled=True, character_set=['LATIN'
                                   ])
    # session.set_smart_hashtags(smart_hashtag_list, limit=3, sort='top',
    #                            log_tags=True)
    # session.set_smart_location_hashtags(location_list, radius=60,
    #         limit=5)
    session.set_do_like(enabled=True, percentage=90)
    session.set_dont_like(restricted_hashtag_list)
    session.set_delimit_commenting(enabled=True, max_comments=6000,
                                   min_comments=5)
    session.set_do_reply_to_comments(enabled=False)
    session.set_do_comment(enabled=True, percentage=35)
    session.set_do_follow(enabled=True, percentage=40, times=1)
    session.set_dont_unfollow_active_users(enabled=True, posts=5)

    # like

    session.like_by_tags(hashtag_list, amount=10)
    session.like_by_locations(location_list, amount=40)

    # comment

    session.comment_by_locations(location_list, amount=20)

    # follow

    session.follow_by_locations(location_list, amount=50)
    session.follow_user_followers(follow_users_list, amount=10,
                                  randomize=True)

    # unfollow nonfollowers after one day

    session.unfollow_users(amount=random.randint(75, 100),
                           nonFollowers=True, style='FIFO',
                           unfollow_after=24 * 60 * 60, sleep_delay=600)

    # unfollow users after week to keep following list clean

    session.unfollow_users(amount=random.randint(75, 100),
                           allFollowing=True, style='FIFO',
                           unfollow_after=168 * 60 * 60,
                           sleep_delay=600)
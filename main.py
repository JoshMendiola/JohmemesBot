import random

from instagrapi import Client
hashtag = ["programming", "music"]
comments = ["this is cool !!!", "this is neat!!!", "wow!!!"]
client = Client()


def login():
    with open("credentials.txt", "r") as f:
        username, password = f.read().splitlines()
    client.login(username, password)


def like_hashtags_and_follow():
    medias = client.hashtag_medias_recent(hashtag, 20)
    for i, media in enumerate(medias):
        print(f"Liked post number {i} of hashtag {hashtag}")
        if i % 5 == 0:
            client.user_follow(media.user.pk)
            print(f"Followed user {media.user.username}")
            comment = random.choice(comments)
            client.media_comment(media.id, comment)
            print(f"Commented {comment} under post number {i + 5}")


if __name__ == '__main__':
    login()
    like_hashtags_and_follow()


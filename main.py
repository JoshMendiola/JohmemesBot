import random
from instagrapi import Client
from instagrapi.types import Usertag, Location

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


def post_content():
    tagged_user = client.user_info_by_username("luna.supern0va")
    media = client.photo_upload(
        path="photos/testimage.jpg",
        caption="free me :(",
        usertags=[Usertag(user=tagged_user, x=0.5, y=0.5)],
        location=Location(name="Austin, Texas", lat= 30.22797618972211, lng=-97.75483341792386)
    )


if __name__ == '__main__':
    login()
    post_content()


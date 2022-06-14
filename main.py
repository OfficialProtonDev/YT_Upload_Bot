from youtubeBot import YoutubeBot


def main():
    email = "REPLACE_ME"
    password = "REPLACE_ME"
    vid_path = r"REPLACE_ME"
    vid_title = "REPLACE_ME"
    vid_desc = "REPLACE_ME"
    loops = 1

    bot = YoutubeBot(email, password, vid_path, vid_title, vid_desc, loops)
    bot.upload_videos()


if __name__ == '__main__':
    main()

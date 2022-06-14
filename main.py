from youtubeBot import YoutubeBot


def main():
    email = "REPLACE_ME"
    password = "REPLACE_ME"
    vid_path = "REPLACE_ME"
    vid_title = "REPLACE_ME"
    vid_desc = "REPLACE_ME"
    loops = 1

    bot = YoutubeBot()
    bot.upload_videos()


if __name__ == '__main__':
    main()

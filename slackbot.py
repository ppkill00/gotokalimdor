import os
import slack

# slack_token = os.environ["SLACK_API_TOKEN"]
slack_token = os.environ['SLACK_API_KEY']
client = slack.WebClient(token=slack_token)


def sendImgtoSlack(path,comment):
    client.files_upload(
        channels='wow',
        file=path,
        title=comment
    )

def sendTexttoSlack(text):
    client.chat_meMessage(
        channel='wow',
        text = text
    )


# client.chat_meMessage(
#   channel="wow",
#   text="Hello silently from your app! :tada:",
# )
# client.files_upload(
#     channels='wow',
#     file='./images/1909222008_r.png',
#     title='test upload'
# )
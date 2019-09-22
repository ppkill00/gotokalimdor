import os
import slack

# slack_token = os.environ["SLACK_API_TOKEN"]
slack_token ='xoxp-736925152993-743310759888-756237343378-ab90a2f5843f7b7e669a52df1032abe0'
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
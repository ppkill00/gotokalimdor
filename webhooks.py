import requests, os, json,time
import logging

logger = logging.getLogger('automatorLogger') 

headers = {'Contents-Type':'application/json','Accept':'application/json'}
url  = os.environ['SLACK_WEBHOOK_WOW']

def webhook(data,status,err):
    payload={"text": str(time.strftime('%y.%m.%d. %H:%M:%S'))+" :  : Message : " + str(data), "channel": "#wow"}
    #print(payload)
    resp = requests.post(url,data=json.dumps(payload),headers=headers)
    if resp.status_code !=200:
        logger.error('error : ' + str(resp.status_code))

# event = {'a' : 'test1','b':'test2'}

# if event['a'] == None or event['b'] == None:
#         print('asdf')
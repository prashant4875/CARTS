import json


def hello(event, context):
    # user_id = event["params"]["querystring"]["userid"]
    # activity_id = event["params"]["querystring"]["activityid"]
    # print(event)
    u = int(event['userid'])
    a = int(event['activityid'])

    if u==1 and a==2:
        return {
            'name': "CARTS",
            'company': "WM"
        }
    
    else: 
        return {
            'ui': u,
            'ai': a,
            'name': "other",
            'company': "other1"
        }

    # body = {
    #     "id": 1,
    #     "message": "Go Serverless v2.0! Your function executed successfully!",
    #     "input": event,
    # }

    # return {
    #         "userid": 2,
    #         "start_date": 2
            
    #         }


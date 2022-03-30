import json
from dateutil.parser import parse
from datetime import timedelta
#from functions.common.carts.cache import get_hauling_site_by_code

print("Loading AWS Lambda Function")
def hello(**kwargs):
    # load parameters form the path or the querystring
    hauling_site_code = kwargs['columns']['id']
    #hauling_site_id = get_hauling_site_by_code(hauling_site_code)['id']
    hauling_site_id = 340
    needed_start_date = parse(kwargs['event']['query']['start_date'])
    needed_end_date = parse(kwargs['event']['query']['end_date'])
    needed_quantity = int(kwargs['event']['query']['quantity'])
    volume = f"{kwargs['event']['query']['volume']} YD"
    container_type = kwargs['event']['query']['container_type']

    #for k,w in kwargs.items():
    #    print(k,w)


    # Printing the values
    # print('hauling_site_code=' + hauling_site_code)
    # print('hauling_site_id=' + hauling_site_id)
    # print('needed_start_date=' + needed_start_date)
    # print('needed_end_date=' + needed_end_date)
    # print('needed_quantity=' + needed_quantity)
    # print('volume=' + volume)
    # print('container_type=' + container_type)

    # Body of Response Object
    # records = {}
    # records['hauling_site_code'] = hauling_site_code
    # records['hauling_site_id'] = hauling_site_id
    # records['needed_start_date'] = needed_start_date
    # records['needed_end_date'] = needed_end_date
    # records['needed_quantity'] = needed_quantity
    # records['volume'] = volume
    # records['container_type'] = container_type
    records = []
    dummy_var = 3 #mahender 
    while needed_start_date <= needed_end_date:
        new_record = {'date': needed_start_date.strftime('%Y-%m-%d'), 'hauling_site_code': hauling_site_code,
                          'hauling_site_id': hauling_site_id, 'container_type': container_type, 'volume': volume,
                          'quantity': needed_quantity}
        
        if dummy_var%2 == 0:
            new_record['available'] = True
        else:
            new_record['available'] = False

        dummy_var+= 1
        records.append(new_record)

        needed_start_date += timedelta(1)
    #http response object

    return records





# def hello(event, context):
#     # user_id = event["params"]["querystring"]["userid"]
#     # activity_id = event["params"]["querystring"]["activityid"]
#     # print(event)
#     u = int(event['userid'])
#     a = int(event['activityid'])

#     if u==1 and a==2:
#         return {
#             'name': "CARTS",
#             'company': "WM"
#         }
    
#     else: 
#         return {
#             'ui': u,
#             'ai': a,
#             'name': "other",
#             'company': "other1"
#         }

    # body = {
    #     "id": 1,
    #     "message": "Go Serverless v2.0! Your function executed successfully!",
    #     "input": event,
    # }

    # return {
    #         "userid": 2,
    #         "start_date": 2
            
    #         }


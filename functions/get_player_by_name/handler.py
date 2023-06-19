from functions.get_player_by_name.index import get_player_by_name
import json

def handler(event, _):
    try:
        player_name =  event['pathParameters']['player_name']
    except KeyError as e:
        body = json.dumps({"message": "missing player_name"})
        return {
            "statusCode": 400,
            "body": body
        }
    player_results = get_player_by_name(player_name)
    if len(player_results) == 0:
        response = {
            "data": player_results,
            "statusCode": 404
        }
    else:
        response = player_results
    return response

import apiai
import json
import vk_api
import time
import random

# def send_message(message):
#     request = apiai.ApiAI("3d1433a96dfb415193456ebc0c61713c").text_request()
#     request.lang = "en"
#     request.session_id = "session_1"
#     request.query = message
#     response = json.loads(request.getresponse().read().decode('utf-8'))
#     print(response['result']['fulfillment']['speech'])
#     return response['result']['action']
#
#
# print('Input your message or type exit: ')
# message = input()
# action = None
# while True:
#     action = send_message(message)
#     if action == 'smalltalk.greetings.bye':
#         break
#     message = input()

# --------------------------------------------------------------------------
# def send_message(message):
#     request = apiai.ApiAI("3d1433a96dfb415193456ebc0c61713c").text_request()
#     request.lang = "en"
#     request.session_id = "session_1"
#     request.query = message
#     response = json.loads(request.getresponse().read().decode('utf-8'))
#     print(response['result']['fulfillment']['speech'])
#     return response['result']['action']
#
#
# print('Input your message or type exit: ')
# message = input()
# while True:
#     send_message(message)
#     message = input()

# --------------------------------------------------------------------------

# request = apiai.ApiAI("3d1433a96dfb415193456ebc0c61713c").text_request()
# request.lang = "en"
# request.session_id = "session_1"
# request.query = message
# response = json.loads(request.getresponse().read().decode('utf-8'))
# print(response['result']['fulfillment']['speech'])

token = "5b86f731421492463e1781a18de370ec6622d87db285da0aa314d1815c2914516d6b5e349880671ba54a5"

vk = vk_api.VkApi(token=token)

vk._auth_token()

# print('Input your message or type exit: ')
# message = input()
# while True:
#     request = apiai.ApiAI("3d1433a96dfb415193456ebc0c61713c").text_request()
#     request.lang = "en"
#     request.session_id = "session_1"
#     request.query = message
#     response = json.loads(request.getresponse().read().decode('utf-8'))
#     print(response['result']['fulfillment']['speech'])
#     message = input()

while True:
    # request = apiai.ApiAI("3d1433a96dfb415193456ebc0c61713c").text_request()
    # request.lang = "en"
    # request.session_id = "session_1"
    # request.query = message
    # response = json.loads(request.getresponse().read().decode('utf-8'))
    # print(response['result']['fulfillment']['speech'])
    # message = input()
    try:
        request = apiai.ApiAI("3d1433a96dfb415193456ebc0c61713c").text_request()
        request.lang = "en"
        request.session_id = "session_1"
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]
            request.query = body.lower()
            response = json.loads(request.getresponse().read().decode('utf-8'))
            vk.method("messages.send",
                      {"peer_id": id, "message": response['result']['fulfillment']['speech'], "random_id": random.randint(1, 2147483647)})

            # if body.lower().__contains__("привет"):
            #     vk.method("messages.send",
            #               {"peer_id": id, "message": "Привет!", "random_id": random.randint(1, 2147483647)})
            # elif body.lower() == "я не подписан на канал":
            #     vk.method("messages.send",
            #               {"peer_id": id, "message": "А ну быстро подписался!", "random_id": random.randint(1, 2147483647)})
            # else:
            #     vk.method("messages.send",
            #               {"peer_id": id, "message": "Не понял тебя!", "random_id": random.randint(1, 2147483647)})
    except Exception as E:
        time.sleep(1)
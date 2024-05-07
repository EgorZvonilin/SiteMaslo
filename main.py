# import vk_api
# import course
#
# token = 'vk1.a.9fGW8iV6HlEbvMZWOfZWZUW9v1Uc5FB1aKuoOsi0z_tEI87RL3EEuq_dZ7XpVgH0EfEB1nJHhoX5ldmnyrf4O5jYnMFpYAzMGzSoqcJVYJHGy21TQzqRdEjJrPOminZilwf__8z8_CAdP1KtCjCLyllFfmMo-EB7RaMwbCC1XrDvWSuB52XK8u8-AbqQAsCt8bILrePzjlZbU35DCxhwWg'
#
# vk = vk_api.VkApi(token=token)
#
# messages = vk.method('messages.getConversations', {'count': 20, 'filters': 'unanswered'})
#
# # print(messages['items'][0]['last_message']['text'])
# #
# # user_id = messages['items'][0]['last_message']['from_id']
# # message_id = messages['items'][0]['last_message']['id']
# #
# # vk.method('messages.send', {'peer_id': user_id, 'random_id': message_id, 'message': 'Привет! Я бот, который скоро будет уметь делать много всего!'})
#
# while True:
#     messages = vk.method('messages.getConversations', {'count': 20, 'filter': 'unanswered'})
#     if messages['count'] >= 1:
#         print(messages)
#         user_id = messages['items'][0]['last_message']['from_id']
#         message_id = messages['items'][0]['last_message']['id']
#         message_text = messages['items'][0]['last_message']['text']
#         if message_text.lower() == 'привет':
#             vk.method('messages.send', {'peer_id': user_id, 'random_id': message_id,
#                                         'message': 'Привет! Я бот, который скоро будет уметь делать много всего!'})
#
#         elif message_text.lower() == 'курс':
#             vk.method('messages.send', {'peer_id': user_id, 'random_id': message_id,
#                                         'message': course.get_course('R01235')})
#
#         elif message_text.lower() == 'пока':
#             vk.method('messages.send', {'peer_id': user_id, 'random_id': message_id,
#                                         'message': 'До скорых встреч!'})
#
#         else:
#             vk.method('messages.send', {'peer_id': user_id, 'random_id': message_id,
#                                         'message': 'Я тебя не понимаю :('})



import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from course import get_course

token = 'vk1.a.9fGW8iV6HlEbvMZWOfZWZUW9v1Uc5FB1aKuoOsi0z_tEI87RL3EEuq_dZ7XpVgH0EfEB1nJHhoX5ldmnyrf4O5jYnMFpYAzMGzSoqcJVYJHGy21TQzqRdEjJrPOminZilwf__8z8_CAdP1KtCjCLyllFfmMo-EB7RaMwbCC1XrDvWSuB52XK8u8-AbqQAsCt8bILrePzjlZbU35DCxhwWg'

vk = vk_api.VkApi(token=token)
vk2 = vk.get_api()

longpoll = VkLongPoll(vk)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        msg = event.text
        user_id = event.user_id
        msg_id = event.message_id
        message = 'Привет! Как дела?'
        message2 = 'До скорых встреч!'
        if msg.lower() == 'привет':
            vk2.messages.send(user_id=user_id, random_id=msg_id, message=message)
        elif msg.lower() == 'курс':
            message = f'{get_course("R01235")} рублей на 1 доллар'
            vk2.messages.send(user_id=user_id, random_id=msg_id, message=message)
        elif msg.lower() == 'пока':
            vk2.messages.send(user_id=user_id, random_id=msg_id, message=message2)
        else:
            vk2.messages.send(user_id=user_id, random_id=msg_id, message='Я тебя не понимаю')
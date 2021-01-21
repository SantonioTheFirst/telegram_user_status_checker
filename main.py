from telethon import TelegramClient
from telethon import types
from datetime import datetime
import time
from phone_numbers import * # phone numbers, api_id and api_hash


client = TelegramClient('check', api_id, api_hash)

async def check(count : int):
    file = open('data.csv', 'w')
    file.write('ID;User_1;Was_online_1;User_2;Was_online_2;time\n')
    for i in range(count):
        start = datetime.now()
        user_1 = await client.get_entity(number1)
        user_2 = await client.get_entity(number2)
        if isinstance(user_1.status, types.UserStatusOnline):
            u1 = 1
            u1_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S+00:00')
        else:
            u1 = 0
            u1_time = user_1.status.was_online
        if isinstance(user_2.status, types.UserStatusOnline):
            u2 = 1
            u2_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S+00:00')
        else:
            u2 = 0
            u2_time = user_2.status.was_online
        file.write('{0};{1};{2};{3};{4};{5}\n'.format(i, u1, u1_time, u2, u2_time, datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S+00:00')))
        print(i, datetime.now() - start)
        if i != count - 1:
            time.sleep(10)
    file.close()


if __name__ == '__main__':
    count = int(input())
    with client:
        client.loop.run_until_complete(check(count))

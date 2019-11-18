from telethon import TelegramClient
from telethon import types
from datetime import datetime
import time
from numbers import *

api_id = 
api_hash = ""

client = TelegramClient("ananas4", api_id, api_hash)

async def check():
    counter = 0
    f = open('online.csv', 'w')
    f.write('\tID     \tUSER1     \tUSER2' + '\n')
    while counter in range(0,500):
        user_h = await client.get_entity(number1)
        user_d = await client.get_entity(number2)
        if isinstance(user_h.status, types.UserStatusOnline):
            if isinstance(user_d.status, types.UserStatusOnline):
                print(datetime.time(datetime.now()).strftime("%H:%M:%S"))
                print(datetime.time(datetime.now()).strftime("%H:%M:%S"))
                print('------------------------------------------------')
                counter += 1
                f.write('\t' + str(counter) + '     ' + str(datetime.time(datetime.now()).strftime("%H:%M:%S")) + '     ' + str(datetime.time(datetime.now()).strftime("%H:%M:%S")) + '\n')
                #print(str(user_h.status.expires.hour + 2) + ':' + str(user_h.status.expires.minute) + ':' + str(user_h.status.expires.second))
                #print(str(user_d.status.expires.hour + 2) + ':' + str(user_d.status.expires.minute) + ':' + str(user_d.status.expires.second))
            else:
                print(datetime.time(datetime.now()).strftime("%H:%M:%S"))
                #print(str(user_h.status.expires.hour + 2) + ':' + str(user_h.status.expires.minute) + ':' + str(user_h.status.expires.second))
                print(str(user_d.status.was_online.hour + 2) + ':' + str(user_d.status.was_online.minute) + ':' + str(user_d.status.was_online.second))
                print('------------------------------------------------')
                counter += 1
                f.write('\t' + str(counter) + '     ' + str(datetime.time(datetime.now()).strftime("%H:%M:%S")) + '     ' + str(user_d.status.was_online.hour + 2) + ':' + str(user_d.status.was_online.minute) + ':' + str(user_d.status.was_online.second) + '\n')
        elif isinstance(user_h.status, types.UserStatusOffline):
            if isinstance(user_d.status, types.UserStatusOnline):
                print(str(user_h.status.was_online.hour + 2) + ':' + str(user_h.status.was_online.minute) + ':' + str(user_h.status.was_online.second))
                print(datetime.time(datetime.now()).strftime("%H:%M:%S"))
                print('------------------------------------------------')
                counter += 1
                f.write('\t' + str(counter) + '     ' + str(user_h.status.was_online.hour + 2) + ':' + str(user_h.status.was_online.minute) + ':' + str(user_h.status.was_online.second) + '     ' + str(datetime.time(datetime.now()).strftime("%H:%M:%S")) + '\n')
                #print(str(user_d.status.expires.hour + 2) + ':' + str(user_d.status.expires.minute) + ':' + str(user_d.status.expires.second))
            else:
                #print(datetime.time(datetime.now()).strftime("%H:%M:%S"))
                print('Offline')
                print(str(user_h.status.was_online.hour + 2) + ':' + str(user_h.status.was_online.minute) + ':' + str(user_h.status.was_online.second))
                print(str(user_d.status.was_online.hour + 2) + ':' + str(user_d.status.was_online.minute) + ':' + str(user_d.status.was_online.second))
                print('------------------------------------------------')
                #counter += 1
                #f.write('\t' + str(counter) + '     ' + str(user_h.status.was_online.hour + 2) + ':' + str(user_h.status.was_online.minute) + ':' + str(user_h.status.was_online.second) + '     ' + str(user_d.status.was_online.hour + 2) + ':' + str(user_d.status.was_online.minute) + ':' + str(user_d.status.was_online.second) + '\n')
        print(counter)
        time.sleep(0.5)
    f.close()

with client:
    client.loop.run_until_complete(check())

import requests
import json
import sched
import os

from dotenv import load_dotenv
from discord.ext import commands, tasks
from datetime import datetime

# misc variables
load_dotenv()
START_DATE = datetime.today().strftime('%Y-%m-%d')
END_DATE = '2023-12-22'
# END_DATE = '2024-1-9'
printed_times = []
count = -1

bot = commands.Bot(command_prefix='!', intents=None)

url = 'https://us.booksy.com/core/v2/customer_api/me/businesses/623412/appointments/time_slots'
payload = {
    "subbookings": [
        {
            "service_variant_id": 12105956,
            "staffer_id": 531701,
            "combo_children": []
        }
    ],
    "start_date": START_DATE,
    "end_date": END_DATE
}
headers = {
    'authority':'us.booksy.com',
    'method':'POST',
    'path':'/core/v2/customer_api/me/businesses/623412/appointments/time_slots',
    'scheme':'https',
    'Accept':'application/json, text/plain, */*',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'en',
    'Cache-Control':'no-cache',
    'Content-Length':'139',
    'Content-Type':'application/json',
    'Origin':'https://booksy.com',
    'Pragma':'no cache',
    'Referer':'https://booksy.com/',
    'Sec-Ch-Ua':'"Not_A Brand";v="8", "Chromium";v="120", "Brave";v="120"',
    'Sec-Ch-Ua-Mobile':'?0',
    'Sec-Ch-Ua-Platform':'"Windows"',
    'Sec-Fetch-Dest':'empty',
    'Sec-Fetch-Mode':'cors',
    'Sec-Fetch-Site':'same-site',
    'Sec-Gpc':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'X-Access-Token':'v4607mry75sy2unwi6os84u6kcb01soa',
    'X-Api-Key':'web-e3d812bf-d7a2-445d-ab38-55589ae6a121',
    'X-App-Version':'3.0',
    'X-Fingerprint':'c9e36b03-7237-4143-8a2c-a85ce7374555'
}

@tasks.loop(seconds=5)
async def get_times_in_date_range():
    # get data
    r = requests.post(url, json=payload, headers=headers)
    response_json = json.loads(r.text)
    time_slots = response_json['time_slots']

    # iterate through response for new times listed
    for time_slot in time_slots:
        date = time_slot['date']
        for t in time_slot['slots']:
            time = t['t']
            full_time = f'{date} {time}'
            full_time_obj = datetime.strptime(full_time, '%Y-%m-%d %H:%M')
            formatted_time = full_time_obj.strftime('%m-%d-%Y %I:%M %p')

            if formatted_time not in printed_times:
                print(f'Availability at: {formatted_time}')
                printed_times.append(formatted_time)

                # discord notification
                user = await bot.fetch_user(os.getenv('DISCORD_USER'))
                await user.send(f'Availability at - {formatted_time}')
    
    # iterate count and print info
    global count
    count += 1
    if count % 10 == 0:
        print(f'\niteration: {count}')
        print(f'response code: {r.status_code}\n')
    
@bot.event
async def on_ready():
    print('bot successfully started')
    get_times_in_date_range.start()

bot.run(os.getenv('TOKEN'))
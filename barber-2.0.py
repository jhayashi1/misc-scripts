from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from datetime import datetime

import sched
import time


req_url = 'https://booksy.com/en-us/623412_side-part-seth-cash-only_barber-shop_17558_des-moines'
# req_headers = {
#     'Sec-Ch-Ua': 'Not_A Brand;v=8, Chromium;v=120, Brave;v=120',
#     'Sec-Ch-Ua-Mobile' : '?0',
#     'Sec-Ch-Ua-Platform' : 'Windows',
#     'Upgrade-Insecure-Requests' : '1',
#     'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
# }

driver = webdriver.Chrome('C:/Users/JaredNew/Desktop/chromedriver.exe')
driver.get(req_url)
element = driver.find_element(By.ID, 'service-3960308')

# def print_earliest_time(runnable_task):
#     # schedule next task
#     runnable_task.enter(300, 1, print_earliest_time, (runnable_task,))

#     # request
#     r = requests.get(req_url, headers=req_headers)
#     data = r.json()['d'].pop()
#     # print(data)

#     # get important data
#     d = data["AppDate"]
#     t = datetime.strptime(d + " " + data["AvailableTime"], "%d %b %Y %I:%M %p")
#     p = data["ServicepPoviderData"].pop()["ServiceProviderName"]

#     if t.hour == 12 and t.month == 1 and t.day <= 31:
#         print(p + " is available on " + d +
#               " at " + str(t.strftime("%I:%M %p")))


# task = sched.scheduler(time.time, time.sleep)
# task.enter(300, 1, print_earliest_time, (task,))
# task.run()

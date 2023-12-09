import requests
from datetime import datetime
import sched, time

URL = "https://www.vagaro.com/us04/websiteapi/homepage/getavailablemultiappointments"
payload = {
    "lAppointmentID": "",
    "businessID": "169310",
    "csvServiceID": "16577632",
    "csvSPID": "88135106-88167896",
    "AppDate": "Wed Jan-18-2023",
    "StyleID": "null",
    "isPublic": "true",
    "isOutcallAppointment": "false",
    "strCurrencySymbol": "$",
    "IsFromWidgetPage": "false",
    "isFromShopAdmin": "false",
    "isMoveBack": "false",
    "BusinessPackageID": 0,
    "PromotionID": ""
}

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.7",
    "brandedApp": "false",
    "Connection": "keep-alive",
    "Content-Length": "320",
    "Content-Type": "application/json; charset=UTF-8",
    "Cookie": "proximitystate_v3=%7B%22lat%22%3A%2242.03%22%2C%22long%22%3A%22-93.5905%22%2C%22countryid%22%3A%221%22%2C%22zip%22%3A%2250010%22%2C%22city%22%3A%22Ames%22%2C%22state%22%3A%22Iowa%22%2C%22stateName%22%3A%22IA%22%2C%22currencysymbol%22%3A%22%22%2C%22businesstypes%22%3A%22%22%2C%22service%22%3A%22%22%2C%22vagaroURL%22%3A%22%22%2C%22titleTimesTamp%22%3A%22%22%2C%22utcOffset%22%3A0%2C%22timeZoneOffSet%22%3A-6.0%2C%22isSupportDayLight%22%3Atrue%7D; vPowerV2=bqoruryp13qyxe0ur5kakj5e; tenant_group=us04; visid_incap_451694=Q1Sx16xGQJau3iDH4JmKGiVEs2MAAAAAQUIPAAAAAACr9YZiZAq4ckSYY6iUBgxG; CustomizableBusinessID=bUQmhzcejnmc8Tr+EvVTxA==; incap_ses_515_451694=SvylZFoJvijgNPa9lKYlB26iyGMAAAAA+9bpSIrOuCu3kW4PRI3efw==; reese84=3:45eoupFRIYsM6ZWl44aqaw==:9reBYh5go+Sdnp1MTeLncoRd5V5hG1Nv/2wg8DV28+sQDsVX+CVumYXDVyXbmmpCLVmteNMhUSru+GXGjyPj7iQgK7sdwBwuBOzsPMEmtxjYNV0UNJIcG2fHlam9f/+r6tdcqYX/ZmY+0r61FjE0pMCIYlCfcX0fpzeQ4Q03SsUZ8TY9UKjuZNGTNx1Hq68HEBnhKtoZnzg8d7PELBi7pbVIFAOak4a0eEj4dG1wfIyRkyzKkgow7jKfWL/3wvr/ZwhGLaDN0BVFA/JMZ31ysHVcSfyIDUJ6T7rOGOA2pLZA0tseToUAW2heaymAwdBwywVEHgxQyz0b3XQ3tbdm12lAA0cms6EOGC3WlulR7r7JtH1vAgsFhmH3Tb+VZ83frMjmWbzEtX9HGZrBdRXrLlcVgT7YPnU+kNi+g47DnCYgqlEY0dGLRCC3nsSpgfz7U++c8DHQa30D+sE8d/ysq9l/6HT+zgSk9iH3Y94Ttqz9KMj1sKISIzWx4bjXRZ8s:o2YvNaOM2MLPjaClyFF33iz4wUHdBIaNjBWrTM7pw/8=",
    "grouptoken": "US04",
    "Host": "www.vagaro.com",
    "Origin": "https://www.vagaro.com",
    "Referer": "https://www.vagaro.com/thegroomroom3/book-now",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Sec-GPC": "1",
    "token2": "kVCBX8HKoZnxJoS6vzWtkm",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}

def print_earliest_time(runnable_task):
    # schedule next task
    runnable_task.enter(300, 1, print_earliest_time, (runnable_task,))
    
    # request
    r = requests.post(URL, json = payload, headers=headers)
    data = r.json()['d'].pop()
    # print(data)

    # get important data
    d = data["AppDate"]
    t = datetime.strptime(d + " " + data["AvailableTime"], "%d %b %Y %I:%M %p")
    p = data["ServicepPoviderData"].pop()["ServiceProviderName"]

    if t.hour == 12 and t.month == 1 and t.day <= 31:
        print(p + " is available on " + d + " at " + str(t.strftime("%I:%M %p")))

task = sched.scheduler(time.time, time.sleep)
task.enter(300, 1, print_earliest_time, (task,))
task.run()
import discord
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
import json


class MyClient(discord.Client):
    async def on_ready(self):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        driver = webdriver.Chrome("C:\Program Files (x86)\PY_DRIVERS\chromedriver.exe", options=options)

        while True:
            dic_a = {}
            dic_b = {}
            print("start new run")
            driver.get("https://earth2stats.net/api/get_countries")
            print("searching a")
            data_a = driver.find_element_by_xpath("/html/body/pre")
            dic_a = json.loads(data_a.text)
            print(dic_a)
            same = True
            while same:
                print("searching b")
                driver.get("https://earth2stats.net/api/get_countries")
                data_b = driver.find_element_by_xpath("/html/body/pre")
                dic_b = json.loads(data_b.text)
                if dic_a != dic_b:
                    print(dic_b)
                    print("got different dic b")
                    same = False
                else:
                    time.sleep(0.5)

            for i in range(len(dic_a)):
                if dic_a[i] != dic_b[i] and int(dic_a[i]["sold_tiles"]) < 2000:
                    print("found something")
                    channel = client.get_channel(channel-id)
                    await channel.send(f"<@&796062627926245397> Es wurden Gebite in {dic_a[i]['name']} verkauft")
                else:
                    print("found nothing")

    async def on_message(self, message):
        if message.content.startswith("§display"):
            print(message)
            await message.channel.send("bot is running")

client = MyClient()
client.run("Nzk1ODc1ODkwOTgyNDIwNDgw.X_PvLw.bgGHZN3c9CWIU7zeYTtmO9nUYtQ")

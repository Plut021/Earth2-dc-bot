import discord
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import json
import time


class MyClient(discord.Client):
    async def on_ready(self):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        driver = webdriver.Chrome("C:\Program Files (x86)\PY_DRIVERS\chromedriver.exe", options=options)

        while True:
            dic_a = {}
            dic_b = {}
            not_a = True
            while not_a:
                driver.get("https://earth2stats.net/api/get_countries")
                try:
                    driver.find_element_by_xpath("/html/body/pre")
                    data_a = driver.find_element_by_xpath("/html/body/pre")
                    not_a = False
                except():
                    time.sleep(1)

            dic_a = json.loads(data_a.text)
            same = True
            while same:
                time.sleep(1)
                not_b = True
                while not_b:
                    driver.get("https://earth2stats.net/api/get_countries")
                    try:
                        driver.find_element_by_xpath("/html/body/pre")
                        data_b = driver.find_element_by_xpath("/html/body/pre")
                        not_b = False
                    except():
                        time.sleep(1)
                dic_b = json.loads(data_b.text)
                if dic_a != dic_b:
                    same = False
                else:
                    time.sleep(4)

            for i in range(len(dic_a)):
                if dic_a[i] != dic_b[i]:
                    if int(dic_a[i]["total_sold_tiles"]) < 2000:
                        channel = client.get_channel(796117415389167666)
                        # 796117415389167666
                        await channel.send(f"<@&796062627926245397> Es wurden Gebiete in {dic_a[i]['name']} für {dic_b[i]['new_tile_price']}verkauft")
                    else:
                        channel2 = client.get_channel(796203364194582528)
                        await channel2.send("runing")
                else:
                    time.sleep(0.5)
            driver.close()
            driver.quit()

    async def on_message(self, message):
        if message.content.startswith("§display"):
            await message.channel.send("bot is running")


client = MyClient()
client.run("Nzk1ODc1ODkwOTgyNDIwNDgw.X_PvLw._jdO3p1MN0c5_u-NAGYE0ILgquQ")


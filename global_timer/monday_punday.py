import aiohttp
import datetime
import discord
import global_vars
import json
import re

from discord.ext import commands
from pathlib import Path

url = "https://mondaypunday.com/wp-json/wp/v2/posts"

async def monday_punday(bot):

    # get current day in YYYY-MM-DD
    today = "{0.year}-{0.month:02d}-{0.day:02d}".format(datetime.datetime.today())

    # get punday data
    async with aiohttp.get(url) as resp:
        data = await resp.json()
        html = data[0]["content"]["rendered"]

        img_url = re.findall('\ssrc="([^"]+)"', html)[0]

        if global_vars.PROD:
            dest = discord.utils.get(bot.get_all_channels(),
                    server__name="くコ:彡Squid Squad くコ:", 
                    name="general")
        else:
            dest = discord.utils.get(bot.get_all_channels(),
                    server__name="Memes PTR Alpha", 
                    name="general")

        await bot.send_message(
                dest,
                "Monday Punday for {0}!\n" +
                "Enter guess here: https://mondaypunday.com/\n"+
                "{1}".format(today, img_url))

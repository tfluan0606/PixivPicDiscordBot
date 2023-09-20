# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 11:59:07 2022

@author: tfluan0606
"""


import discord
import os
import re
from pixivpy3 import *

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

pixiv_api = AppPixivAPI()
REFRESH_TOKEN = 'PIXIV TOKEN HERE'

purl = 'YOUR REVERSE PROXY SERVER HERE'


@client.event
#this is the on_ready function for discord, once the bot successfully lauch, this will be called
#you can delet this if you don't need.
async def on_ready():
    pid = os.getpid()
    log = client.get_channel(some channel id)
    await log.send('成功啟動'+'\n'+str(pid))


@client.event
async def on_message(message):


    if some condition to process coming link:
        channel = message.channel
        #mesId = message.id
        #字串的處理
        url = message.content.split('/')

        if 'www.pixiv.net' in url:
            pixiv_api.auth(refresh_token=REFRESH_TOKEN)
            artid = url[-1]
            art_data = pixiv_api.illust_detail(int(artid))
            pages = art_data.illust.page_count
            if pages == 1 :
                image_url = art_data.illust.meta_single_page['original_image_url']
                await channel.send(image_url.replace('i.pximg.net',purl))
            else:
                for i in range(pages):
                    image_url = art_data.illust.meta_pages
                    await channel.send(image_url[i]["image_urls"]["original"].replace('i.pximg.net',purl))




client.run('discord token here')

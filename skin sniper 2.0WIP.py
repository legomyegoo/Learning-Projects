#skinport sniper prototype

#imports
from bs4 import BeautifulSoup
from datetime import time, timedelta, datetime
import time
import requests
import schedule 
import re 

#shortend links
skinporturl = 'https://skinport.com/market?sort=date&order=desc'
buffurl = 'https://buff.market/market/all'

##scan & rescan## function(connected to timing_skiport_check())
def timed_rescans():
    req= lambda: requests.get(skinporturl, timeout=1)#get spesifc html info I need, this the entire site, its not efficent 
    global r_req
    r_req = req() 
    soup = lambda: BeautifulSoup(r_req.text, 'html.parser')
    global s_req
    s_req = soup()


##schdule## function(connected to timed_rescans())
def timing_skiport_check():
    schedule.every(1).second.do(timed_rescans)
    while True:
        schedule.run_pending()
        time.sleep(1) 


#intial skinport connection fucntion 
def intial_skinport_check():
    try:
        inti_req = requests.get(skinporturl, timeout=1)
        if inti_req.status_code==200:
            print('W Connection to Skinport')
            buff_check()
    except Exception as e:
        print('L Connection to Skinport','-',e)
        #### add discrd bot ####

##intial buff connection## fucntion(connwcted to intial_skinport_check())
def buff_check():
    try:
        inti_req = requests.get(buffurl)
        if inti_req.status_code==200:
            print('W Connection to Buff') 
            timing_skiport_check()
    except Exception as e:
        print('L Connection to Buff','-',e)
        #### add discrd bot ####

def listing_info_grabber():
    soup = s_req.find_all('a', class_="ItemPreview-href")
    #<a class="ItemPreview-href" aria-label="G3SG1 | Green Apple (Factory New)" href="/item/g3sg1-green-apple-factory-new">G3SG1 | Green Apple (Factory New)</a>
    
    ###########     #get soup info and make class for gun
    #check class vs buff        #########################
    
        

def find_listings():
    x=0
    try: 
        new_dates = re.compile(r'^2024-12-10')#change to auto updated dates
        result = s_req.find_next('time',{'datetime': new_dates})
        for result in s_req:
            x += 1 
            listing_info_grabber()
            if x >= 3:
                break
            print(x,'/3','New listings found')
    except Exception:
        print('No new listings found')

    



intial_skinport_check()

if connection_made_to_both:
    print('poo')
    #timing_skiport_check()



#info if item was good to add to cart
#def constant_skinport_check():
    
  
#<div class="CatalogPage-item CatalogPage-item--grid" style="z-index: 92;"><div class="ItemPreview ItemPreview--grid ItemPreview--id-730"><a class="ItemPreview-href" aria-label="StatTrak™ AWP | Chrome Cannon (Field-Tested)" href="/item/stattrak-awp-chrome-cannon-field-tested">StatTrak™ AWP | Chrome Cannon (Field-Tested)</a><div class="ItemPreview-content"><div class="ItemPreview-wrapper"><a class="ItemPreview-link" rel="ugc" href="/item/stattrak-awp-chrome-cannon-field-tested/52831141"><div class="ItemPreview-commonInfo"><div class="ItemPreview-top"><div class="TradeLock-lock ItemPreview-lock TradeLock-lock--locked"><div class="Tooltip-link"><svg class="TradeLock-timeIcon clock-lock"><use xlink:href="/static/svg/sprite.4199c1bdf6f0f3d88338.svg#clock-lock"></use></svg>in 7 days</div></div></div><div class="ItemPreview-itemImage"><img class="" src="https://community.cloudflare.steamstatic.com/economy/image/class/730/5721236370/256x128" alt="StatTrak™ AWP | Chrome Cannon (Field-Tested)" loading="lazy" aria-hidden="true"></div><div class="ItemPreview-stickers"><div class="Tooltip-link"><img src="https://steamcdn-a.akamaihd.net/apps/730/icons/econ/stickers/community/community_2024/holo_cedar_creek.2bcc652c3ece90652659db4dc59c481d2194f295.png" alt="Cedar Creek (Holo)" loading="lazy" class="ItemPreview-sticker"></div><div class="Tooltip-link"><img src="https://steamcdn-a.akamaihd.net/apps/730/icons/econ/stickers/community/community_2024/holo_cedar_creek.2bcc652c3ece90652659db4dc59c481d2194f295.png" alt="Cedar Creek (Holo)" loading="lazy" class="ItemPreview-sticker"></div><div class="Tooltip-link"><img src="https://steamcdn-a.akamaihd.net/apps/730/icons/econ/stickers/community/community_2024/holo_cedar_creek.2bcc652c3ece90652659db4dc59c481d2194f295.png" alt="Cedar Creek (Holo)" loading="lazy" class="ItemPreview-sticker"></div><div class="Tooltip-link"><img src="https://steamcdn-a.akamaihd.net/apps/730/icons/econ/stickers/community/community_2024/holo_cedar_creek.2bcc652c3ece90652659db4dc59c481d2194f295.png" alt="Cedar Creek (Holo)" loading="lazy" class="ItemPreview-sticker"></div></div><div class="ItemPreview-itemInfo"><div class="ItemPreview-price"><div class="ItemPreview-priceValue"><div class="Tooltip-link">$79.13</div><div class="GradientLabel ItemPreview-discount"><span>− 12%</span></div></div><div class="ItemPreview-oldPrice">Suggested price $89.58</div></div><div class="ItemPreview-itemTitle" style="color: rgb(207, 106, 50);">StatTrak™ AWP</div><div class="ItemPreview-itemName">Chrome Cannon<div class="Tooltip-link ItemPreview-nameTag">&nbsp;<svg class="nametag"><use xlink:href="/static/svg/sprite.4199c1bdf6f0f3d88338.svg#nametag"></use></svg></div></div><div class="ItemPreview-itemText">Field-Tested StatTrak™ Covert Sniper Rifle</div></div></div><div class="ItemPreview-wear"><div class="WearBar"><div class="WearBar-value">0.378</div><div class="WearBar-bar"><div class="WearBar-barBg"><span class="WearBar-bgColor WearBar-bgColor--worst"></span><span class="WearBar-bgColor WearBar-bgColor--bad"></span><span class="WearBar-bgColor WearBar-bgColor--normal"></span><span class="WearBar-bgColor WearBar-bgColor--good"></span><span class="WearBar-bgColor WearBar-bgColor--perfect"></span></div><div class="WearBar-progress" style="left: 37.8705%;"><svg class="WearBar-arrow triangle"><use xlink:href="/static/svg/sprite.4199c1bdf6f0f3d88338.svg#triangle"></use></svg></div></div></div></div></a></div><div role="presentation" class="ItemPreview-actionBtn"><button type="button" class="ItemPreview-mainAction">Add to cart</button><button type="button" class="ItemPreview-sideAction" aria-label="..."><span class="ItemPreview-sideDot"></span><span class="ItemPreview-sideDot"></span><span class="ItemPreview-sideDot"></span></button></div></div></div></div>
#<div class="CatalogPage-item CatalogPage-item--grid" style="z-index: 84;"><div class="ItemPreview ItemPreview--grid ItemPreview--id-730"><a class="ItemPreview-href" aria-label="StatTrak™ Music Kit | The Verkkars &amp; n0thing, Flashbang Dance" href="/item/stattrak-music-kit-the-verkkars-n0thing-flashbang-dance">StatTrak™ Music Kit | The Verkkars &amp; n0thing, Flashbang Dance</a><div class="ItemPreview-content"><div class="ItemPreview-wrapper"><a class="ItemPreview-link" rel="ugc" href="/item/stattrak-music-kit-the-verkkars-n0thing-flashbang-dance/52831126"><div class="ItemPreview-commonInfo"><div class="ItemPreview-top"><div class="TradeLock-lock ItemPreview-lock TradeLock-lock--locked"><div class="Tooltip-link"><svg class="TradeLock-timeIcon clock-lock"><use xlink:href="/static/svg/sprite.4199c1bdf6f0f3d88338.svg#clock-lock"></use></svg>in 7 days</div></div></div><div class="ItemPreview-itemImage"><img class="" src="https://community.cloudflare.steamstatic.com/economy/image/class/730/4638743545/256x128" alt="StatTrak™ Music Kit | The Verkkars &amp; n0thing, Flashbang Dance" loading="lazy" aria-hidden="true"></div><div class="ItemPreview-itemInfo"><div class="ItemPreview-price"><div class="ItemPreview-priceValue"><div class="Tooltip-link">$5.18</div><div class="GradientLabel ItemPreview-discount"><span>− 21%</span></div></div><div class="ItemPreview-oldPrice">Suggested price $6.57</div></div><div class="ItemPreview-itemTitle" style="color: rgb(207, 106, 50);">StatTrak™ Music Kit</div><div class="ItemPreview-itemName">The Verkkars &amp; n0thing, Flashbang Dance</div><div class="ItemPreview-itemText">StatTrak™ High Grade Music Kit</div></div></div></a></div><div role="presentation" class="ItemPreview-actionBtn"><button type="button" class="ItemPreview-mainAction">Add to cart</button><button type="button" class="ItemPreview-sideAction" aria-label="..."><span class="ItemPreview-sideDot"></span><span class="ItemPreview-sideDot"></span><span class="ItemPreview-sideDot"></span></button></div></div></div></div>









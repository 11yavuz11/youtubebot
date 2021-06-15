#!/usr/bin/python3
# -- coding: utf-8 --
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy,ProxyType
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options
from time import sleep
import random
import sys
import subprocess as cmd

#https://github.com/mozilla/geckodriver/releases

def returnIp():
    a=str(random.randint(1,254))
    b=str(random.randint(1,254))
    c=str(random.randint(1,254))
    d=str(random.randint(1,254))
    e="."
    f=a+e+b+e+c+e+d
    return f

def print_percent_done(index, total, bar_len=50, title='Video İzleniyor '):
    
    percent_done = (index+1)/total*100
    percent_done = round(percent_done, 1)

    done = round(percent_done/(100/bar_len))
    togo = bar_len-done

    done_str = '█'*int(done)
    togo_str = '░'*int(togo)

    print(f'⏳{title}: [{done_str}{togo_str}] {percent_done}% İzlendi', end='\r')

    if round(percent_done) == 100:
        print('\t✅')

print('Uygulama Başladı.')
targetUrl = 'https://www.youtube.com/watch?v=hfJedQCMdAc' ###CHANGE THIS
counter=0
elapsed=0
    
while True:
    print("Bot tarafından {} kez görüntülendi".format(counter))
    dakika = 0
    saniye = 0
    sure = 0
    newIp = returnIp()
    httpProxy="http://{}".format(newIp)+":80"
    httpsProxy = "https://{}".format(newIp)+":443"
    ftpProxy = "ftp://{}".format(newIp)+":21"

    proxy=Proxy({
        'ProxyType':ProxyType.MANUAL,
        'http':httpProxy,
        'https':httpsProxy,
        'ftp':ftpProxy,
        'noProxy':''
    })

    path=("/home/kali/Documents/bot/geckodriver") ###CHANGE THIS
    profile = webdriver.FirefoxProfile()
    #1 > Allow all
    #2 > Block all
    #3 > Block 3rd party
    profile.set_preference("permissions.default.image",2)
    options = Options()
    options.headless = True
    #firefox_profile=profile
    #options=options
    driver = webdriver.Firefox(proxy=proxy,executable_path=path,firefox_profile=profile,options=options)
    print("İp Adresleri >>>>>> HTTP = ",httpProxy," HTTPS = ",httpsProxy," FTP = ",ftpProxy)
    driver.get(targetUrl)
    cmd.run("clear")

    #DEFINE BUTTONS
    while True:
        try:
            wievsData = driver.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[5]/div[2]/ytd-video-primary-info-renderer/div/div/div[1]/div[1]/ytd-video-view-count-renderer/span[1]").text
            wievsDataSplitted = wievsData.split(' ')
            wievs = wievsDataSplitted[0]
            playButton = driver.find_element_by_class_name("ytp-play-button")
            muteButton = driver.find_element_by_class_name("ytp-mute-button")           
            settingsButton = driver.find_element_by_class_name("ytp-settings-button")
            fullScreenButton = driver.find_element_by_class_name("ytp-fullscreen-button")
            break
        except:
            sleep(0.2)
            continue
    print("Sayfa Yüklendi")
    print("Ne kadar görüntülendi: ",wievs)
    playButton.click()
    print("Oynatılıyor...")
    muteButton.click()
    #TIME TO WAIT
    duration = driver.find_element_by_class_name("ytp-time-duration").text
    print("Toplam Süre : ",duration)
    splittedDuration = duration.split(":")
    dakika = int(splittedDuration[0])*60
    saniye = int(splittedDuration[1])
    sure = dakika+saniye
    elapsedTime = driver.find_element_by_class_name("ytp-time-current").text
    r = sure
    for i in range(r):
        print_percent_done(i,r)
        sleep(1)
    counter+=1
    print("Bot tarafından {} kez görüntülendi".format(counter))
    sleep(0.3)
    print("Video bitti...")
    driver.close()
    cmd.run("clear")

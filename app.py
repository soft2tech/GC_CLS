import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import yaml

a_yaml_file = open("db.yaml")

DIC = yaml.load(a_yaml_file, Loader=yaml.FullLoader)

ID = DIC['login']['username']
PD = DIC['login']['password']


def get_time():
    TIME = datetime.datetime.now()
    global WD
    WD = TIME.strftime('%a')
    global TM
    TM = TIME.strftime('%H%M')
def open_class(url, UN, passwd):
    if url == "NOTH":
        pass
    else:
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get("%s?proto=true" % (url)) # proto=true mean openning class via web
        driver.find_element_by_id("name").send_keys(str(UN))
        driver.find_element_by_id("pwd").send_keys(str(passwd))
        driver.find_element_by_xpath("//input[@id='login-button']") .click()
        driver.find_element_by_xpath("//button[@class='button-style']") .click()
get_time()
while True:
    if WD == "Sat":
        dic = DIC['sat']
        if 758 <= int(TM) <= 858:
            url = dic['1st']
            open_class(url, ID, PD)
        elif 918 <= int(TM) <= 1018:
            url = dic['2nd']
            open_class(url, ID, PD)
        elif 1038 <= int(TM) <= 1138:
            url = dic['3rd']
            open_class(url, ID, PD)
        elif 1158 <= int(TM) <= 1258:
            url = dic['4th']
            open_class(url, ID, PD)
        elif 1318 <= int(TM) <= 1418:
            url = dic['5th']
            open_class(url, ID, PD)
        else:
            print("You Dont Have any class yet")
            exit()
    elif WD == "Sun":
        dic = DIC['sun']
        if 758 <= int(TM) <= 858:
            url = dic['1st']
            open_class(url, ID, PD)
        elif 918 <= int(TM) <= 1018:
            url = dic['2nd']
            open_class(url, ID, PD)
        elif 1038 <= int(TM) <= 1138:
            url = dic['3rd']
            open_class(url, ID, PD)
        elif 1158 <= int(TM) <= 1258:
            url = dic['4th']
            open_class(url, ID, PD)
        elif 1318 <= int(TM) <= 1418:
            url = dic['5th']
            open_class(url, ID, PD)
        else:
            print("You Dont Have any class yet")
            exit()
    elif WD == "Mon":
        dic = DIC['mon']
        if 758 <= int(TM) <= 858:
            url = dic['1st']
            open_class(url, ID, PD)
        elif 918 <= int(TM) <= 1018:
            url = dic['2nd']
            open_class(url, ID, PD)
        elif 1038 <= int(TM) <= 1138:
            url = dic['3rd']
            open_class(url, ID, PD)
        elif 1158 <= int(TM) <= 1258:
            url = dic['4th']
            open_class(url, ID, PD)
        elif 1318 <= int(TM) <= 1418:
            url = dic['5th']
            open_class(url, ID, PD)
        else:
            print("You Dont Have any class yet")
            exit()
    elif WD == "Tue":
        dic = DIC['tue']
        if 758 <= int(TM) <= 858:
            url = dic['1st']
            open_class(url, ID, PD)
        elif 918 <= int(TM) <= 1018:
            url = dic['2nd']
            open_class(url, ID, PD)
        elif 1038 <= int(TM) <= 1138:
            url = dic['3rd']
            open_class(url, ID, PD)
        elif 1158 <= int(TM) <= 1258:
            url = dic['4th']
            open_class(url, ID, PD)
        elif 1318 <= int(TM) <= 1418:
            url = dic['5th']
            open_class(url, ID, PD)
        else:
            print("You Dont Have any class yet")
            exit()
    elif WD == "Wed":
        dic = DIC['wed']
        if 758 <= int(TM) <= 858:
            url = dic['1st']
            open_class(url, ID, PD)
        elif 918 <= int(TM) <= 1018:
            url = dic['2nd']
            open_class(url, ID, PD)
        elif 1038 <= int(TM) <= 1138:
            url = dic['3rd']
            open_class(url, ID, PD)
        elif 1158 <= int(TM) <= 1258:
            url = dic['4th']
            open_class(url, ID, PD)
        elif 1318 <= int(TM) <= 1418:
            url = dic['5th']
            open_class(url, ID, PD)
        else:
            print("You Dont Have any class yet")
            exit()
    else:
        print("Happy Holyday to you")
        exit()
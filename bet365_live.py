# all leagues - live
from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
import time
from loadMatch import loadMatch
import pandas as pd

# connect to the website
driver = webdriver.Chrome(executable_path=r'C:/Users/Angel/Downloads/chromedriver_win32/chromedriver_1.exe')
driver.get("https://www.bet365.com/#/IP/B18/")
main_window = driver.current_window_handle

print("Load all live games")
time.sleep(5)

''' switchButton '''
def loadPage(leagueName):
    time.sleep(2)
    now = str(datetime.now())
    nowtime = now[:10] + '_' + now[11:13] + '-' + now[14:16] + '-' + now[17:19]
    gameName = getName()
    mylist = []
    try:
        loadMatch(leagueName, mylist, gameName, now)
        time.sleep(1)
        # to csv
        df = pd.DataFrame(mylist, columns=['leagueName', 'gameName', 'type', 'Festival', 'fest', 'gameTime', 'Match', 'Head', 'Team', 'Odd_1', 'Odd_2', 'Odd_3', 'createTime'])
        df.to_csv('result/Bet365Data/live/' + gameName + '_' + nowtime + '.csv', index=False)
    except:
        print("one error")
        print(mylist[-1])
        df = pd.DataFrame(mylist,columns=['leagueName', 'gameName', 'type', 'Festival', 'fest', 'gameTime', 'Match', 'Head','Team', 'Odd_1', 'Odd_2', 'Odd_3', 'createTime'])
        df.to_csv('result/Bet365Data/live/' + gameName + '_' + nowtime + '.csv', index=False)
        return

''' get Name '''
def getName():
    gameName = driver.find_element_by_xpath('//div[@class="ipe-EventHeader_Fixture "]').get_attribute(
        'innerHTML').lstrip()
    gameName = gameName.replace('@', 'v')
    extra = ['?', '/', '.', ',', '\\', '*', '<', '>', '\'', '\"', '|', '`', '~', '!']
    for ex in extra:
        gameName = gameName.replace(ex, '')
    print(gameName)
    return gameName

''' mainMatch '''
def mainMatch(leagueName, gameName, gameTime, gameFest, block, Festival, mylist, now):
    path = '//div[@class="sip-MarketGroup "][' + str(block) + ']/div[2]/div[@class="gl-MarketGroupContainer "]'
    length = len(driver.find_elements_by_xpath(path + '/div[1]/div'))
    for i in range(2, length + 1):
        Match = driver.find_element_by_xpath(path + '/div[1]/div[' + str(i) + ']/div').get_attribute('innerHTML').lstrip()
        Team = ''
        Odd_3 = ''
        check = driver.find_elements_by_xpath(path + '/div[2]/div[' + str(i) + ']/span')
        if len(check) > 1:
            Head = driver.find_element_by_xpath(path + '/div[2]/div[' + str(i) + ']/span[1]').get_attribute('innerHTML').lstrip()
            Odd_1 = driver.find_element_by_xpath(path + '/div[2]/div[' + str(i) + ']/span[2]').get_attribute('innerHTML').lstrip()
            Odd_2 = driver.find_element_by_xpath(path + '/div[3]/div[' + str(i) + ']/span[2]').get_attribute('innerHTML').lstrip()
        else:
            Head = ''
            Odd_1 = driver.find_element_by_xpath(path + '/div[2]/div[' + str(i) + ']/span[1]').get_attribute('innerHTML').lstrip()
            Odd_2 = driver.find_element_by_xpath(path + '/div[3]/div[' + str(i) + ']/span[1]').get_attribute('innerHTML').lstrip()
        mylist.append([leagueName, gameName, 'Live', Festival, gameFest, gameTime, Match, Head, Team, Odd_1, Odd_2, Odd_3, now])
    time.sleep(0.1)


def resultTotal(leagueName, gameName, gameTime, gameFest, block, Festival, mylist, now):
    path = '//div[@class="sip-MarketGroup "][' + str(block) + ']/div[2]/div[@class="gl-MarketGroupContainer "]'
    length = len(driver.find_elements_by_xpath(path + '/div[1]/div'))
    for i in range(2, length + 1):
        Team = driver.find_element_by_xpath(path + '/div[1]/div[' + str(i) + ']/div').get_attribute('innerHTML').lstrip()
        Match = ''
        Head = ''
        Odd_3 = ''
        check = driver.find_elements_by_xpath(path + '/div[2]/div[' + str(i) + ']/span')
        if len(check) > 1:
            Head = driver.find_element_by_xpath(path + '/div[2]/div[' + str(i) + ']/span[@class="srb-ParticipantCenteredStackedMarketRow_Handicap"]').get_attribute('innerHTML').lstrip()
        Odd_1 = driver.find_element_by_xpath(path + '/div[2]/div[' + str(i) + ']/span[@class="srb-ParticipantCenteredStackedMarketRow_Odds"]').get_attribute('innerHTML').lstrip()
        Odd_2 = driver.find_element_by_xpath(path + '/div[3]/div[' + str(i) + ']/span[@class="srb-ParticipantCenteredStackedMarketRow_Odds"]').get_attribute('innerHTML').lstrip()
        mylist.append([leagueName, gameName, 'Live', Festival, gameFest, gameTime, Match, Head, Team, Odd_1, Odd_2, Odd_3, now])
    time.sleep(0.1)


def teamPoints(leagueName, gameName, gameTime, gameFest, block, Festival, mylist, now):
    path = '//div[@class="sip-MarketGroup "][' + str(block) + ']/div[2]/div/div'
    Match = '球隊總分'
    Odd_3 = ''
    homeName = driver.find_element_by_xpath(path + '[1]/div[1]').get_attribute('innerHTML').lstrip()
    awayName = driver.find_element_by_xpath(path + '[2]/div[1]').get_attribute('innerHTML').lstrip()

    length = len(driver.find_elements_by_xpath(path + '[1]/div'))
    for l in range(2, length, 2):
        Head = driver.find_element_by_xpath(path + '[1]/div[' + str(l) + ']/span[1]').get_attribute(
            'innerHTML').lstrip()
        Odd_1 = driver.find_element_by_xpath(path + '[1]/div[' + str(l) + ']/span[2]').get_attribute(
            'innerHTML').lstrip()
        Odd_2 = driver.find_element_by_xpath(path + '[1]/div[' + str(l + 1) + ']/span[2]').get_attribute(
            'innerHTML').lstrip()
        mylist.append([leagueName, gameName, 'Live', Festival, gameFest, gameTime, Match, Head, homeName, Odd_1, Odd_2, Odd_3, now])

    length = len(driver.find_elements_by_xpath(path + '[2]/div'))
    for l in range(2, length, 2):
        Head = driver.find_element_by_xpath(path + '/div[' + str(l) + ']/span[1]').get_attribute(
            'innerHTML').lstrip()
        Odd_1 = driver.find_element_by_xpath(path + '/div[' + str(l) + ']/span[2]').get_attribute(
            'innerHTML').lstrip()
        Odd_2 = driver.find_element_by_xpath(path + '/div[' + str(l + 1) + ']/span[2]').get_attribute(
            'innerHTML').lstrip()
        mylist.append([leagueName, gameName, 'Live', Festival, gameFest, gameTime, Match, Head, awayName, Odd_1, Odd_2, Odd_3, now])
    time.sleep(0.1)

def firstGet(leagueName, gameName, gameTime, gameFest, block, Festival, mylist, now):
    path = '//div[@class="sip-MarketGroup "][' + str(block) + ']/div[2]/div/div'
    length = len(driver.find_elements_by_xpath(path + '[1]/div'))
    Match = ''
    Team = ''
    for l in range(2, length + 1):
        Head = driver.find_element_by_xpath(path + '[1]/div[' + str(l) + ']/div').get_attribute('innerHTML').lstrip()
        Odd_1 = driver.find_element_by_xpath(path + '[2]/div[' + str(l) + ']/span').get_attribute('innerHTML').lstrip()
        Odd_2 = driver.find_element_by_xpath(path + '[3]/div[' + str(l) + ']/span').get_attribute('innerHTML').lstrip()
        Odd_3 = driver.find_element_by_xpath(path + '[4]/div[' + str(l) + ']/span').get_attribute('innerHTML').lstrip()
        mylist.append(
            [leagueName, gameName, 'Live', Festival, gameFest, gameTime, Match, Head, Team, Odd_1, Odd_2, Odd_3, now])
    time.sleep(0.1)


def givePoints(leagueName, gameName, gameTime, gameFest, block, Festival, mylist, now):
    path = '//div[@class="sip-MarketGroup "][' + str(block) + ']/div[2]/div/div'
    length = len(driver.find_elements_by_xpath(path + '[1]/div'))
    Match = '讓分'
    Team = ''
    Odd_3 = ''
    for l in range(2, length+1):
        Head = driver.find_element_by_xpath(path+'[1]/div[' + str(l) + ']/span[2]').get_attribute('innerHTML').lstrip()
        Odd_1 = driver.find_element_by_xpath(path+'[1]/div[' + str(l) + ']/span[3]').get_attribute('innerHTML').lstrip()
        Odd_2 = driver.find_element_by_xpath(path+'[1]/div[' + str(l) + ']/span[3]').get_attribute('innerHTML').lstrip()
        mylist.append([leagueName, gameName, 'Live', Festival, gameFest, gameTime, Match, Head, Team, Odd_1, Odd_2, Odd_3, now])
    time.sleep(0.1)

def attachTotal(leagueName, gameName, gameTime, gameFest, block, Festival, mylist, now):
    Match = '總分'
    Team = ''
    Odd_3 = ''
    path = '//div[@class="sip-MarketGroup "][' + str(block) + ']/div[2]/div/div'
    length = len(driver.find_elements_by_xpath(path + '[1]/div'))
    for l in range(2, length + 1):
        Head = driver.find_element_by_xpath(path + '[1]/div[' + str(l) + ']/div').get_attribute('innerHTML').lstrip()
        Odd_1 = driver.find_element_by_xpath(path + '[2]/div[' + str(l) + ']/span').get_attribute('innerHTML').lstrip()
        Odd_2 = driver.find_element_by_xpath(path + '[3]/div[' + str(l) + ']/span').get_attribute('innerHTML').lstrip()
        mylist.append([leagueName, gameName, 'Live', Festival, gameFest, gameTime, Match, Head, Team, Odd_1, Odd_2, Odd_3, now])
    time.sleep(0.1)

''' totalPoints '''
def totalPoints(leagueName, gameName, gameTime, gameFest, block, Festival, mylist, now):
    path = '//div[@class="sip-MarketGroup "][' + str(block) + ']/div[2]/div/div'
    length = len(driver.find_elements_by_xpath(path+'[1]/div'))
    Match = ''
    Team = ''
    Odd_3 = ''
    for l in range(2, length+1):
        Head = driver.find_element_by_xpath(path + '[1]/div[' + str(l) + ']/div').get_attribute('innerHTML').lstrip()
        Odd_1 = driver.find_element_by_xpath(path + '[2]/div[' + str(l) + ']/span').get_attribute('innerHTML').lstrip()
        Odd_2 = driver.find_element_by_xpath(path + '[3]/div[' + str(l) + ']/span').get_attribute('innerHTML').lstrip()
        mylist.append([leagueName, gameName, 'Live', Festival, gameFest, gameTime, Match, Head, Team, Odd_1, Odd_2, Odd_3,now])
    time.sleep(0.1)


''' load matches '''
def loadMatch(leagueName, mylist, gameName, now):
    time.sleep(3)
    blocksRoot = '//div[@class="sip-MarketGroup "]'
    blocks = len(driver.find_elements_by_xpath(blocksRoot))
    if blocks < 1:
        return

    # extend the list
    print("展翅")
    for block in range(1, blocks+1):
        path = blocksRoot + '[' + str(block) + ']'
        if len(driver.find_elements_by_xpath(path + '/div')) < 2:
            button = driver.find_element_by_xpath(path + '/div[1]')
            ActionChains(driver).move_to_element(button)
            button.click()
        time.sleep(0.1)
    print("啰资料", blocks)
    # load all blocks' data
    for block in range(1, blocks+1):
        try:
            Festival = driver.find_element_by_xpath(blocksRoot + '[' + str(block) + ']/div[1]/div[@class="sip-MarketGroupButton_Text "]').get_attribute('innerHTML').lstrip()
            print(Festival)
            if len(driver.find_elements_by_xpath('//div[@class="ipe-EventHeader_Period "]')) > 0:
                gameFest = driver.find_element_by_xpath('//div[@class="ipe-EventHeader_Period "]').get_attribute('innerHTML').lstrip()
            else:
                gameFest = ''
            if len(driver.find_elements_by_xpath('//div[@class="ipe-EventHeader_ClockContainer "]')) > 0:
                gameTime = driver.find_element_by_xpath('//div[@class="ipe-EventHeader_ClockContainer "]').get_attribute('innerHTML').lstrip()
            else:
                gameTime = ''
            if Festival == "分數投注":
                totalPoints(leagueName, gameName, gameTime, gameFest, block, Festival, mylist, now)
            elif "投注" in Festival:
                mainMatch(leagueName, gameName, gameTime, gameFest, block, Festival, mylist, now)
            elif '奇/偶' in Festival:
                mainMatch(leagueName, gameName, gameTime, gameFest, block, Festival, mylist, now)
            elif '比賽結果和總分' in Festival:
                resultTotal(leagueName, gameName, gameTime, gameFest, block, Festival, mylist, now)
            elif "輸贏比數 3項" in Festival:
                print(Festival, "not yet")
            elif "節 輸贏比數" in Festival:
                print(Festival, "not yet")
            elif "輸贏比數" in Festival:
                totalPoints(leagueName, gameName, gameTime, gameFest, block, Festival, mylist, now)
            elif ("節" in Festival) & ("得分" in Festival):
                totalPoints(leagueName, gameName, gameTime, gameFest, block, Festival, mylist, now)
            elif ("附加" in Festival) & ("總分" in Festival):
                totalPoints(leagueName, gameName, gameTime, gameFest, block, Festival, mylist, now)
            elif "球隊總分" in Festival:
                teamPoints(leagueName, gameName, gameTime, gameFest, block, Festival, mylist, now)
            elif "附加讓分" in Festival:
                givePoints(leagueName, gameName, gameTime, gameFest, block, Festival, mylist, now)
            elif "附加比賽總分" in Festival:
                attachTotal(leagueName, gameName, gameTime, gameFest, block, Festival, mylist, now)
            elif "讓分 三項" in Festival:
                print(Festival, "not yet")
            elif "首先獲得" in Festival:
                firstGet(leagueName, gameName, gameTime, gameFest, block, Festival, mylist, now)
            else:
                print(Festival, "extra")
        except:
            print(Festival, "loading error!")
        time.sleep(0.1)


''' load betting list '''
def loadLeague():
    try:
        leaguePath = '//div[@class="ovm-Competition ovm-Competition-open "]'
        leagues = driver.find_elements_by_xpath(leaguePath)
        for league in range(1, len(leagues)+1):
            leagueName = driver.find_element_by_xpath(leaguePath + '[' + str(league) + ']/div[1]/div/div[1]').get_attribute('innerHTML').lstrip()
            # load games in one league
            gamePath = leaguePath + '[' + str(league) + ']/div[2]/div'
            games = driver.find_elements_by_xpath(gamePath)
            print(leagueName, len(games))
            for game in range(1, len(games)+1):
                Go = driver.find_element_by_xpath(gamePath + '[' + str(game) + ']/div[1]/div[1]/div')
                ActionChains(driver).move_to_element(Go)
                Go.click()
                loadPage(leagueName)
                time.sleep(1)
                driver.back()
                time.sleep(1)
    except:
        loadLeague()
# start loading data
while True:
    loadLeague()
    time.sleep(5)

print('done')
time.sleep(1000)
driver.quit()
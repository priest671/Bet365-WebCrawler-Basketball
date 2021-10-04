import time
from datetime import datetime
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains

def givePoints(driver, block, mylist, leagueName, gameTime, gameName, now):
    print("附加让分")
    Festival = driver.find_element_by_xpath('//div[@class="gl-MarketGroup "][' + str(block) + ']/div[1]/div').get_attribute('innerHTML').lstrip()
    Match = '讓分'
    Team = ''
    homePath = '//div[@class="gl-MarketGroup "][' + str(block) + ']/div[2]/div/div[1]'
    awayPath = '//div[@class="gl-MarketGroup "][' + str(block) + ']/div[2]/div/div[2]'
    length = len(driver.find_elements_by_xpath(homePath + '/div'))
    for l in range(2, length+1):
        Head = driver.find_element_by_xpath(homePath+'/div[' + str(l) + ']/span[2]').get_attribute('innerHTML').lstrip()
        Odd_1 = driver.find_element_by_xpath(homePath+'/div[' + str(l) + ']/span[3]').get_attribute('innerHTML').lstrip()
        Odd_2 = driver.find_element_by_xpath(awayPath+'/div[' + str(l) + ']/span[3]').get_attribute('innerHTML').lstrip()
        mylist.append([leagueName, gameName, 'Prematch', Festival, gameTime, Match, Head, Team, Odd_1, Odd_2, now])


def totalPoints(driver, block, mylist, leagueName, gameTime, gameName, now):
    print("附加比赛总分")
    Festival = driver.find_element_by_xpath('//div[@class="gl-MarketGroup "][' + str(block) + ']/div[1]/div').get_attribute('innerHTML').lstrip()
    Match = '總分'
    Team = ''
    num = '//div[@class="gl-MarketGroup "][' + str(block) + ']/div[2]/div/div[1]'
    big = '//div[@class="gl-MarketGroup "][' + str(block) + ']/div[2]/div/div[2]'
    small = '//div[@class="gl-MarketGroup "][' + str(block) + ']/div[2]/div/div[3]'
    length = len(driver.find_elements_by_xpath(num + '/div'))
    for l in range(2, length+1):
        Head = driver.find_element_by_xpath(num + '/div[' + str(l) + ']/div').get_attribute('innerHTML').lstrip()
        Odd_1 = driver.find_element_by_xpath(big + '/div[' + str(l) + ']/span').get_attribute('innerHTML').lstrip()
        Odd_2 = driver.find_element_by_xpath(small + '/div[' + str(l) + ']/span').get_attribute('innerHTML').lstrip()
        mylist.append([leagueName, gameName, 'Prematch', Festival, gameTime, Match, Head, Team, Odd_1, Odd_2, now])
    num = '//div[@class="gl-MarketGroup "][' + str(block) + ']/div[2]/div/div[4]'
    big = '//div[@class="gl-MarketGroup "][' + str(block) + ']/div[2]/div/div[5]'
    small = '//div[@class="gl-MarketGroup "][' + str(block) + ']/div[2]/div/div[6]'
    length = len(driver.find_elements_by_xpath(num + '/div'))
    for l in range(2, length):
        Head = driver.find_element_by_xpath(num + '/div[' + str(l) + ']/div').get_attribute('innerHTML').lstrip()
        Odd_1 = driver.find_element_by_xpath(big + '/div[' + str(l) + ']/span').get_attribute('innerHTML').lstrip()
        Odd_2 = driver.find_element_by_xpath(small + '/div[' + str(l) + ']/span').get_attribute('innerHTML').lstrip()
        mylist.append([leagueName, gameName, 'Prematch', Festival, gameTime, Match, Head, Team, Odd_1, Odd_2, now])


def teamPoints(driver, block, mylist, leagueName, gameTime, gameName, now):
    print("球隊總得分")
    Festival = driver.find_element_by_xpath('//div[@class="gl-MarketGroup "][' + str(block) + ']/div[1]/div').get_attribute('innerHTML').lstrip()
    Match = '球隊總分'
    homePath = '//div[@class="gl-MarketGroup "][' + str(block) + ']/div[2]/div/div[1]'
    awayPath = '//div[@class="gl-MarketGroup "][' + str(block) + ']/div[2]/div/div[2]'
    homeName = driver.find_element_by_xpath(homePath + '/div[1]').get_attribute('innerHTML').lstrip()
    awayName = driver.find_element_by_xpath(awayPath + '/div[1]').get_attribute('innerHTML').lstrip()
    length = len(driver.find_elements_by_xpath(homePath + '/div'))
    for l in range(2, length, 2):
        Head = driver.find_element_by_xpath(homePath + '/div[' + str(l) + ']/span[1]').get_attribute('innerHTML').lstrip()
        Odd_1 = driver.find_element_by_xpath(homePath + '/div[' + str(l) + ']/span[2]').get_attribute('innerHTML').lstrip()
        Odd_2 = driver.find_element_by_xpath(homePath + '/div[' + str(l+1) + ']/span[2]').get_attribute('innerHTML').lstrip()
        mylist.append([leagueName, gameName, 'Prematch', Festival, gameTime, Match, Head, homeName, Odd_1, Odd_2, now])
    length = len(driver.find_elements_by_xpath(awayPath + '/div'))
    for l in range(2, length, 2):
        Head = driver.find_element_by_xpath(awayPath + '/div[' + str(l) + ']/span[1]').get_attribute('innerHTML').lstrip()
        Odd_1 = driver.find_element_by_xpath(awayPath + '/div[' + str(l) + ']/span[2]').get_attribute('innerHTML').lstrip()
        Odd_2 = driver.find_element_by_xpath(awayPath + '/div[' + str(l+1) + ']/span[2]').get_attribute('innerHTML').lstrip()
        mylist.append([leagueName, gameName, 'Prematch', Festival, gameTime, Match, Head, awayName, Odd_1, Odd_2, now])


''' load matches '''
def loadMatch(driver, leagueName):
    time.sleep(5)
    mylist = []
    now = str(datetime.now())
    nowtime = now[:10] + '_' + now[11:13] + '-' + now[14:16] + '-' + now[17:19]
    blocksRoot = '//div[@class="gl-MarketGroup "]'
    blocks = driver.find_elements_by_xpath(blocksRoot)
    if len(blocks) > 0:
        # get game name & filter it
        gameName = driver.find_element_by_xpath('//div[@class="sph-EventHeader_Label "]/span').get_attribute('innerHTML').lstrip()
        gameName = gameName.replace('@', 'v')
        extra = ['?', '/', '.', ',', '\\', '*', '<', '>', '\'', '\"', '|', '`', '~', '!']
        for ex in extra:
            gameName = gameName.replace(ex, '')
        print(gameName, len(blocks))
    else:
        return
    ''' load mainMatch '''
    for block in range(1, len(blocks)):
        Festival = driver.find_element_by_xpath(blocksRoot + '[' + str(block) + ']/div[1]/div[@class="gl-MarketGroupButton_Text "]').get_attribute('innerHTML').lstrip()
        gameTime = driver.find_element_by_xpath('//div[@class="sph-ExtraData_TimeStamp "]').get_attribute('innerHTML').lstrip()
        path = '//div[@class="gl-MarketGroup "][' + str(block) + ']/div[2]/div[@class="gl-MarketGroupContainer "]'
        length = len(driver.find_elements_by_xpath(path + '/div[1]/div'))
        for i in range(2, length+1):
            Match = driver.find_element_by_xpath(path + '/div[1]/div[' + str(i) + ']/div').get_attribute('innerHTML').lstrip()
            Team = ''
            Head = ''
            check = driver.find_elements_by_xpath(path + '/div[2]/div[' + str(i) + ']/span')
            if len(check) > 1:
                Head = driver.find_element_by_xpath(path + '/div[2]/div[' + str(i) + ']/span[@class="sab-ParticipantCenteredStackedOTB_Handicap"]').get_attribute('innerHTML').lstrip()
            Odd_1 = driver.find_element_by_xpath(path + '/div[2]/div[' + str(i) + ']/span[@class="sab-ParticipantCenteredStackedOTB_Odds"]').get_attribute('innerHTML').lstrip()
            Odd_2 = driver.find_element_by_xpath(path + '/div[3]/div[' + str(i) + ']/span[@class="sab-ParticipantCenteredStackedOTB_Odds"]').get_attribute('innerHTML').lstrip()
            mylist.append([leagueName, gameName, 'Prematch', Festival, gameTime, Match, Head, Team, Odd_1, Odd_2, now])


    ''' load specialMatch '''
    Go = driver.find_element_by_xpath('//div[@class="sph-HorizontalNavBarScroller_Contents "]/div[3]')
    Go.click()
    time.sleep(1)
    blocksRoot = '//div[@class="gl-MarketGroup "]'
    blocks = driver.find_elements_by_xpath(blocksRoot)
    # extend the list
    for block in range(1, len(blocks)):
        path = blocksRoot + '[' + str(block) +']'
        if len(driver.find_elements_by_xpath(path + '/div')) < 2:
            button = driver.find_element_by_xpath(path + '/div[@class="gl-MarketGroupButton "]')
            ActionChains(driver).move_to_element(button)
            button.click()
        time.sleep(1)
    # loading data
    for block in range(1, len(blocks)):
        item = driver.find_element_by_xpath(blocksRoot + '[' + str(block) + ']/div[1]/div').get_attribute('innerHTML').lstrip()
        if item == "附加讓分" or item == "附加讓分2":
            givePoints(driver, block, mylist, leagueName, gameTime, gameName, now)
        elif item == "附加比賽總分" or item == "附加比賽總分2":
            totalPoints(driver, block, mylist, leagueName, gameTime, gameName, now)

    
    ''' load teamTotal '''
    Go = driver.find_element_by_xpath('//div[@class="sph-HorizontalNavBarScroller_Contents "]/div[4]')
    Go.click()
    time.sleep(1)
    blocksRoot = '//div[@class="gl-MarketGroup "]'
    blocks = driver.find_elements_by_xpath(blocksRoot)
    print(len(blocks), "blocks")
    # extend the list
    for block in range(1, len(blocks)):
        path = blocksRoot + '[' + str(block) + ']'
        if len(driver.find_elements_by_xpath(path + '/div')) < 2:
            button = driver.find_element_by_xpath(path)
            ActionChains(driver).move_to_element(button)
            button.click()
        time.sleep(1)
    # loading data
    for block in range(1, len(blocks)):
        item = driver.find_element_by_xpath(blocksRoot + '[' + str(block) + ']/div[1]/div').get_attribute('innerHTML').lstrip()
        if item == "球隊總得分" or item == "附加球隊總分" or item == "附加球隊總分2":
            teamPoints(driver, block, mylist, leagueName, gameTime, gameName, now)
    driver.back()

    driver.back()
    time.sleep(1)
    # to csv
    df = pd.DataFrame(mylist, columns=['leagueName', 'gameName', 'type', 'Festival', 'gameTime', 'Match', 'Head', 'Team', 'Odd_1', 'Odd_2', 'createTime'])
    df.to_csv('result/Bet365Data/' + gameName + '_' + nowtime + '.csv', index=False)

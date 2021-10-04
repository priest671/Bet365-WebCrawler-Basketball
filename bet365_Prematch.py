# all leagues - Prematch
from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from loadMatch import loadMatch

# connect to the website
driver = webdriver.Chrome(executable_path=r'C:/Users/Angel/Downloads/chromedriver_win32/chromedriver_1.exe')
driver.get("https://www.bet365.com/#/AS/B18/")
main_window = driver.current_window_handle

# log in
print("all")
print("log in by yourself!")
time.sleep(30)
print("30s left..")
time.sleep(30)


# load all games of one league
def loadGames(leagueName, gamePath):
    games = driver.find_elements_by_xpath(gamePath)
    for item in range(1, len(games)):
        game = driver.find_element_by_xpath(gamePath + '[' + str(item) + ']')
        ActionChains(driver).move_to_element(game)
        game.click()
        try:
            loadMatch(driver, leagueName)
        except:
            loadMatch(driver, leagueName)
        time.sleep(1)
        driver.back()
        time.sleep(1)


''' load betting list '''
def loadLeague():
    try:
        print("load all items in the list")
        time.sleep(7)
        leaguePath = '//div[@class="gl-MarketGrid gl-MarketGrid-wide "]/div'
        leagues = driver.find_elements_by_xpath(leaguePath)
        if len(leagues) == 0:
            print("league element class name error!")
            return
        print(len(leagues), "leagues in the list")
        for i in range(2, len(leagues)-1):
            LeaguePath = leaguePath + '[' + str(i) + ']'
            leagueName = driver.find_element_by_xpath(LeaguePath + '/div[1]/div[@class="sm-SplashMarketGroupButton_Text "]').get_attribute('innerHTML').lstrip()
            print(leagueName)
            if i > 2:
                # click button to extend list
                button = driver.find_element_by_xpath(LeaguePath)
                ActionChains(driver).move_to_element(button)
                button.click()
                time.sleep(1)
            # get matches
            # check match title
            titlePath = LeaguePath + '/div[2]/div/div[@class="sm-SplashMarket "]'
            titles = driver.find_elements_by_xpath(titlePath)
            print(len(titles), "titles in the list")
            if len(titles) > 1:

                title = driver.find_element_by_xpath(titlePath + '[' + str(len(titles)) + ']/div/div[@class="sm-SplashMarket_Title "]').get_attribute('innerHTML').lstrip()
                if title == "賽事特別投注":
                        print("賽事特別投注")
                        button = driver.find_element_by_xpath(titlePath + '[' + str(len(titles)) + ']/div')
                        ActionChains(driver).move_to_element(button)
                        button.click()
                        loadGames(leagueName, titlePath + '[' + str(len(titles)) + ']/div[2]/div[@class="sm-CouponLink "]')
                        time.sleep(0.5)
                else:
                    print("无赛事")
                # close all buttons
                button = driver.find_element_by_xpath(titlePath + '[' + str(len(titles)) + ']/div[1]')
                ActionChains(driver).move_to_element(button)
                button.click()
                time.sleep(0.5)
    except:
        loadLeague()


# start loading data
while True:
    loadLeague()
    time.sleep(3600)

print('done')
driver.quit()
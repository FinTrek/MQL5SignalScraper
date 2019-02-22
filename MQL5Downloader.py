# Importing

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import os


# Requirements

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

def reader() :
    f = open("INPUT.txt","r")
    m = f.readlines()
    f.close()
    url = "https://www.mql5.com/en/signals/"+m[0].replace("SIGNAL ID :","").strip()
    username = m[1].replace("USERNAME :","").strip()
    password = m[2].replace("PASSWORD :","").strip()
    path = m[3].replace("SAVE FILE IN :","").strip()
    if not path[len(path)-1] == "\\" :
        path += "\\"
    return username, password, path, url

USERNAME, PASSWORD, PATH , URL = reader()

# other functions

def contentGetter(string) :
    string = str(string)
    i = 0
    while i < len(string) :
        if string[i] == ">" :
            s = i
            while s < len(string) :
                if string[s] == "<" :
                    return string[i+1:s]
                s += 1
        i += 1

def write(information,path) :
    name = "RESULT.txt"
    f = open(path + name,"w")
    for key in information:
        f.write(str(key)+":"+str(information[key])+"\n")
    f.close()
    print("*** All information have been saved successfully ***")

# Linke maker


# Elements getter functions

def firstPageElementGetter(browser) :
    # Cost
    items = browser.find_elements_by_css_selector(".button.button_tiny.button_green span")
    if len(items) == 0 :
        cost = "Subscription not permitted"
    else :
        cost = items[0].get_attribute("textContent").strip()
    cost = cost.replace("Copy for","").replace("USD","").strip()
    # User
    items = browser.find_elements_by_css_selector(".s-plain-card__title-wrapper")
    user = items[0].get_attribute("textContent").strip()
    # aouthor name and aouthor links
    items = browser.find_elements_by_css_selector(".s-plain-card__author a")
    aouthor = items[0].get_attribute("textContent").strip()
    aouthorLink = items[0].get_attribute("href").strip()
    # Maximum drawdown
    items = browser.find_elements_by_css_selector("tspan")
    Maximum_drawdown = items[6].get_attribute("textContent").replace("drawdown: ","").strip()
    # Profit Trades
    profit_trades = items[1].get_attribute("textContent").strip()
    # Loss Trades
    loss_trades = items[2].get_attribute("textContent").replace("Loss Trades: ","").strip()
    # Leverage
    items = browser.find_elements_by_css_selector(".s-plain-card__leverage")
    leverage = items[0].get_attribute("textContent").strip()
    # Growth
    items = browser.find_elements_by_css_selector(".s-list-info__value")
    growth = items[0].get_attribute("textContent").strip()
    # Initial Deposit
    initial_deposit = items[4].get_attribute("textContent").strip()
    # Balance
    balance = items[3].get_attribute("textContent").strip()
    # Trading Days
    trading_days = items[7].get_attribute("textContent").strip()
    # Trades per week
    trades_per_week = items[9].get_attribute("textContent").strip()
    # Avg holding time
    Avg_holding_time = items[10].get_attribute("textContent").strip()
    # Weeks
    weeks = items[12].get_attribute("textContent").strip()
    # Started
    started = items[13].get_attribute("textContent").strip()
    # Latest trade
    latest_trade = items[8].get_attribute("textContent").strip()
    # Subscribers
    subscribers = items[11].get_attribute("textContent").strip()
    # trading history csv link
    items = browser.find_elements_by_css_selector(".export-csv.padded a")
    trading_history_csv_link = items[0].get_attribute("href").strip()
    # Trades
    items = browser.find_elements_by_css_selector(".s-data-columns__value")
    trades = items[0].get_attribute("textContent").strip()
    # Gross Profit
    gross_profit = items[5].get_attribute("textContent").strip()
    # Gross Loss
    gross_loss = items[6].get_attribute("textContent").strip()
    # Sharp Ratio
    sharp_ratio = items[9].get_attribute("textContent").strip()
    # Max deposit load
    max_deposit_load = items[11].get_attribute("textContent").strip()
    # Latest trade
    latest_trade = items[12].get_attribute("textContent").strip()
    # Long Trades
    long_trades = items[16].get_attribute("textContent").strip()
    # Short Trades
    short_trades = items[17].get_attribute("textContent").strip()
    # Average Profit
    average_profit = items[20].get_attribute("textContent").strip()
    # Average Loss
    average_loss = items[21].get_attribute("textContent").strip()
    return {"cost":cost,
    "user" : user,
    "aouthor" : aouthor,
    "aouthorLink" : aouthorLink,
    "Maximum_drawdown" : Maximum_drawdown,
    "profit_trades" : profit_trades,
    "loss_trades" : loss_trades,
    "leverage" : leverage,
    "growth" : growth,
    "initial_deposit" : initial_deposit,
    "balance" : balance,
    "trading_days" : trading_days,
    "trades_per_week" : trades_per_week,
    "Avg_holding_time" : Avg_holding_time,
    "weeks" : weeks,
    "started" : started,
    "latest_trade" : latest_trade,
    "subscribers" : subscribers,
    "trading_history_csv_link" : trading_history_csv_link,
    "trades" : trades,
    "gross_profit" : gross_profit,
    "gross_loss" : gross_loss,
    "sharp_ratio" : sharp_ratio,
    "max_deposit_load" : max_deposit_load,
    "latest_trade" : latest_trade,
    "long_trades":long_trades,
    "short_trades" : short_trades,
    "average_profit" : average_profit,
    "average_loss" : average_loss
    }

# For one page
option = webdriver.ChromeOptions()
option.add_argument("--start-maximized")
browser = webdriver.Chrome(chrome_options=option)


browser.get("https://www.mql5.com/en/auth_login")
browser.find_element_by_css_selector("#Login").send_keys(USERNAME)
browser.find_element_by_css_selector("#Password").send_keys(PASSWORD)
browser.find_elements_by_css_selector("input")[11].click()
#

time.sleep(5)
browser.get(URL)
information = firstPageElementGetter(browser)

write(information,PATH)

browser.close()
#

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# ========================================= Browser Setup =========================================
# Configure and launch the Chrome browser with options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# Load the Cookie Clicker game and allow time for page load
driver.get("https://orteil.dashnet.org/cookieclicker/")
time.sleep(3)

# Select Brazilian Portuguese as the game language
language = driver.find_element(By.ID, "langSelect-PT-BR")
language.click()
time.sleep(2)

# ========================================= Initialize Game Elements =========================================
cookie_stats = []
cookies_per_second = 0
cookie_money = 0
cost = 0

# Locate the main cookie element
cookie = driver.find_element(By.ID, "bigCookie")

# ========================================= Helper Functions =========================================

def update_stats():
    """
    Updates the current cookie count and cookies-per-second rate
    by parsing the game's on-screen stats.
    """
    global cookie_stats
    global cookie_money
    global cookies_per_second

    cookie_stats = driver.find_element(By.ID, "cookies").text.split("\n")
    cookies_per_second = float(cookie_stats[1].split(" ")[-1])
    try:
        cookie_money = int(cookie_stats[0].split(" ")[0])
    except ValueError:
        cookie_money = int(cookie_stats[0].split(" ")[0].replace(",", ""))

def update_cost():
    """
    Updates the cost of the current upgrade by reading its displayed price.
    Handles number formatting with commas.
    """
    global cost
    try:
        cost = int(upgrade.find_element(By.CLASS_NAME, "price").text)
    except ValueError:
        cost = int(upgrade.find_element(By.CLASS_NAME, "price").text.replace(",", ""))

# ========================================= Main Automation Loop =========================================
# Set total game duration (20 minutes)
game_time = time.time()
end_time = game_time + 60 * 20

while game_time < end_time:
    current_time = time.time()
    time_until_upgrade = current_time + 5

    # Repeatedly click the cookie for 5 seconds
    while current_time < time_until_upgrade:
        cookie.click()
        current_time = time.time()

    # Update game stats and check for available upgrades
    update_stats()
    upgrades_available = driver.find_elements(By.CLASS_NAME, "product.unlocked.enabled")

    # Buy the most expensive upgrades available (right to left)
    if upgrades_available:
        for upgrade in reversed(upgrades_available):
            update_cost()
            while cookie_money > cost:
                upgrade.click()
                update_stats()
                update_cost()

    # Refresh loop timer and show remaining time
    game_time = time.time()
    print(f"Minutes left: {(end_time - game_time)/60: .1f}")

# ========================================= End of Game =========================================
print(f"Congrats! Your total Cookies per Second was {cookies_per_second}")
driver.quit()

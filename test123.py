import requests
from selenium import webdriver
import psutil
import time
import os
import ctypes

def is_internet_connected(): #This function used to ensure that your internet is connected.
    try:
        # Attempt to connect to a well-known server (Google's public DNS)
        psutil.net_connections(kind='inet')
        return True
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        return False


def cappic():

    # URL of (Your)Github Profile
    url = 'https://github.com/Sakolkrit' #This i mine, so you need to change this URL into yours first

    # Send a GET request to the website
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
            
        driver = webdriver.Chrome('C:\webdriver\chromedriver.exe') #Directory of your Chrome driver
        driver.get(url)
        driver.maximize_window() # full size the website that we open though url variable
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # Scroll the screen to the place where github contribution presented.
        driver.save_screenshot('screenshot555.png') # Screenshot that position, name the picture as screenshot555.png
        time.sleep(2)
        ctypes.windll.user32.SystemParametersInfoW(20, 0,os.path.abspath(r"C:\Users\M S I\OneDrive\Desktop\testpy123\github_contribution\screenshot555.png") , 0) #Put it into your desktop screen, from the directory of the previous screenshot picture
        time.sleep(2)

        # Close the webdriver
        driver.quit()
            

    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

def main():
    previous_status = False  # Initialize with no internet connection

    while True:
        current_status = is_internet_connected()

        if current_status and not previous_status:
            # Internet connection established
           cappic()
           break
        previous_status = current_status
        time.sleep(1)  # Check every 1 second (adjust as needed)

if __name__ == "__main__":
    main()
time.sleep(10)
import pyautogui as pyg
import webbrowser as wb
import datetime
import time
import click

def join_meeting(zoom_link):

    # zoom app related
    wb.get(using='chrome').open(zoom_link, new=2) #open zoom link in a new window
    time.sleep(5) # given time for the link to show app top-up window
    pyg.click(x=805, y=254, clicks=1, interval=0, button='left') # click on open zoom.app option
    time.sleep(10) # wait for 10 sec
    pyg.click(x=195, y=31, clicks=1, interval=0, button='left') # maximize zoom app
    time.sleep(3) # wait for 3 sec
    pyg.click(x=50, y=776, clicks=1, interval=0, button='left')

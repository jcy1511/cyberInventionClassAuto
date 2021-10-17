from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def auto(a,u) : #a는 차시수, u는 강의 목록 세가지 중에서 순서 (0부터)
    with open("idpw.txt","r") as e :
        id,pw = e.readlines()
    id = id.strip()
    print(id,pw)
    browser = webdriver.Chrome("./chromedriver.exe")
    browser.get("https://daegusci.ipacademy.net/")

    elem = browser.find_element_by_id("sso.ID")
    elem.send_keys(id)
    elem = browser.find_element_by_id("sso.PW")
    elem.send_keys(pw)
    elem = browser.find_element_by_class_name("btn_login")
    elem.click()

    time.sleep(3)

    elem = browser.find_element_by_xpath(f"//*[@id='contents']/div/form/table/tbody/tr[{u+1}]/td[1]/a")
    elem.click()




    for p in range(2,a+2) :
        browser.switch_to.window(browser.window_handles[1])
        time.sleep(2)
        elem = browser.find_element_by_xpath(f"//*[@id='ItemList']/table/tbody/tr[{p}]/td[2]/a")
        elem.click()

        browser.switch_to.window(browser.window_handles[3])
        browser.switch_to.frame("contents")

        time.sleep(3)

        while True :
            time_tol = browser.find_element_by_xpath("//*[@id='fs-footer']/div/div[1]/div[1]/ul/li[3]").text
            time_cur = browser.find_element_by_xpath("//*[@id='fs-footer']/div/div[1]/div[1]/ul/li[1]").text
            page_current = browser.find_element_by_xpath("//*[@id='fs-footer']/div/div[1]/div[3]/ul/li[2]").text
            page_total = browser.find_element_by_xpath("//*[@id='fs-footer']/div/div[1]/div[3]/ul/li[4]").text
            if time_tol == time_cur :
                if page_total != page_current :
                    elem = browser.find_element_by_xpath("//*[@id='fs-footer']/div/div[1]/div[3]/ul/li[5]")
                    elem.click()
                else :
                    break
            time.sleep(1)

    browser.close()
        



def auto2(s,e) : # s차시부터 e차시까지
    with open("idpw.txt","r") as f :
        id,pw = f.readlines()
    id = id.strip()
    print(id,pw)
    browser = webdriver.Chrome("./chromedriver.exe")
    browser.get("https://daegusci.ipacademy.net/")

    elem = browser.find_element_by_id("sso.ID")
    elem.send_keys(id)
    elem = browser.find_element_by_id("sso.PW")
    elem.send_keys(pw)
    elem = browser.find_element_by_class_name("btn_login")
    elem.click()

    time.sleep(3)

    elem = browser.find_element_by_xpath("//*[@id='contents']/div/form/table/tbody/tr[3]/td[1]/a")
    elem.click()

    for p in range(s+1,e+2) :
        browser.switch_to.window(browser.window_handles[1])
        time.sleep(2)
        elem = browser.find_element_by_xpath(f"//*[@id='ItemList']/table/tbody/tr[{p}]/td[2]/a")
        elem.click()

        time.sleep(1)
        
        browser.switch_to.window(browser.window_handles[3])
        WebDriverWait(browser, 3).until(EC.alert_is_present())
        alert = browser.switch_to.alert
        alert.accept()

        elem = browser.find_element_by_xpath("//*[@id='player-container']/div[2]/div[2]/div/ul/li[5]") #2배속
        elem.click() 

        time.sleep(3)

        while True :
            time_tol = browser.find_element_by_xpath("//*[@id='jp_container_2']/div/div/div[4]/div[2]").text
            time_cur = browser.find_element_by_xpath("//*[@id='jplayer_current_time']").text
            if time_cur == "00:00" :
                break
            time.sleep(1)
        


    browser.close()

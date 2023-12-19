from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import traceback
import warnings
warnings.filterwarnings('ignore')

def login(driver, username, password, retry=0):
    if retry == 3:
        raise ValueError('login failed.')
    
    print('login...')
    url = 'https://988660.cc/h5/index/login'
    driver.get(url)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[4]/button[1]')))
    driver.find_element_by_id('unm').send_keys(username)
    time.sleep(0.1)
    driver.find_element_by_id('pwd').send_keys(password)
    time.sleep(0.1)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div[4]/button[1]').click()
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="v7"]/a/div[1]/img')))
        print('login succesfully.')
    except:
        print('Retrying...')
        login(driver, username, password, retry+1)
        
    time.sleep(3)
        
        
# 签到
def checkin(driver):
    try:
        wait = WebDriverWait(driver, 10)
        
        # 使用WebDriverWait等待元素可见
        button2 = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="v7"]/a/div[1]/img')))
        
        # 检查button是否有效，可点击
        if button2.is_enabled():
            button2.click()
        else:
            raise RuntimeError("Button2 is disabled or not clickable")
        time.sleep(3)
        print('签到成功！')
    except Exception as e:
        print('签到失败！')
        traceback.print_exc()
        

def run(driver, username, password):
    login(driver, username, password)
    checkin(driver)
    
if __name__ == '__main__':
    pass

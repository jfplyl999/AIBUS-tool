from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 创建一个Chrome浏览器实例
driver = webdriver.Chrome()

# 打开登录页面
driver.get("https://8660ggg.cc/#/")

# 第一步：检查是否有元素<uni-view data-v-d1f0eada="" class="task-close">
try:
    task_close = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "task-close"))
    )
    task_close.click()
except:
    pass

# 第二步：检查是否有元素<img src="./static/images/icon/login.png" draggable="false">
try:
    login_icon = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "img[src='./static/images/icon/login.png']"))
    )
    login_icon.click()
except:
    print("错误1")
    driver.quit()
    exit()

# 第三步：检查是否有元素<input maxlength="140" step="" enterkeyhint="done" autocomplete="off" type="" class="uni-input-input">
try:
    username_input = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.CLASS_NAME, "uni-input-input"))
    )
    username_input.send_keys("username")
except:
    print("账号错误")
    driver.quit()
    exit()

# 第四步：检查是否有元素<input maxlength="140" step="" enterkeyhint="done" autocomplete="off" type="password" class="uni-input-input">
try:
    password_input = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='password'][class='uni-input-input']"))
    )
    password_input.send_keys("password")
except:
    print("账号错误")
    driver.quit()
    exit()

# 第五步：检查是否有元素<uni-view data-v-0d8a3f1a="" class="tologin">
try:
    tologin = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "tologin"))
    )
    tologin.click()
except:
    print("登录错误")
    driver.quit()
    exit()

# 第六步：检查是否有元素<uni-view data-v-4d574c0c="" class="sign-close">
try:
    sign_close = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "sign-close"))
    )
    print("登录成功")
except:
    pass

# 关闭浏览器
driver.quit()

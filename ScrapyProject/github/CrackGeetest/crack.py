import time
from io import BytesIO
from PIL import Image
from selenium import webdriver
from chaojiying import ChaojiyingClient
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ACCOUNT = 'simplelikeme'
PASSWORD = 'simple1'
BORDER = 6
INIT_LEFT = 60

CJY_USERNAME = "simple"
CJY_PASSWORD = "simple123"
CJY_SOFT_ID = "901576"


class CrackGeetest():
    def __init__(self):
        self.url = 'https://my.cn.china.cn/manage.php?op=LoginShowNew'
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser, 20)
        self.email = ACCOUNT
        self.password = PASSWORD
        self.chaojiying = ChaojiyingClient(CJY_USERNAME, CJY_PASSWORD, CJY_SOFT_ID)

    def __del__(self):
        self.browser.close()

    def open_image(self, path):
        f = open(path, mode='rb')
        img = f.read()
        f.close()
        return img

    def get_geetest_button(self):
        """
        获取初始验证按钮
        :return:
        """
        button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'geetest_radar_tip')))
        return button
    
    def get_position(self):
        """
        获取验证码位置
        :return: 验证码位置元组
        """
        img = self.wait.until(EC.presence_of_element_located((By.ID, 'showCaptcha')))
        time.sleep(2)
        location = img.location
        size = img.size
        top, bottom, left, right = location['y'], location['y'] + size['height'], location['x'], location['x'] + size[
            'width']
        return (top, bottom, left, right)
    
    def get_screenshot(self):
        """
        获取网页截图
        :return: 截图对象
        """
        screenshot = self.browser.get_screenshot_as_png()
        screenshot = Image.open(BytesIO(screenshot))
        return screenshot
    
    def get_slider(self):
        """
        获取滑块
        :return: 滑块对象
        """
        slider = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'geetest_slider_button')))
        return slider
    
    def get_geetest_image(self, name='captcha.png'):
        """
        获取验证码图片
        :return: 图片对象
        """
        top, bottom, left, right = self.get_position()
        print('验证码位置', top, bottom, left, right)
        screenshot = self.get_screenshot()
        captcha = screenshot.crop((left, top, right, bottom))
        captcha.save(name)
        return captcha
    
    def open(self):
        """
        打开网页输入用户名密码
        :return: None
        """
        # 打开浏览器登陆页面
        self.browser.get(self.url)
        # 获取账号输入框
        email = self.wait.until(EC.presence_of_element_located((By.ID, 'userName')))
        # 获取密码输入框
        password = self.wait.until(EC.presence_of_element_located((By.ID, 'userPassword')))
        # 输入账号
        email.send_keys(self.email)
        # 输入密码
        password.send_keys(self.password)
        # 获取验证码输入框
        img = self.wait.until(EC.presence_of_element_located((By.ID, 'verifystr')))
        # 获取验证码
        self.get_geetest_image(name="login.png")
        time.sleep(0.1)
        image = self.open_image("login.png")
        img_num = self.chaojiying.PostPic(image, 1902).get("pic_str")
        # 输入验证码
        img.send_keys(img_num)
        # 获取登陆按钮
        submit = self.wait.until(EC.presence_of_element_located((By.ID, 'btn')))
        submit.click()
        time.sleep(10)

    def get_gap(self, image1, image2):
        """
        获取缺口偏移量
        :param image1: 不带缺口图片
        :param image2: 带缺口图片
        :return:
        """
        left = 60
        for i in range(left, image1.size[0]):
            for j in range(image1.size[1]):
                if not self.is_pixel_equal(image1, image2, i, j):
                    left = i
                    return left
        return left
    
    def is_pixel_equal(self, image1, image2, x, y):
        """
        判断两个像素是否相同
        :param image1: 图片1
        :param image2: 图片2
        :param x: 位置x
        :param y: 位置y
        :return: 像素是否相同
        """
        # 取两个图片的像素点
        pixel1 = image1.load()[x, y]
        pixel2 = image2.load()[x, y]
        threshold = 60
        if abs(pixel1[0] - pixel2[0]) < threshold and abs(pixel1[1] - pixel2[1]) < threshold and abs(
                pixel1[2] - pixel2[2]) < threshold:
            return True
        else:
            return False
    
    def get_track(self, distance):
        """
        根据偏移量获取移动轨迹
        :param distance: 偏移量
        :return: 移动轨迹
        """
        # 移动轨迹
        track = []
        # 当前位移
        current = 0
        # 减速阈值
        mid = distance * 4 / 5
        # 计算间隔
        t = 0.2
        # 初速度
        v = 0
        
        while current < distance:
            if current < mid:
                # 加速度为正2
                a = 2
            else:
                # 加速度为负3
                a = -3
            # 初速度v0
            v0 = v
            # 当前速度v = v0 + at
            v = v0 + a * t
            # 移动距离x = v0t + 1/2 * a * t^2
            move = v0 * t + 1 / 2 * a * t * t
            # 当前位移
            current += move
            # 加入轨迹
            track.append(round(move))
        return track
    
    def move_to_gap(self, slider, track):
        """
        拖动滑块到缺口处
        :param slider: 滑块
        :param track: 轨迹
        :return:
        """
        ActionChains(self.browser).click_and_hold(slider).perform()
        for x in track:
            ActionChains(self.browser).move_by_offset(xoffset=x, yoffset=0).perform()
        time.sleep(0.5)
        ActionChains(self.browser).release().perform()
    
    def login(self):
        """
        登录
        :return: None
        """
        submit = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'login-btn')))
        submit.click()
        time.sleep(3)
        print('登录成功')
    
    def crack(self):
        # 输入用户名密码
        # self.open()
        # home = self.browser.find_element_by_xpath("//div[@class='brand']/a")
        # # 执行js访问主页
        # self.browser.execute_script("arguments[0].click();", home)

        url = 'https://cn.china.cn/'
        self.browser.get(url)
        # time.sleep(10)
        # 获取搜索框搜索
        self.wait.until(EC.element_to_be_clickable((By.ID, 'keyinput'))).send_keys("智能设备")
        # 找到公司搜索
        button = self.browser.find_element_by_xpath("//ul[@class='serch-items']/li[2]")
        # 执行js搜索公司
        self.browser.execute_script("arguments[0].click();", button)
        time.sleep(1)
        provinces = self.browser.find_elements_by_xpath("//div[@class='branlist-view']/ul/li/a")
        n = len(provinces) - 1
        print(provinces)
        for i in range(n):
            provinces = self.browser.find_elements_by_xpath("//div[@class='branlist-view']/ul/li/a")
            provinces[n - i].click()
            cities = self.browser.find_elements_by_xpath("//div[contains(@class,'ctg-mod-brancate')][2]//ul/li/a")
            cn = len(cities) - 1
            print(cities)
            for j in range(cn):
                cities = self.browser.find_elements_by_xpath("//div[contains(@class,'ctg-mod-brancate')][2]//ul/li/a")
                cities[cn - j].click()
                print(self.browser.current_url)
                companies = self.browser.find_elements_by_xpath("//div[@class='corpinfo']/h3/a")
                cpn = len(companies) - 1
                # 访问公司主页
                for i in range(cpn):
                    companies = self.browser.find_elements_by_xpath("//div[@class='corpinfo']/h3/a")
                    companies[i].click()
                    print(self.browser.current_url)
                    self.browser.back()
                    time.sleep(1)

                self.browser.find_element_by_class_name("rollPage").click()
                time.sleep(1)

            companies = self.browser.find_elements_by_xpath("//div[@class='corpinfo']/h3/a")
            cpn = len(companies) - 1
            # 访问公司主页
            for i in range(cpn):
                companies = self.browser.find_elements_by_xpath("//div[@class='corpinfo']/h3/a")
                companies[i].click()
                print(self.browser.current_url)
                self.browser.back()
                time.sleep(1)

        # # 点击验证按钮
        # button = self.get_geetest_button()
        # button.click()
        # # 获取验证码图片
        # image1 = self.get_geetest_image('captcha1.png')
        # # 点按呼出缺口
        # slider = self.get_slider()
        # slider.click()
        # # 获取带缺口的验证码图片
        # image2 = self.get_geetest_image('captcha2.png')
        # # 获取缺口位置
        # gap = self.get_gap(image1, image2)
        # print('缺口位置', gap)
        # # 减去缺口位移
        # gap -= BORDER
        # # 获取移动轨迹
        # track = self.get_track(gap)
        # print('滑动轨迹', track)
        # # 拖动滑块
        # self.move_to_gap(slider, track)
        #
        # success = self.wait.until(
        #     EC.text_to_be_present_in_element((By.CLASS_NAME, 'geetest_success_radar_tip_content'), '验证成功'))
        # print(success)
        #
        # # 失败后重试
        # if not success:
        #     self.crack()
        # else:
        #     self.login()


if __name__ == '__main__':
    crack = CrackGeetest()
    crack.crack()

import requests
from selenium import webdriver  # 用来驱动浏览器的
from selenium.webdriver.common.keys import Keys
import time
import os
import pprint
'''
===============所有方法===================
    element是查找一个标签
    elements是查找所有标签

    1、find_element_by_link_text  通过链接文本去找
    2、find_element_by_id 通过id去找
    3、find_element_by_class_name
    4、find_element_by_partial_link_text
    5、find_element_by_name
    6、find_element_by_css_selector
    7、find_element_by_tag_name
'''



# try:

# 往百度发送请求
pic_num = []
def ppbc(id):
    path = './38/'+id
    if os.path.exists(path):
        pass
    else:
        os.mkdir(path)
    driver.get('http://ppbc.iplant.cn/sp/'+ id)
    driver.implicitly_wait(10)
    # print("将页面拉到最上方")
    # time.sleep(5)
    # driver.execute_script("window.scrollTo(0,0);")
    # time.sleep(5)

    # 将页面向下拉取40000像素
    print("将页面向下拉取到底")
    time.sleep(5)
    for i in range(10):
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        print(i)
        time.sleep(20)
    time.sleep(10)
    # login_button = driver.find_element_by_partial_link_text('一年蓬')   # 找网页含有“一年蓬”的链接
    # login_button.click()
    # print(login_button.tag_name)   # 整个网页的代码

    # pageSource = driver.page_source   # 整个网页的代码
    # pprint.pprint(pageSource)
    count = 0  #统计次数，剔除前几个链接
    for link in driver.find_elements_by_tag_name("img"):
        # print(link.text)
        print(link.get_attribute("src"))
        img_url = link.get_attribute("src")
        count = count+1
        if count>7:
            img_url_list = img_url.split("/")
            img_url_jpg = img_url_list[-1]
            img_url_jpg_list = img_url_jpg.split(".")
            img_url = img_url_jpg_list[0]
            print(count-7, end=" ")
            print( ":" + img_url)
            s_id = img_url
            headers={
                'Referer':'http://ppbc.iplant.cn/tu/' + s_id
            }
            img_name_path = './38/'+id + "/" + s_id +'.jpg'
            img_url = "http://img9.iplant.cn/image61/b/" + s_id + ".jpg"
            page = requests.get(img_url,headers= headers)
            img = page.content
            with open(img_name_path ,mode='wb') as f:
                f.write(img)
    pic_num.append(count-7)
    time.sleep(10)

def find_id(name_id):
    driver.get('http://ppbc.iplant.cn/')
    driver.implicitly_wait(10)
    className = driver.find_element_by_class_name('field1')  # 使用class="s_ipt"定位

    className.send_keys(name_id)  # 输入贵州财经大学
    className.send_keys(Keys.ENTER)  # 注意Keys,K是大写
    currentPageUrl = driver.current_url
    id = currentPageUrl.split("/")[-1]
    return id


if __name__ == '__main__':
    # 获取驱动对象
    driver = webdriver.Chrome()
    # nane_id = [
    # "节节草", "问荆", "饭包草","白茅","狗牙根","牛筋草","马唐","虮子草","香附子","葎草",
    # "杠板归", "藜","牛膝", "反枝苋","木防己","救荒野豌豆","广布野豌豆","野老鹳草",
    # "乌蔹莓", "野胡萝卜", "萝藦", "鸡矢藤","打碗花", "圆叶牵牛","小蓬草","苍耳","泥胡菜","鳢肠"]
    nane_id = ["苍耳"]
    for name in nane_id:
        id = find_id(name)
        print(id)
        ppbc(id)
    print(pic_num)
    print("爬取完成！")
# finally:
#     driver.close()



# 保存图片
# s_id = "2129873"
#
# headers={
#     'Referer':'http://ppbc.iplant.cn/tu/' + s_id
# }
#
# img_name_path = './38/'+ s_id +'.jpg'
# img_url = "http://img9.iplant.cn/image61/b/" + s_id + ".jpg"
# page = requests.get(img_url,headers= headers)
# img = page.content
# with open(img_name_path ,mode='wb') as f:
#     f.write(img)
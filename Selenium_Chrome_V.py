
# Selenium　对应谷歌浏览器的驱动版本2.31
＃下载地址  http://chromedriver.storage.googleapis.com/index.html?path=2.31/


# Chrome 版本58
# 下载地址　　https://www.slimjet.com/chrome/google-chrome-old-version.php


# 可使用下面脚本请求页面


def get_first_page():

    url = 'https://movie.douban.com/celebrity/1275260/photos/'


    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome("/usr/bin/chromedriver", chrome_options=options)
    driver.get(url)
    html = driver.page_source
    return html

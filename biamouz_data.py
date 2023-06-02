import re

persian_leters = '''ءاآبپتثجچحخدذرزژسشصضطظعغفقکگلمنوهیئ'''
words_countainer_xpath = '//*[@id="page-content"]/div/div/div[1]/div/ul'
english_word_xpath = '//*[@id="page-content"]/div/div/div[1]/div/ul/li[{num}]/div/div[1]/a/div'
mean_xpath = '//*[@id="page-content"]/div/div/div[1]/div/ul/li[{num}]/div/div[2]'

url_countainer_xpath = '//*[@id="page-content"]/div/div'
url_xpath = '//*[@id="page-content"]/div/div/div[{num}]/div/div[3]/a'

_web_driver_cache = None

def _get_web_driver ():
    global _web_driver_cache
    if _web_driver_cache :
        return _web_driver_cache
    from selenium import webdriver
    print('    opening webdriver...')
    _web_driver_cache = webdriver.Chrome()
    return _web_driver_cache


def get_data (*biamouz_urls:str):
    data = []
    driver = _get_web_driver()
    for url in biamouz_urls:
        print(f'    opening {url}:')
        driver.get(url)
        print(f'    fetching {url}:')
        countainer_el = driver.find_element(by='xpath', value=words_countainer_xpath)
        words_num = countainer_el.find_elements(by='tag name', value='li').__len__()
        for num in range(1,words_num+1):
            eng  = driver.find_element(by='xpath', value=english_word_xpath.format(num=num)).text
            mean = driver.find_element(by='xpath', value=mean_xpath.format(num=num)).text

            mean = re.sub(r'\u200c',' ',mean)

            print(f'        Found {num} words', end='\r')

            data.append((eng,mean))
        print()
    return data


def fetch_countainer (url):
    driver = _get_web_driver()
    
    print(f'    opening {url} for find urls')
    driver.get(url)
    
    urls = []
    urls_num = driver.find_elements(by='xpath', value=url_countainer_xpath+'/*').__len__()
    for num in range(1,urls_num+1):
        url_el = driver.find_element(by='xpath',value=url_xpath.format(num=num))
        _url = url_el.get_attribute('href')
        print(f'        Found {num} urls', end='\r')

        urls.append(_url)
    print()
    return urls



'''
//*[@id="page-content"]/div/div/div[1]/div/ul/li[1]/div
//*[@id="page-content"]/div/div/div[1]/div/ul/li[2]/div
//*[@id="page-content"]/div/div/div[1]/div/ul/li[127]/dev
'''

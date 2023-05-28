import re

persian_leters = '''ءاآبپتثجچحخدذرزژسشصضطظعغفقکگلمنوهیئ'''
countainer_xpath = '//*[@id="page-content"]/div/div/div[1]/div/ul'
english_word_xpath = '//*[@id="page-content"]/div/div/div[1]/div/ul/li[{num}]/div/div[1]/a/div'
mean_xpath = '//*[@id="page-content"]/div/div/div[1]/div/ul/li[{num}]/div/div[2]'


def get_data (*biamouz_urls:str):
    data = []
    from selenium import webdriver
    print('    opening webdriver...')
    driver = webdriver.Chrome()
    for url in biamouz_urls:
        print(f'    opening {url}:')
        driver.get(url)
        print(f'    fetching {url}:')
        countainer_el = driver.find_element(by='xpath', value=countainer_xpath)
        words_num = countainer_el.find_elements(by='tag name', value='li').__len__()
        for num in range(1,words_num+1):
            eng  = driver.find_element(by='xpath', value=english_word_xpath.format(num=num)).text
            mean = driver.find_element(by='xpath', value=mean_xpath.format(num=num)).text

            mean = re.sub(r'\u200c',' ',mean)

            print(f'        Found {num} words', end='\r')

            data.append((eng,mean))
        print()
    return data



'''
//*[@id="page-content"]/div/div/div[1]/div/ul/li[1]/div
//*[@id="page-content"]/div/div/div[1]/div/ul/li[2]/div
//*[@id="page-content"]/div/div/div[1]/div/ul/li[127]/dev
'''

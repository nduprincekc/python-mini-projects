from selenium import webdriver
import time
import random
def you():
    driver = webdriver.Chrome("C:\\Users\\us er\\Desktop\\e\\chromedriver.exe")

    video =['https://www.youtube.com/watch?v=NzoDxzXbb-E',
            'https://www.youtube.com/watch?v=ihA6oNCp5xs',
            'https://www.youtube.com/watch?v=ubq7KzxXUpU']

    for i in range(10):
        print('Running the video for {} time'.format(i))
        random_video = random.randint(0,2)
        driver.get(video[random_video])
        #time.sleep(2)

    driver.quit()
#x    679069545
# https://api.telegram.org/bot1170731835:AAEazRdKRShQ65TfGNc5ODohQ2LHvKrJSHA/sendMessage?chat_id=-679069545&text="kcemm"
you()

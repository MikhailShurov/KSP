from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By

import telebot

from time import sleep


bot = telebot.TeleBot('5302087727:AAGDn7_L7mU9rVg7j4VOIaT2iC3Xg5rv2fY')

login = '375445471743'
password = '10bg277'

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f'user-agent={user_agent}')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

browser = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)


@bot.message_handler(commands=['start'])
def send_information(message):
    bot.send_message(message.chat.id, 'Введите фамилию человека, чей долг вы хотите узнать')
    bot.register_next_step_handler(message, get_information_by_surname)


def get_information_by_surname(surname):
    try:
        browser.get('https://ipay.znaj.by/sso/page/login?auth_return_url=/school/!sso_client.authentication&lang=ru')
        browser.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')
    except:
        browser.get('https://ipay.znaj.by/sso/page/login?auth_return_url=/school/!sso_client.authentication&lang=ru')
        login_form = browser.find_element(By.ID, 'login')
        login_form.find_element(By.NAME, 'Login').send_keys(login)
        login_form.find_element(By.NAME, 'Password').send_keys(password)
        sleep(3)
        login_form.find_element(By.TAG_NAME, 'button').click()

    sleep(5)
    students = browser.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')
    for i in range(len(students)):
        rows = students[i].find_elements(By.TAG_NAME, 'td')
        current_surname = rows[1].text.split(' ')[0]
        if current_surname == surname.text:
            bot.send_message(surname.chat.id, str(rows[7].text + ' руб.'))
            return
    bot.send_message(surname.chat.id, 'Возможно вы неправильно ввели фаимилию, проверьте и попробуйте ещё раз')
    return


if __name__ == '__main__':
    bot.infinity_polling()

# KSP

This telegram bot is just a school project.

It was created to track balance of my classmates. 

Using selenium it logs in to "https://ipay.znaj.by/sso/page/login" with login and password. Then find table with balances and send its cell with the help of telebot. It was pushed to Heroku and worked there.

## Principle of operation

### main.py

Seting up options to webdriver and installing it:
```
chrome_options.add_argument(f'user-agent={user_agent}')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

browser = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
```

Start function to telegram bot which gets surname of student to find his balance:
```
@bot.message_handler(commands=['start'])
...
```

In lines 34-43 bot logs in to site

Find a table with balances:
```
students = browser.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')
```

And then find balance and send it using telebot:
```
bot.send_message(surname.chat.id, str(rows[7].text + ' руб.'))
```

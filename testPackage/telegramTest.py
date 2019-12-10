import requests


# 텔레그램 봇에 메시지 보내는 함수
def telegram_bot_sendtext(bot_message):
    bot_token = '327497093:AAGJCRubUJv36_rwbD2Ul4D_DkXoA-ZORag'
    bot_chatID = '51404588'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


test = telegram_bot_sendtext("Testing Telegram bot")
print(test)
print(test['ok'])
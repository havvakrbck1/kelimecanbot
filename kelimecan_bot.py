print("Bot başlatılıyor...")

import logging
logging.basicConfig(level=logging.DEBUG)

import telebot
import random

TOKEN = '8021903015:AAEwBMVSzdFnlM5BcjtEFIw3GRCCoYwsofs'  
bot = telebot.TeleBot(TOKEN)


def kelimeleri_al():
    with open('kelimeler.txt', 'r', encoding='utf-8') as file:
        kelimeler = file.read().splitlines()
    return kelimeler

kelimeler = kelimeleri_al() 

oyuncular = {} 


@bot.message_handler(commands=['basla'])
def baslat(message):
    user_id = message.from_user.id
    orijinal = random.choice(kelimeler)  
    karisik = ''.join(random.sample(orijinal, len(orijinal)))  

 
    if user_id not in oyuncular:
        oyuncular[user_id] = {'kelime': orijinal, 'puan': 0}

    bot.reply_to(message, f"Hadi başlayalım! Bu harflerle anlamlı bir kelime bul: 🔤 {karisik}")


@bot.message_handler(func=lambda m: True)
def kontrol_et(message):
    user_id = message.from_user.id

   
    if user_id in oyuncular:
        cevap = message.text.lower()  
        dogru_kelime = oyuncular[user_id]['kelime']  

        if cevap == dogru_kelime:
            oyuncular[user_id]['puan'] += 1  
            bot.reply_to(message, f"🎉 Doğru! Puanın: {oyuncular[user_id]['puan']}")
        else:
            bot.reply_to(message, f"❌ Yanlış. Doğru kelime: {dogru_kelime}")
        
     
        orijinal = random.choice(kelimeler)  
        karisik = ''.join(random.sample(orijinal, len(orijinal))) 
        oyuncular[user_id]['kelime'] = orijinal 
        bot.reply_to(message, f"Yeni kelime: 🔤 {karisik}")

bot.polling(none_stop=True)


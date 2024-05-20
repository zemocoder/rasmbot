"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging
import requests
from aiogram import Bot, Dispatcher, executor, types 
import _tugma as nav
from _tugma import *
import random

API_TOKEN = '5860263373:AAE03XMh6fAHM24weeez3OW6rorwRzC_Q_w'
botname = "@hayvonlar_rasmibot"


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
admin = 693313498
rek ={
  "photo": "",
  "text": "",
  "btnname": "",
  "url": ""
}

reklam = InlineKeyboardMarkup(row_width=2)

rekbtn = InlineKeyboardButton(text="Kirish ✅", url="https://t.me/hayvonlar_rasmibot" )
reklam.add(rekbtn)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    print(message.photo)
    joinedFile = open("user.txt","r")
    joinedUsers = set()
    for line in joinedFile:
       joinedUsers.add(line.strip())
    if not str(message.chat.id) in joinedUsers:
       joinedFile = open("user.txt","a")
       joinedFile.write(str(message.chat.id)+ "\n")
       joinedUsers.add(message.chat.id)
    await bot.send_photo(message.from_user.id, "https://w0.peakpx.com/wallpaper/368/742/HD-wallpaper-cool-cat.jpg", caption=" <i>Assalomu alaykum </i> <b>"+message.from_user.first_name + "</b> <i>hush kelibsiz bo'limlardan birini tanlang va sizga bot qiziqarli rasmlar jo\'natadi</i>",parse_mode="HTML", reply_markup=nav.mainMenu)


@dp.message_handler(commands=['admin'])
async def admin_panel(message : types.Message):
    if message.from_user.id == admin:
      await bot.send_photo(admin, "https://sliderzemo.cf/img/p3.jpg", caption="Salom Ezozbek hush kelibsiz Bot amringizga muntazir 😁",  reply_markup=nav.adminMenu)
    else:
      await bot.send_message(chat_id=message.from_user.id, text="<i> Kechirasiz </i> <b>" + str(message.from_user.first_name) + "</b> <i> siz admin emassiz 😝 \n \n Bot admini: @MrXayitov </i>", parse_mode="HTML")

@dp.message_handler(content_types=["photo"])
async def img(message : types.Message):
  photo_id = message.photo[-1].file_id
  rek["photo"] = photo_id
  await bot.send_photo(chat_id=message.from_user.id, photo=photo_id , caption=rek["text"], reply_markup=reklam)




@dp.message_handler()
async def ads(message: types.Message): 
  try:
      if message.chat.id == admin :
       if message.text.startswith('#caption'):
        removeXabar = message.text.replace("#caption", "")
        rek["text"] = removeXabar
  except Exception as e:
    print(e)
@dp.message_handler()
async def ads(message: types.Message): 
  try:
      if message.chat.id == admin :
        if message.text.startswith('#btn'):
          removeXabar = message.text.replace("#btn", "")
          rek["btnname"] = removeXabar
  except Exception as e:
    print(e)


@dp.message_handler()
async def ads(message: types.Message): 
  try:
      if message.chat.id == admin :
       if message.text.startswith('#url'):
        removeXabar = message.text.replace("#url", "")
        rek["url"] = removeXabar
  except Exception as e:
    print(e)

@dp.message_handler()
async def sendWiki(message: types.Message): 
  try:
    if message.chat.id == admin :
      if message.text.startswith('#xabar'):
        for user_s in open('user.txt'):
         print(rek)
         await bot.send_photo(chat_id=user_s, photo=rek["photo"], caption=rek["text"], reply_markup=reklam, parse_mode="HTML"  )
  except :
    return True







@dp.callback_query_handler(text="btnRandom")
async def randomize(message: types.Message):
  link = 'https://dog.ceo/api/breeds/image/random'
  response = requests.get(link)
  itlar= response.json()
  xbr=itlar['message']

  # await bot.delete_message(message.from_user.id, message_id=types.Message.delete_reply_markup(self=btnRandom))
  await bot.send_photo(message.from_user.id, xbr , caption="Kuchuklar ❤️", reply_markup=nav.mainMenu)
  # print(message.message_id.as_integer_ratio())  
# MUSHUKLAR
@dp.callback_query_handler(text="btnRandom2")
async def randomize(message: types.Message):
  link = 'https://api.thecatapi.com/v1/images/search?limit=1'
  response = requests.get(link)
  itlar= response.json()
  xbr=""
  for i in itlar :
    xbr+=i['url']
  # xbr=mushuklar['message']
  
  await bot.send_photo(message.from_user.id, xbr , caption="Mushuklar ❤️", reply_markup=nav.mainMenu)
  # await bot.delete_message(message.from_user.id, message_id=types.Message.delete_reply_markup(self=btnRandom))
  # print(message.message_id.as_integer_ratio())  
# STATISTIKA
@dp.callback_query_handler(text_contains='stats')
async def stat(call: types.CallbackQuery):
    # if call.message.chat.id == admin :
    
        d = sum(1 for line in open('user.txt'))
        await bot.send_message(chat_id=call.message.chat.id, text="<i>👨🏻‍💻 Obunachilar soni - </i> <b>"+str(d)+" </b>  ta. \n \n 📊 "+botname+" <i> statistikasi  </i>",parse_mode="HTML")

@dp.callback_query_handler(text_contains='sendmsg')
async def stat(call: types.CallbackQuery):
    if call.message.chat.id == admin :

      for xabarla in open('message.txt'):
        await bot.send_message(chat_id=admin, text=xabarla, parse_mode="HTML")
          
@dp.callback_query_handler(text="btnRandom3")
async def randomize(message: types.Message):
  try:
      taxmin = random.randint(1, 19)
      link = 'https://pixabay.com/api/?key=32452369-fb4ecba71876a7c19595878f8&q=snakes&image_type=photo&pretty='+str(taxmin)
      response = requests.get(link)
      itlar= response.json()
      hts = itlar["hits"]
      lists = []
      # taxmin = random.randint(1, 20)
      # print(taxmin, message.from_user.first_name)
      for n in hts:
        lists.append(n["largeImageURL"])

      await bot.send_photo(message.from_user.id, lists[taxmin] , caption="Ilonlar 🐍", reply_markup=nav.mainMenu)
  except:
    await bot.send_photo(message.from_user.id, lists[taxmin] , caption="Ilonlar 🐍", reply_markup=nav.mainMenu)

          

@dp.callback_query_handler(text="btnRandom4")
async def randomize(message: types.Message):
  taxmin = random.randint(1, 20)
  link = 'https://pixabay.com/api/?key=32452369-fb4ecba71876a7c19595878f8&q=rabbit&image_type=photo&pretty='+str(taxmin)
  response = requests.get(link)
  itlar= response.json()
  hts = itlar["hits"]
  lists = []
  # print(taxmin)
  
  for n in hts:
    lists.append(n["largeImageURL"])

  await bot.send_photo(message.from_user.id, lists[taxmin] , caption="Quyonlar 🐇", reply_markup=nav.mainMenu)


@dp.callback_query_handler(text="btnRandom5")
async def randomize(message: types.Message):
  taxmin = random.randint(1, 20)
  link = 'https://pixabay.com/api/?key=32452369-fb4ecba71876a7c19595878f8&q=animal+mouse&image_type=photo&pretty='+str(taxmin)
  response = requests.get(link)
  itlar= response.json()
  hts = itlar["hits"]
  lists = []
  print(taxmin)
  for n in hts:
    lists.append(n["largeImageURL"])

  await bot.send_photo(message.from_user.id, lists[taxmin] , caption="Sichqonlar  🐁", reply_markup=nav.mainMenu)

@dp.callback_query_handler(text="btnRandom6")
async def randomize(message: types.Message):
  taxmin = random.randint(1, 19)
  link = 'https://pixabay.com/api/?key=32452369-fb4ecba71876a7c19595878f8&q=birds&image_type=photo&pretty='+str(taxmin)
  response = requests.get(link)
  itlar= response.json()
  hts = itlar["hits"]
  lists = []
  for n in hts:
    lists.append(n["largeImageURL"])

  await bot.send_photo(message.from_user.id, lists[taxmin] , caption="Qushlar  🦚", reply_markup=nav.mainMenu)

@dp.callback_query_handler(text="boshqa")
async def edit(message : types.Message):
  await bot.send_photo(chat_id=message.from_user.id, photo="https://i.pinimg.com/564x/ba/92/7f/ba927ff34cd961ce2c184d47e8ead9f6.jpg", caption=" <i>Assalomu alaykum </i> <b>"+message.from_user.first_name + "</b> <i>hush kelibsiz bo'limlardan birini tanlang va sizga bot qiziqarli rasmlar jo\'natadi</i>",parse_mode="HTML", reply_markup=nav.bolm2)



@dp.callback_query_handler(text="otlar")
async def randomize(message: types.Message):
  taxmin = random.randint(1, 19)
  link = 'https://pixabay.com/api/?key=32452369-fb4ecba71876a7c19595878f8&q=horses&image_type=photo&pretty='+str(taxmin)
  response = requests.get(link)
  itlar= response.json()
  hts = itlar["hits"]
  lists = []
  for n in hts:
    lists.append(n["largeImageURL"])
  await bot.send_photo(message.from_user.id, lists[taxmin] , caption="Otlar 🐎", reply_markup=nav.bolm2)

@dp.callback_query_handler(text="pandalar")
async def randomize(message: types.Message):
  taxmin = random.randint(1, 19)
  link = 'https://pixabay.com/api/?key=32452369-fb4ecba71876a7c19595878f8&q=white+panda&image_type=photo&pretty='+str(taxmin)
  response = requests.get(link)
  itlar= response.json()
  hts = itlar["hits"]
  lists = []
  for n in hts:
    lists.append(n["largeImageURL"])
  await bot.send_photo(message.from_user.id, lists[taxmin] , caption="Pandalar 🐼", reply_markup=nav.bolm2)


@dp.callback_query_handler(text="pinvgin")
async def randomize(message: types.Message):
  taxmin = random.randint(1, 19)
  link = 'https://pixabay.com/api/?key=32452369-fb4ecba71876a7c19595878f8&q=pinguin&image_type=photo&pretty='+str(taxmin)
  response = requests.get(link)
  itlar= response.json()
  hts = itlar["hits"]
  lists = []
  for n in hts:
    lists.append(n["largeImageURL"])
  await bot.send_photo(message.from_user.id, lists[taxmin] , caption="Pingvinlar 🐧", reply_markup=nav.bolm2)


@dp.callback_query_handler(text="sherlar")
async def randomize(message: types.Message):
  taxmin = random.randint(1, 19)
  link = 'https://pixabay.com/api/?key=32452369-fb4ecba71876a7c19595878f8&q=lion&image_type=photo&pretty='+str(taxmin)
  response = requests.get(link)
  itlar= response.json()
  hts = itlar["hits"]
  lists = []
  for n in hts:
    lists.append(n["largeImageURL"])
  await bot.send_photo(message.from_user.id, lists[taxmin] , caption="Sherlar 🦁", reply_markup=nav.bolm2)

@dp.callback_query_handler(text="tovus")
async def randomize(message: types.Message):
  taxmin = random.randint(1, 19)
  link = 'https://pixabay.com/api/?key=32452369-fb4ecba71876a7c19595878f8&q=peacock&image_type=photo&pretty='+str(taxmin)
  response = requests.get(link)
  itlar= response.json()
  hts = itlar["hits"]
  lists = []
  for n in hts:
    lists.append(n["largeImageURL"])
  await bot.send_photo(message.from_user.id, lists[taxmin] , caption="Tovuslar 🦚", reply_markup=nav.bolm2)



@dp.callback_query_handler(text="tovuq")
async def randomize(message: types.Message):
  taxmin = random.randint(1, 19)
  link = 'https://pixabay.com/api/?key=32452369-fb4ecba71876a7c19595878f8&q=chicken&image_type=photo&pretty='+str(taxmin)
  response = requests.get(link)
  itlar= response.json()
  hts = itlar["hits"]
  lists = []
  for n in hts:
    lists.append(n["largeImageURL"])
  await bot.send_photo(message.from_user.id, lists[taxmin] , caption="Kulguli Tovuqlar 🐓 ", reply_markup=nav.bolm2)

@dp.callback_query_handler(text="ortga")
async def randomize(message: types.Message):

  await bot.send_photo(chat_id=message.from_user.id, photo="https://w0.peakpx.com/wallpaper/368/742/HD-wallpaper-cool-cat.jpg", caption="Siz orqaga qaytdingiz 😜", reply_markup=nav.mainMenu)





@dp.callback_query_handler(text="userfayl")
async def randomize(message: types.Message):
  with open("user.txt","rb") as mics:
    f=mics.read()
    await  bot.send_document(chat_id=admin, document=f)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True) 

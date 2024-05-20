from aiogram.types import InlineKeyboardMarkup , InlineKeyboardButton

mainMenu = InlineKeyboardMarkup(row_width=2)
bolm2 = InlineKeyboardMarkup(row_width=2)
adminMenu = InlineKeyboardMarkup(row_width=2)
btnRandom = InlineKeyboardButton(text="Kuchuklar 🐕"  , callback_data="btnRandom" )
btnRandom2 = InlineKeyboardButton(text="Mushuklar 🐈‍" , callback_data="btnRandom2")
btnRandom3 = InlineKeyboardButton(text="Ilonlar 🐍" , callback_data="btnRandom3")
btnRandom4 = InlineKeyboardButton(text="Quyonlar  🐇" , callback_data="btnRandom4")
btnRandom5 = InlineKeyboardButton(text="Sichqonlar  🐁" , callback_data="btnRandom5")
btnRandom6 = InlineKeyboardButton(text="Qushlar  🦚" , callback_data="btnRandom6")
statik = InlineKeyboardButton(text="Statistika 📊"  , callback_data="stats" )
foydalanuvchilar = InlineKeyboardButton(text="Foydalanuvchilar 👥" , callback_data="userfayl")
ikkibol = InlineKeyboardButton(text="Boshqa hayvonlar rasmi 🦫"  , callback_data="boshqa" )

mainMenu.row(btnRandom, btnRandom2)
mainMenu.row(btnRandom3,btnRandom4)
mainMenu.row(btnRandom5,btnRandom6)
mainMenu.add(ikkibol)
mainMenu.add(statik)



xabar_yuborish = InlineKeyboardButton(text="Xabarlar ✍️"  , callback_data="sendmsg" )
statlar = InlineKeyboardButton(text="Statistika 📊"  , callback_data="stats" )
adminMenu.insert(xabar_yuborish)
adminMenu.add(statlar)
adminMenu.add(foydalanuvchilar)


ikkibolm1 = InlineKeyboardButton(text="Otlar 🐎"  , callback_data="otlar" )
ikkibolm2 = InlineKeyboardButton(text="Pandalar 🐼"  , callback_data="pandalar" )
ikkibolm3 = InlineKeyboardButton(text="Pingvinlar 🐧"  , callback_data="pinvgin" )
ikkibolm4 = InlineKeyboardButton(text="Sherlar 🦁 "  , callback_data="sherlar" )
ikkibolm5 = InlineKeyboardButton(text="Tovuslar 🦚 "  , callback_data="tovus" )
ikkibolm6 = InlineKeyboardButton(text="Tovuqlar 🐓 "  , callback_data="tovuq" )
ikkibolm7 = InlineKeyboardButton(text="Orqaga 🔙 "  , callback_data="ortga" )
bolm2.row(ikkibolm1,ikkibolm2)
bolm2.row(ikkibolm3,ikkibolm4)
bolm2.row(ikkibolm5,ikkibolm6)
bolm2.add(ikkibolm7)



import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.types import LabeledPrice, PreCheckoutQuery, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from aiogram.filters.command import Command
from aiogram import F
from aiogram.types import FSInputFile 
import sqlite3
import aiohttp
import logging


#db = sqlite3.connect('main.db')
#c = db.cursor()

TOKEN = "7568250713:AAFv0gXCEtfkhXW8pGO_WO6PGL9QpYh7-LU"
bot = Bot(TOKEN)
dp = Dispatcher()

user_id = 0
chat_id = 0
username = ''

CHANNEL_ID = "-1002253618063"

@dp.message(CommandStart())
async def start(message: types.Message):
    
    global user_id
    global chat_id
    global username
    
    
    user_id = message.from_user.id
    chat_id = message.chat.id
    username = message.from_user.username
    
    await request_op(user_id, chat_id)
    
        
@dp.callback_query(F.data == 'buy')
async def calldata(call: CallbackQuery):
    await call.message.delete()
    
    btn1 = InlineKeyboardButton(text='✅ Проверить оплату ✅', callback_data='cheak_buy')
    btn2 = InlineKeyboardButton(text='↪ Назад ↩', callback_data='exit')
    row_one = [btn1]
    row_two = [btn2]
    rows = [row_one, row_two]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    photo = FSInputFile("img/GlStart.png")
    await bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption=f"❗️<b>Standoff 2 API Token Program</b>\n\nДля оплаты :\n1) Перейдите на сайт - https://www.donationalerts.com/r/darcness_bot\n2) Оплатите любым удобным способом\n3) После оплаты вы сразу получите доступ к скачиванию двух файлов\n\n🔴 <b>Сумма  — 150₽</b>", parse_mode='HTML', reply_markup=markup)

@dp.callback_query(F.data == 'cheak_buy')
async def calldata(call: CallbackQuery):    
    await bot.send_message(call.message.chat.id, "❌<b>Ошибка!</b>\nВы не оплатили программу. Произведите оплату или обратитесь в техподдержку.", parse_mode='HTML')

@dp.callback_query(F.data == 'exit')
async def calldata(call: CallbackQuery): 
    await call.message.delete()
       
    btn1 = InlineKeyboardButton(text='💸 Купить программу 💸', callback_data='buy')
    btn2 = InlineKeyboardButton(text='▶ Наш Telegram канал ◀', url="https://t.me/+JfaAicE2WeYwNzky")
    btn3 = InlineKeyboardButton(text='⁉ Как это работает? ⁉', callback_data='help')
    btn4 = InlineKeyboardButton(text='🚀 Отзывы 🚀', callback_data='otzivi')
    row_one = [btn1]
    row_two = [btn2]
    row_fre = [btn3]
    row_fho = [btn4]
    rows = [row_one, row_two, row_fre, row_fho]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    photo = FSInputFile("img/GlStart.png")
    await bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption=f"<b>Приветствую! Вы зашли в Darcness Bot 🔐</b>\n\n<em>Тут ты можешь приобрести программу, что бы заходить в аккаунты Standoff 2 по id 💣</em>\n\nВыбери пункт ниже, который тебя интересует 👇", parse_mode='HTML', reply_markup=markup)

@dp.callback_query(F.data == 'help')
async def calldata(call: CallbackQuery):   
    await bot.send_message(call.message.chat.id, "<b>❗️ Предлагаем вам посмотреть видео для ознакомления с нашим сервисом</b>", parse_mode='HTML')
    video = FSInputFile("img/1.mp4")
    await bot.send_video(call.message.chat.id, video=video)
    
@dp.callback_query(F.data == 'otzivi')
async def calldata(call: CallbackQuery): 
    
    photo = FSInputFile("img/Otzivi/1.jpg")
    await bot.send_photo(chat_id=call.message.chat.id, photo=photo)
    photo = FSInputFile("img/Otzivi/2.jpg")
    await bot.send_photo(chat_id=call.message.chat.id, photo=photo)
    photo = FSInputFile("img/Otzivi/3.jpg")
    await bot.send_photo(chat_id=call.message.chat.id, photo=photo)
    photo = FSInputFile("img/Otzivi/4.jpg")
    await bot.send_photo(chat_id=call.message.chat.id, photo=photo)
    photo = FSInputFile("img/Otzivi/5.jpg")
    await bot.send_photo(chat_id=call.message.chat.id, photo=photo)
    photo = FSInputFile("img/Otzivi/6.jpg")
    await bot.send_photo(chat_id=call.message.chat.id, photo=photo)
    photo = FSInputFile("img/Otzivi/7.jpg")
    await bot.send_photo(chat_id=call.message.chat.id, photo=photo)
    photo = FSInputFile("img/Otzivi/8.jpg")
    await bot.send_photo(chat_id=call.message.chat.id, photo=photo)
    photo = FSInputFile("img/Otzivi/9.jpg")
    await bot.send_photo(chat_id=call.message.chat.id, photo=photo)

      
    btn1 = InlineKeyboardButton(text='💸 Купить программу 💸', callback_data='buy')
    btn2 = InlineKeyboardButton(text='▶ Наш Telegram канал ◀', url="https://t.me/+JfaAicE2WeYwNzky")
    btn3 = InlineKeyboardButton(text='⁉ Как это работает? ⁉', callback_data='help')
    btn4 = InlineKeyboardButton(text='🚀 Отзывы 🚀', callback_data='otzivi')
    row_one = [btn1]
    row_two = [btn2]
    row_fre = [btn3]
    row_fho = [btn4]
    rows = [row_one, row_two, row_fre, row_fho]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    photo = FSInputFile("img/GlStart.png")
    await bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption=f"<b>Приветствую! Вы зашли в Darcness Bot 🔐</b>\n\n<em>Тут ты можешь приобрести программу, что бы заходить в аккаунты Standoff 2 по id 💣</em>\n\nВыбери пункт ниже, который тебя интересует 👇", parse_mode='HTML', reply_markup=markup)

@dp.callback_query(F.data == 'adminka')
async def calldata(call: CallbackQuery):   
    #--------------------
    db = sqlite3.connect('main.db')
    c = db.cursor()
    cheack = c.execute(f"SELECT * FROM Users").fetchall()
    #---------------------
    all_users = len(cheack)
    #---------------------
    
    #Смотрим кто заблокал бота, а кто нет
    for user in cheack:
        try:
            msg = await bot.send_message(chat_id=user[1], text='test')
            await bot.delete_message(chat_id=user[1], message_id=msg.message_id)
        except:
            c.execute(f"UPDATE Users SET Active = ('0') WHERE UserId = ('{user[1]}')")
            db.commit()
            
    #Смотрим в таблице кто заблокал
    cheack = c.execute(f"SELECT * FROM Users WHERE Active = ('0')").fetchall()
    all_block_user = len(cheack)
    
    #Высчитываем активных пользователей
    no_block_users = int(all_users) - int(all_block_user)
    
    btn1 = InlineKeyboardButton(text='Обновить', callback_data='obnova')
    row_one = [btn1]
    rows = [row_one]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)

    #Вывод статистики на экран
    await bot.send_message(call.message.chat.id, f'📊 <b>Статистика</b>\n-----------------------------------\n<b>👤 Всего пользователей: {all_users}\n🚀 Активные пользователи: {no_block_users}\n-----------------------------------\n </b>', parse_mode='HTML', reply_markup=markup)

@dp.callback_query(F.data == 'obnova')
async def calldata(call: CallbackQuery): 
    await call.message.delete()
    
    #--------------------
    db = sqlite3.connect('main.db')
    c = db.cursor()
    cheack = c.execute(f"SELECT * FROM Users").fetchall()
    #---------------------
    all_users = len(cheack)
    #---------------------
    
    #Смотрим кто заблокал бота, а кто нет
    for user in cheack:
        try:
            msg = await bot.send_message(chat_id=user[1], text='test')
            await bot.delete_message(chat_id=user[1], message_id=msg.message_id)
        except:
            c.execute(f"UPDATE Users SET Active = ('0') WHERE UserId = ('{user[1]}')")
            db.commit()
            
    #Смотрим в таблице кто заблокал
    cheack = c.execute(f"SELECT * FROM Users WHERE Active = ('0')").fetchall()
    all_block_user = len(cheack)
    
    #Высчитываем активных пользователей
    no_block_users = int(all_users) - int(all_block_user)
    
    btn1 = InlineKeyboardButton(text='Обновить', callback_data='obnova')
    row_one = [btn1]
    rows = [row_one]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)

    #Вывод статистики на экран
    await bot.send_message(call.message.chat.id, f'📊 <b>Статистика</b>\n-----------------------------------\n<b>👤 Всего пользователей: {all_users}\n🚀 Активные пользователи: {no_block_users}\n-----------------------------------\n </b>', parse_mode='HTML', reply_markup=markup)

@dp.message(Command("sender"))
async def Sender(message: types.Message):
    if message.from_user.id == 5890667637:
        text = message.text[8:]
        
        
        db = sqlite3.connect('main.db')
        c = db.cursor()
        cheack = c.execute(f"SELECT * FROM Users").fetchall()

        for user in cheack:
            try:
                await bot.send_message(chat_id=user[1], text=text)
            except:
                pass
        
        db.close()
        await bot.send_message(chat_id='5890667637', text='Рассылка закончилась!')
    else:
        await bot.send_message(message.from_user.id, 'Команда не доступна для вас!')
        
        
async def request_op(user_id, chat_id, gender=None):
    try:
        headers = {
            'Content-Type': 'application/json',
            'Auth': '70b064f4dd45617be5549ac0b3d43aeb7025389127993b2170ad6b7d96a86f87',
            'Accept': 'application/json',
        }
        data = {
            'UserId': user_id, 
            'ChatId': chat_id
        }
        if gender:
            data['Gender'] = gender

        async with aiohttp.ClientSession() as session:
            async with session.post('https://api.subgram.ru/request-op/', headers=headers, json=data) as response:
                if not response.ok:
                    logging.error('SubGram: %s' % str(await response.json()))
                    return 'ok', 400
                response_json = await response.json()
                
                if response_json['message'] == 'Успешно':
                    
                    
                    db = sqlite3.connect('main.db')
                    c = db.cursor()
                    active = 1
                        
                    cheack = c.execute(f"SELECT * FROM Users WHERE UserId = ?", (user_id, )).fetchall()
                    if len(cheack) == 0:
                        c.execute(f"INSERT INTO Users VALUES ('{username}', '{user_id}', '{active}')")
                        db.commit()
                        db.close()
                    else:
                        c.execute(f"SELECT Active FROM Users WHERE UserId = ?", (user_id, ))
                        balance = c.fetchone()
                        db.commit()
                        if balance[0] == 0:
                            c.execute(f"UPDATE Users SET Active = ('1') WHERE UserId = ('{user_id}')")
                            db.commit()
                            db.close()
                        else:
                            db.commit()
                            db.close()
                            
                    if chat_id == 5890667637:
                        
                        btn1 = InlineKeyboardButton(text='💸 Купить программу 💸', callback_data='buy')
                        btn2 = InlineKeyboardButton(text='🔓 Пробная версия 🔓', url='https://t.me/+JfaAicE2WeYwNzky')
                        btn3 = InlineKeyboardButton(text='▶ Наш Telegram канал ◀', url="https://t.me/+JfaAicE2WeYwNzky")
                        btn4 = InlineKeyboardButton(text='⁉ Как это работает? ⁉', callback_data='help')
                        btn5 = InlineKeyboardButton(text='🚀 Отзывы 🚀', callback_data='otzivi')
                        btn6 = InlineKeyboardButton(text='☘ АДМИНКА ☘', callback_data='adminka')
                        row_one = [btn1]
                        row_two = [btn2]
                        row_fre = [btn3]
                        row_fho = [btn4]
                        row_five = [btn5]
                        row_six = [btn6]
                        rows = [row_one, row_two, row_fre, row_fho, row_five, row_six]
                        markup = InlineKeyboardMarkup(inline_keyboard=rows)
                        photo = FSInputFile("img/GlStart.png")
                        await bot.send_photo(chat_id=chat_id, photo=photo, caption=f"<b>Приветствую! Вы зашли в Darcness Bot 🔐</b>\n\n<em>Тут ты можешь приобрести программу, что бы заходить в аккаунты Standoff 2 по id 💣</em>\n\nВыбери пункт ниже, который тебя интересует 👇", parse_mode='HTML', reply_markup=markup)
                        
                    else:
                                
                        btn1 = InlineKeyboardButton(text='💸 Купить программу 💸', callback_data='buy')
                        btn2 = InlineKeyboardButton(text='🔓 Пробная версия 🔓', url='https://t.me/+JfaAicE2WeYwNzky')
                        btn3 = InlineKeyboardButton(text='▶ Наш Telegram канал ◀', url="https://t.me/+JfaAicE2WeYwNzky")
                        btn4 = InlineKeyboardButton(text='⁉ Как это работает? ⁉', callback_data='help')
                        btn5 = InlineKeyboardButton(text='🚀 Отзывы 🚀', callback_data='otzivi')
                        row_one = [btn1]
                        row_two = [btn2]
                        row_fre = [btn3]
                        row_fho = [btn4]
                        row_five = [btn5]
                        rows = [row_one, row_two, row_fre, row_fho, row_five]
                        markup = InlineKeyboardMarkup(inline_keyboard=rows)
                        photo = FSInputFile("img/GlStart.png")
                        await bot.send_photo(chat_id=chat_id, photo=photo, caption=f"<b>Приветствую! Вы зашли в Darcness Bot 🔐</b>\n\n<em>Тут ты можешь приобрести программу, что бы заходить в аккаунты Standoff 2 по id 💣</em>\n\nВыбери пункт ниже, который тебя интересует 👇", parse_mode='HTML', reply_markup=markup)

                    return response_json.get("status"), response_json.get("code")
                    
                else:
                    print('TYT!')
                    return response_json.get("status"), response_json.get("code")

    except Exception as e:
        logging.error('SubGram: %s' % str(e))
        return 'ok', 400  
    
@dp.callback_query(lambda call: call.data.startswith("subgram"))
async def subgram_callback_query(call):
    global referrer_id
    user_id = call.from_user.id
    chat_id = call.message.chat.id
    if call.data == "subgram-op":
        status, code = await request_op(user_id, chat_id)
        if status == 'ok' and code == 200: #Если статус ok и code 200 (совокупность параметров означает, что пользователь подписан)
            pass
            
        elif status == 'ok':
            pass
            
        else:
            return
        
    elif call.data.startswith("subgram_gender_"):
        gender = call.data.split("_")[2]
        status, code = await request_op(user_id, chat_id, gender)
        if status == 'ok' and code == 200: #Если статус ok и code 200 (совокупность параметров означает, что пользователь подписан)
            pass
        
        elif status == 'ok':
            pass
        
        else:
            return

async def main() -> None:
    await dp.start_polling(bot)
    
asyncio.run(main())

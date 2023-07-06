from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from youtubesearchpython import *
from youtubesearchpython import VideosSearch, PlaylistsSearch, Search
from pytube import YouTube
from moviepy.editor import VideoFileClip
from aiogram.types import InputFile
from telegram import Audio
from telegram.ext import Updater, MessageHandler
import requests
import time
import asyncio
import urllib.request
import youtube_dl
import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

TOKEN_API = "MY_TOKEN_API"

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)



ikb = InlineKeyboardMarkup(row_width=2)
ikb2 = InlineKeyboardMarkup(row_width=2)
ib1 = InlineKeyboardButton(text='Пошук', callback_data = 'search')
ib2 = InlineKeyboardButton(text='Топ 10 в Україні',
                           callback_data = 'top')

ikb.add(ib1, ib2)



async def on_startup(_):
    print('Я запустился')
 
  

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("""<em>
<b>Ласкаво прошу до MY MUSIC BOT! ♫ </b>
Цей бот конвертує відео,посилання на яке Ви відправите боту!
Просто пришліть посилання на пісню/подкаст з YouTube Music та бот сконвертує це відео у mp3 формат!
Якщо Ви хочете дізнатись про бота більше, введіть команду /help (або просто натисніть на неї) </em>

""",
parse_mode="HTML",
reply_markup=ikb)
 
    await message.delete() 




@dp.message_handler(commands=['1'])
async def audio(message: types.Message):
    audio1 = open("fort.mp3", "rb")
    await bot.send_audio(message.chat.id, audio=audio1)

@dp.message_handler(commands=['2'])
async def audio(message: types.Message):
    audio2 = open("vib.mp3", "rb")
    await bot.send_audio(message.chat.id, audio=audio2)


@dp.message_handler(commands=['3'])
async def audio(message: types.Message):
    audio3 = open("man.mp3", "rb")
    await bot.send_audio(message.chat.id, audio=audio3)



@dp.message_handler(commands=['4'])
async def audio(message: types.Message):
    audio4 = open("vid.mp3", "rb")
    await bot.send_audio(message.chat.id, audio=audio4)



@dp.message_handler(commands=['5'])
async def audio(message: types.Message):
    audio5 = open("vech.mp3", "rb")
    await bot.send_audio(message.chat.id, audio=audio5)




@dp.message_handler(commands=['6'])
async def audio(message: types.Message):
    audio6 = open("tam.mp3", "rb")
    await bot.send_audio(message.chat.id, audio=audio6)



@dp.message_handler(commands=['7'])
async def audio(message: types.Message):
    audio7 = open("por.mp3", "rb")
    await bot.send_audio(message.chat.id, audio=audio7)




@dp.message_handler(commands=['8'])
async def audio(message: types.Message):
    audio8 = open("bur.mp3", "rb")
    await bot.send_audio(message.chat.id, audio=audio8)


@dp.message_handler(commands=['9'])
async def audio(message: types.Message):
    audio9 = open("gul.mp3", "rb")
    await bot.send_audio(message.chat.id, audio=audio9)


@dp.message_handler(commands=['10'])
async def audio(message: types.Message):
    audio10 = open("buz.mp3", "rb")
    await bot.send_audio(message.chat.id, audio=audio10) 



@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer("""
/help - список команд
/start - розпочати роботу з ботом
/info - інформація про MY MUSIC BOT""") 
    
    await message.delete()



@dp.message_handler(commands=['info'])
async def info_command(message: types.Message):
    await message.answer("""
    <b>Наразі цей бот використовується як захист проєкту.
Потім цей бот зможе використовувати кожен охочий!</b>
    """,
    parse_mode="HTML")   
    
    await message.delete()
 


@dp.callback_query_handler(text='search')
async def handle_search(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer("""Введіть команду /giveme, щоб бот почав конвертувати відео, посилання на яке Ви йому скинете.
Введіть команду /dont, щоб бот закінчив робити цю функцію, щоб перейти до інших.""")






@dp.message_handler(commands=['giveme'])
async def enable_convert(message: types.Message):
    global convert_enabled
    convert_enabled = True
    await message.answer("Будь ласка, скиньте посилання на пісню у YouTube Music")





@dp.message_handler(commands=['dont'])
async def disable_convert(message: types.Message):
    global convert_enabled
    convert_enabled = False
    await message.answer("Функція конвертування закінчилася")




@dp.message_handler()
async def run(message: types.Message):
    global convert_enabled

    if convert_enabled:
        if "https://music.youtube.com" not in message.text:
            await message.answer("Скиньте боту посилання саме з YouTube Music!")
            return

        await message.answer("Будь ласка, зачекайте")

        video_info = youtube_dl.YoutubeDL().extract_info(
            url=message.text, download=False
        )
        filename = f"{video_info['title']}.mp3"
        options = {
            'format': 'bestaudio/best',
            'keepvideo': False,
            'outtmpl': filename,
        }

        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([video_info['webpage_url']])

        print("Вже... {}".format(filename))
    
        with open(filename, 'rb') as audio_file:
            await message.reply_audio(audio_file)

        os.remove(filename)
        convert_enabled = False
    else:
        await message.answer("Недійсна команда. Будь ласка, використовуйте /giveme для ввімкнення функції конвертування")




@dp.callback_query_handler(text='top')
async def handle_top(callback_query: types.CallbackQuery):
    await callback_query.message.answer(text="""
    🇺🇦<b>Топ 10 в Україні</b>🇺🇦
Натисніть на одну із цифр, щоб обрати пісню
/1.  Антитіла - Фортеця Бахмут
/2.  Скрябін & Yurcash, Sowa - Вибач
/3.  Артем Пивоваров - Маніфест
/4.  PARFENIUK - Відриваючись
/5.  100лиця & Skylerr - Вечорниці (Добрий день everybody)
/6.  Артем Пивоваров, NK (Настя Каменських) - Там У Тополі
/7.  YAKTAK x KOLA - Порічка
/8.  SHUMEI x ZLATA OGNEVICH - Буревіями
/9.  Kozak Siromaha - Гуляли
/10. Memories Avenue, Артем Лоік - Бузина
    
    """,
    parse_mode="HTML")




if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup) 
import os
import logging
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from info import START_MSG, CHANNELS, ADMINS, INVITE_MSG
from utils import Media

logger = logging.getLogger(__name__)


@Client.on_message(filters.command('start'))
async def start(bot, message):
    """Start command handler"""
    if len(message.command) > 1 and message.command[1] == 'subscribe':
        await message.reply(INVITE_MSG)
    else:
        buttons = [[
            InlineKeyboardButton('Search Movie 🔎', switch_inline_query_current_chat=''),
            InlineKeyboardButton('Go Inline 🦈', switch_inline_query=''),
        ],[
        InlineKeyboardButton('Join Group 👥', url='https://t.me/mmovie_world_Group'),
        InlineKeyboardButton('Join Channel 📡 ', url='https://t.me/mmovie_world'),
        ],[
        InlineKeyboardButton('⭕ Our other Services ⭕', url='https://t.me/mmovieworldlinks'),
        ],[
        InlineKeyboardButton('➕Request Movie➕', url='https://t.me/Contact_MMovie_World_Bot'),
        ],[
        InlineKeyboardButton('Share Bot ↪', url='http://t.me/share/url?url=%E0%B4%B9%E0%B4%B2%E0%B5%8B%20%F0%9F%99%8C,%20@MMovie_World%20%E0%B5%BB%E0%B5%8D%E0%B4%B1%E0%B5%86%20%E0%B4%B8%E0%B4%BF%E0%B4%A8%E0%B4%BF%E0%B4%AE%E0%B4%BE%20%E0%B4%B8%E0%B5%86%E0%B5%BC%E0%B4%9A%E0%B5%8D%E0%B4%9A%E0%B5%8D%20%E0%B4%AC%E0%B5%8B%E0%B4%9F%E0%B5%8D%E0%B4%9F%E0%B5%8D%20%E0%B4%B5%E0%B4%A8%E0%B5%8D%E0%B4%A8%E0%B4%BF%E0%B4%9F%E0%B5%8D%E0%B4%9F%E0%B5%81%E0%B4%A3%E0%B5%8D%E0%B4%9F%E0%B5%8D%20%E0%B4%88%20%E0%B4%9A%E0%B4%BE%E0%B4%B1%E0%B5%8D%E0%B4%B1%E0%B5%8D%20%E0%B4%AC%E0%B5%8B%E0%B4%9F%E0%B5%8D%E0%B4%9F%E0%B4%BF%E0%B5%BD%20Malayalam,%20Tamil,%20Hindi,%20Telugu,%20foreign%20Language%20%E0%B4%8E%E0%B4%A8%E0%B5%8D%E0%B4%A8%E0%B5%80%20%E0%B4%AD%E0%B4%BE%E0%B4%B7%E0%B4%95%E0%B4%B3%E0%B4%BF%E0%B4%B2%E0%B5%86%20%E0%B4%B8%E0%B4%BF%E0%B4%A8%E0%B4%BF%E0%B4%AE%E0%B4%95%E0%B4%B3%E0%B5%81%E0%B4%82%20%E0%B4%B8%E0%B5%80%E0%B4%B0%E0%B4%BF%E0%B4%AF%E0%B4%B2%E0%B5%81%E0%B4%95%E0%B4%B3%E0%B5%81%E0%B4%82%20%E0%B4%B2%E0%B4%AD%E0%B5%8D%E0%B4%AF%E0%B4%AE%E0%B4%BE%E0%B4%A3%E0%B5%8D.%20%20%E0%B4%95%E0%B5%82%E0%B4%9F%E0%B5%81%E0%B4%A4%E0%B4%B2%E0%B5%8D%E2%80%8D%20%E0%B4%85%E0%B4%B1%E0%B4%BF%E0%B4%AF%E0%B4%BE%E0%B4%A8%E0%B5%8D%E2%80%8D%20@MMW_Search_Bot%20%E0%B5%BD%20%E0%B4%9A%E0%B5%86%E0%B4%A8%E0%B5%8D%E0%B4%A8%E0%B5%8D%20START%20%E0%B4%95%E0%B5%8A%E0%B4%9F%E0%B5%81%E0%B4%A4%E0%B5%8D%E0%B4%A4%E0%B4%A4%E0%B4%BF%E0%B4%A8%E0%B5%8D%20%E0%B4%B6%E0%B5%87%E0%B4%B7%E0%B4%82%20/help%20%E0%B4%8E%E0%B4%A8%E0%B5%8D%E0%B4%A8%E0%B5%8D%20%E0%B4%85%E0%B4%AF%E0%B4%95%E0%B5%8D%E0%B4%95%E0%B5%81%E0%B4%95%20%E2%9E%A1%EF%B8%8F%20%20Hello%20%F0%9F%99%8C,%20@MMovie_World%20's%20search%20bot%20is%20now%20available.%20On%20this%20chat%20bot%20you%20can%20find%20Malayalam,%20Tamil,%20Hindi,%20Telugu,%20foreign%20Languages%20Movies%20and%20Series.%20%20For%20more%20details%20Got%20to%20@MMW_Search_Bot%20and%20Click%20START%20and%20type%20/help%20%E2%9E%A1%EF%B8%8F'),
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply(START_MSG, reply_markup=reply_markup)


@Client.on_message(filters.command('channel') & filters.user(ADMINS))
async def channel_info(bot, message):
    """Send basic information of channel"""
    if isinstance(CHANNELS, (int, str)):
        channels = [CHANNELS]
    elif isinstance(CHANNELS, list):
        channels = CHANNELS
    else:
        raise ValueError("Unexpected type of CHANNELS")

    text = '📑 **Indexed channels/groups**\n'
    for channel in channels:
        chat = await bot.get_chat(channel)
        if chat.username:
            text += '\n@' + chat.username
        else:
            text += '\n' + chat.title or chat.first_name

    text += f'\n\n**Total:** {len(CHANNELS)}'

    if len(text) < 4096:
        await message.reply(text)
    else:
        file = 'Indexed channels.txt'
        with open(file, 'w') as f:
            f.write(text)
        await message.reply_document(file)
        os.remove(file)


@Client.on_message(filters.command('total') & filters.user(ADMINS))
async def total(bot, message):
    """Show total files in database"""
    msg = await message.reply("Processing...⏳", quote=True)
    try:
        total = await Media.count_documents()
        await msg.edit(f'📁 Saved files: {total}')
    except Exception as e:
        logger.exception('Failed to check total files')
        await msg.edit(f'Error: {e}')


@Client.on_message(filters.command('logger') & filters.user(ADMINS))
async def log_file(bot, message):
    """Send log file"""
    try:
        await message.reply_document('TelegramBot.log')
    except Exception as e:
        await message.reply(str(e))


@Client.on_message(filters.command('delete') & filters.user(ADMINS))
async def delete(bot, message):
    """Delete file from database"""
    reply = message.reply_to_message
    if reply and reply.media:
        msg = await message.reply("Processing...⏳", quote=True)
    else:
        await message.reply('Reply to file with /delete which you want to delete', quote=True)
        return

    for file_type in ("document", "video", "audio"):
        media = getattr(reply, file_type, None)
        if media is not None:
            break
    else:
        await msg.edit('This is not supported file format')
        return

    result = await Media.collection.delete_one({
        'file_name': media.file_name,
        'file_size': media.file_size,
        'mime_type': media.mime_type,
        'caption': reply.caption.html if reply.caption else None
    })
    if result.deleted_count:
        await msg.edit('File is successfully deleted from database')
    else:
        await msg.edit('File not found in database')

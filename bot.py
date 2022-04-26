# coding=utf-8

import telebot
from telebot import types

TOKEN = ":| Its Private"

app = telebot.TeleBot(TOKEN)

 

@app.message_handler(content_types=["new_chat_members", "left_chat_member", "new_chat_title", "new_chat_photo", "delete_chat_photo", "pinned_message"])
def message(user):
    try:
        msgID = user.message_id
        chatID = user.chat.id
        app.delete_message(chatID, msgID)
    
    except:
        pass
 

@app.message_handler(content_types=["text", "audio", "document", "photo", "sticker", "video", "video_note", "voice", "location", "contant"])
def message(user):
    try:
        usertext = user.text
        chatID = user.chat.id
        UserID = user.from_user.id
        userFN = user.from_user.first_name
        msgID = user.message_id


 
        Adminstxt = open("Admin.txt", "r", encoding="utf_8")
        Adminsread = Adminstxt.read()
        Adminstxt.close()

        ignoreTXT = open("ignore.txt", "r", encoding="utf_8")
        ignoreread = ignoreTXT.read()
        ignoreTXT.close()

        Locktxt = open("lock.txt", "r", encoding="utf_8")
        Lockread = Locktxt.read()
        Locktxt.close()



        if Lockread == "true" and UserID != 5081002694:
            app.delete_message(chatID, user.message_id)

        if usertext == "google" or usertext == "Google":
            app.delete_message(chatID, user.message_id)
            text = "⭕️ سرچ کنید!\n\n📖 کاربر گرامی لطفا به جای پرسیدن سوالات ساده و پیش پا افتاده در گروه از موتور های جست و جو برای رسیدن به جواب استفاده کنید، تا در وقت خود صرفه جویی و از شلوغ کردن گروه جلوگیری کنید!\n\n💎 @DevdoodRules 💎"
            app.send_message(chatID, text, parse_mode="Markdown",
                                reply_to_message_id=user.reply_to_message.message_id)

        if usertext == "Spam" or usertext == "spam":
            app.delete_message(chatID, user.message_id)
            text = "⭕️ اسپم نکنید!\n\n📖 کاربر گرامی لطفا پیام های خود را در چندین پیام ارسال نکنید! ارسال پیام های اضافی باعث اسپم واذیت شدن اعضا می شود!\n\n💎 @DevdoodRules 💎"
            app.send_message(chatID, text, parse_mode="Markdown",
                                reply_to_message_id=user.reply_to_message.message_id)

        if usertext == "Insult" or usertext == "insult":
            app.delete_message(chatID, user.message_id)
            text = "⭕️ احترام به یکدیگر\n\n📖 کاربر گرامی لطفا از توهین و برخورد نادرست با افراد در گروه خود داری کنید! در صورت تکرار دوباره از ارسال پیام در گروه محروم می شوید! گروه جای مشکلات شخصی نیست!\n\n💎 @DevdoodRules 💎"
            app.send_message(chatID, text, parse_mode="Markdown",
                                reply_to_message_id=user.reply_to_message.message_id)

        if usertext == "offtopic" or usertext == "Offtopic":
            app.delete_message(chatID, user.message_id)
            text = "⭕️ خارج از موضوع\n\n📖 کاربر گرامی لطفا از حوزه فعالیت گروه ( برنامه نویسی ) خارج نشوید! در صورت تکرار دوباره از ارسال پیام در گروه محروم می شوید!\n\n💎 @DevdoodRules 💎"
            app.send_message(chatID, text, parse_mode="Markdown",
                                reply_to_message_id=user.reply_to_message.message_id)

        if str(UserID) in ignoreread and user.reply_to_message.from_user.id == 5081002694:
            app.delete_message(chatID, user.message_id)

        if str(UserID) in Adminsread:
            if usertext == 'admin list':
                Adminstxt = open("Admin.txt", "r", encoding="utf_8")
                Adminsread = Adminstxt.read()
                Admins = Adminsread.split(';')
                Adminstxt.close()

                admintext = "⭕️ لیست ادمین های گروه"
                i = 1

                for admin in Admins:
                    admintext = admintext + \
                        f"\n\n{str(i)} - [admin {i}](tg://user?id={admin})"
                    if i == len(Admins):
                        app.send_message(
                            chat_id=chatID, text=admintext, parse_mode="Markdown")
                    i = i + 1

                app.delete_message(chatID, user.message_id)

            if usertext == 'ban':
                app.delete_message(chatID, user.message_id)
                if UserID == 5081002694:
                    app.send_message(
                        chatID, f"⭕️ کاربر [{user.reply_to_message.from_user.first_name}](tg://user?id={user.reply_to_message.from_user.id}) توسط [{userFN}](tg://user?id={UserID}) (مدیر کل) به مدت 365 روز از گروه اخراج شد!", parse_mode="Markdown")

                else:
                    app.send_message(
                        chatID, f"⭕️ کاربر [{user.reply_to_message.from_user.first_name}](tg://user?id={user.reply_to_message.from_user.id}) توسط [{userFN}](tg://user?id={UserID}) به مدت 365 روز از گروه اخراج شد!", parse_mode="Markdown")

                app.ban_chat_member(chatID, user.reply_to_message.from_user.id)
                app.delete_message(chatID, user.message_id + 2)

            if usertext == 'unban':
                app.delete_message(chatID, user.message_id)
                app.unban_chat_member(chatID, user.reply_to_message.from_user.id)
                if UserID == 5081002694:
                    app.send_message(
                        chatID, f"⭕️ کاربر [{user.reply_to_message.from_user.first_name}](tg://user?id={user.reply_to_message.from_user.id}) توسط [{userFN}](tg://user?id={UserID}) (مدیر کل) از لیست سیاه گروه خارج شد!", parse_mode="Markdown")

                else:
                    app.send_message(
                        chatID, f"⭕️ کاربر [{user.reply_to_message.from_user.first_name}](tg://user?id={user.reply_to_message.from_user.id}) توسط [{userFN}](tg://user?id={UserID}) از لیست سیاه گروه خارج شد!", parse_mode="Markdown")

            if usertext == 'mute':
                app.delete_message(chatID, user.message_id)
                app.restrict_chat_member(chatID, user.reply_to_message.from_user.id, can_send_messages=False)
                if UserID == 5081002694:
                    app.send_message(
                        chatID, f"⭕️ کاربر [{user.reply_to_message.from_user.first_name}](tg://user?id={user.reply_to_message.from_user.id}) توسط [{userFN}](tg://user?id={UserID}) (مدیر کل) از پیام دادن محروم شد!", parse_mode="Markdown")

                else:
                    app.send_message(chatID, f"⭕️ کاربر [{user.reply_to_message.from_user.first_name}](tg://user?id={user.reply_to_message.from_user.id}) توسط [{userFN}](tg://user?id={UserID}) از پیام دادن محروم شد!", parse_mode="Markdown")

            if usertext == 'unmute':
                app.delete_message(chatID, user.message_id)
                app.restrict_chat_member(chatID, user.reply_to_message.from_user.id,
                                            can_send_messages=True, can_send_media_messages=True, can_send_other_messages=True)
                if UserID == 5081002694:
                    app.send_message(
                        chatID, f"⭕️ کاربر [{user.reply_to_message.from_user.first_name}](tg://user?id={user.reply_to_message.from_user.id}) توسط [{userFN}](tg://user?id={UserID}) (مدیر کل) از حالت میوت خارج شد!", parse_mode="Markdown")

                else:
                    app.send_message(
                        chatID, f"⭕️ کاربر [{user.reply_to_message.from_user.first_name}](tg://user?id={user.reply_to_message.from_user.id}) توسط [{userFN}](tg://user?id={UserID}) از حالت میوت خارج شد!", parse_mode="Markdown")

        if UserID == 5081002694:
            if usertext == 'promote':
                app.delete_message(chatID, msgID)
                Adminstxt = open("Admin.txt", "r", encoding="utf_8")
                Adminsread = Adminstxt.read()
                if str(user.reply_to_message.from_user.id) in Adminsread:
                    app.send_message(
                        5081002694, text=f"کابر [{user.reply_to_message.from_user.first_name}](tg://user?id={user.reply_to_message.from_user.id}) از قبل در لیست ادمین ها وجود دارد ! ", parse_mode="Markdown")
                else:
                    Adminstxt = open("Admin.txt", "a", encoding="utf_8")
                    Adminsntxt = open("Admins.txt", "a", encoding="utf_8")
                    Adminstxt.write(f";{user.reply_to_message.from_user.id}")
                    Adminsntxt.write(
                        f";{user.reply_to_message.from_user.first_name}:{user.reply_to_message.from_user.id}")
                    app.send_message(
                        chatID, text=f"😎 کاربر [{user.reply_to_message.from_user.first_name}](tg://user?id={user.reply_to_message.from_user.id}) توسط [{userFN}](tg://user?id={UserID}) ( مدیر کل ) به لیست ادمین ها اضافه شد!", parse_mode="Markdown")

            if usertext == 'unpromote':
                app.delete_message(chatID, msgID)
                Adminstxt = open("Admin.txt", "r", encoding="utf_8")
                Adminsread = Adminstxt.read()

                Adminsntxt = open("Admins.txt", "r", encoding="utf_8")
                if str(user.reply_to_message.from_user.id) in Adminsread:
                    new = Adminsread.replace(
                        f";{user.reply_to_message.from_user.id}", "")
                    Adminstxt = open("Admin.txt", "a", encoding="utf_8")
                    Adminstxt.truncate(0)
                    Adminstxt.write(new)

                    new2 = Adminsread.replace(
                        f"{user.reply_to_message.from_user.id}", "none")
                    Adminsntxt = open("Admins.txt", "a", encoding="utf_8")
                    Adminsntxt.truncate(0)
                    Adminsntxt.write(new2)
                    app.send_message(
                        chatID, text=f"🥱 کاربر [{user.reply_to_message.from_user.first_name}](tg://user?id={user.reply_to_message.from_user.id}) توسط [{userFN}](tg://user?id={UserID}) ( مدیر کل ) از لیست ادمین ها حذف شد!", parse_mode="Markdown")

            if usertext == "ignore":
                app.delete_message(chatID, msgID)
                ignoreTXT = open("ignore.txt", "r", encoding="utf_8")
                ignoreread = ignoreTXT.read()
                if str(user.reply_to_message.from_user.id) in ignoreread:
                    app.send_message(
                        5081002694, text=f"کابر [{user.reply_to_message.from_user.first_name}](tg://user?id={user.reply_to_message.from_user.id}) از قبل در لیست نادیده گرفته شده ها وجود دارد !", parse_mode="Markdown")
                else:
                    ignoreTXT = open("ignore.txt", "a", encoding="utf_8")
                    ignoreTXT.write(f";{user.reply_to_message.from_user.id}")
                    app.send_message(
                        chatID, text=f"🥱 کاربر [{user.reply_to_message.from_user.first_name}](tg://user?id={user.reply_to_message.from_user.id}) توسط [{userFN}](tg://user?id={UserID}) ( مدیر کل ) نادیده گرفته شد!", parse_mode="Markdown")

            if usertext == "🔘":
                app.delete_message(chatID, msgID)
                ignoreTXT = open("ignore.txt", "a", encoding="utf_8")
                ignoreTXT.write(f";{user.reply_to_message.from_user.id}")
                app.restrict_chat_member(
                    chatID, user.reply_to_message.from_user.id, can_send_messages=False)
                app.ban_chat_member(chatID, user.reply_to_message.from_user.id)
                app.send_message(
                    chatID, f"🔘 دکمه کاربر [{user.reply_to_message.from_user.first_name}](tg://user?id={user.reply_to_message.from_user.id}) توسط [{userFN}](tg://user?id={UserID}) از گروه زده شد!", parse_mode="Markdown")

            if usertext == "unignore":
                app.delete_message(chatID, msgID)
                ignoreTXT = open("ignore.txt", "r", encoding="utf_8")
                ignoreread = ignoreTXT.read()
                if str(user.reply_to_message.from_user.id) in ignoreread:
                    new = ignoreread.replace(
                        f";{str(user.reply_to_message.from_user.id)}", "")
                    ignoreTXT = open("ignore.txt", "a", encoding="utf_8")
                    ignoreTXT.truncate(0)
                    ignoreTXT.write(new)
                    app.send_message(
                        chatID, text=f"😄 کاربر [{user.reply_to_message.from_user.first_name}](tg://user?id={user.reply_to_message.from_user.id}) توسط [{userFN}](tg://user?id={UserID}) ( مدیر کل ) از لیست نادیده گرفته شده ها خارج شد!", parse_mode="Markdown")

            if usertext == 'clear':
                msg = user.message_id
                i = 0
                while (msg > i):
                    try:
                        app.delete_message(chatID, msg)
                    except:
                        pass
                    msg = msg - 1

            if 'clear' in usertext and len(usertext) > 6:
                clrnum = usertext.replace('/clear ', '')
                msg = user.message_id
                i = 0
                clrnum = int(clrnum)
                clrnum = clrnum + 1
                while(i < clrnum):
                    try:
                        app.delete_message(chatID, msg)
                    except:
                        pass
                    i = i + 1
                    msg = msg - 1
            
            if usertext == "Lock" or usertext == "lock":
                Locktxt = open("lock.txt", "a", encoding="utf_8")
                Locktxt.truncate(0)
                if Lockread == "false":
                    Locked = "true"
                    Locktxt.write(Locked)
                    app.send_message(chatID, f"⭕️ گروه به درخواست [{userFN}](tg://user?id={UserID}) ( مدیر کل ) قفل شد!\n\n❗️ ارسال پیام تا اطلاع بعدی ممنوع می باشد!", parse_mode="Markdown")
                if Lockread == "true":
                    Locked = "false"
                    Locktxt.write(Locked)
                    app.send_message(chatID, f"⭕️ قفل گروه به درخواست [{userFN}](tg://user?id={UserID}) ( مدیر کل ) باز شد!\n\n❗️ ارسال پیام آزاد می باشد!", parse_mode="Markdown")
                    

    except:
        pass
    
    
@app.inline_handler(lambda query: query.query == 'text')
def query_text(inline_query):
    try:
        r = types.InlineQueryResultArticle('1', 'Result', types.InputTextMessageContent('Result message.'))
        r2 = types.InlineQueryResultArticle('2', 'Result2', types.InputTextMessageContent('Result message2.'))
        app.answer_inline_query(inline_query.id, [r, r2])
    except Exception as e:
        print(e)


app.polling(True)
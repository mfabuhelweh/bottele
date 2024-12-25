import requests
from telegram.ext import Updater, CommandHandler

TOKEN = "7450027395:AAEto8W0qQ7vcIVrGm5bXsxiOGbHPMY9gVw"

def download_tiktok(update, context):
    url = ' '.join(context.args)
    if not url:
        update.message.reply_text("يرجى إرسال رابط فيديو TikTok مثل: /tiktok URL")
        return

    try:
        api_url = f"https://api.tikapi.io/video/info?url={url}"  # مثال لواجهة API
        response = requests.get(api_url)
        data = response.json()

        # تنزيل الفيديو
        video_url = data['video_url']
        video_content = requests.get(video_url).content
        with open("tiktok_video.mp4", "wb") as f:
            f.write(video_content)

        update.message.reply_text("تم تنزيل الفيديو! جاري الإرسال...")
        context.bot.send_video(chat_id=update.message.chat_id, video=open("tiktok_video.mp4", "rb"))
    except Exception as e:
        update.message.reply_text(f"حدث خطأ: {str(e)}")

# دالة لتنزيل فيديوهات YouTube
def download_youtube(update, context):
    url = ' '.join(context.args)
    if not url:
        update.message.reply_text("يرجى إرسال رابط فيديو YouTube مثل: /youtube URL")
        return

    try:
        api_url = f"https://api.ytapi.io/video/info?url={url}"  # مثال لواجهة API
        response = requests.get(api_url)
        data = response.json()

        # تنزيل الفيديو
        video_url = data['video_url']
        video_content = requests.get(video_url).content
        with open("youtube_video.mp4", "wb") as f:
            f.write(video_content)

        update.message.reply_text("تم تنزيل الفيديو! جاري الإرسال...")
        context.bot.send_video(chat_id=update.message.chat_id, video=open("youtube_video.mp4", "rb"))
    except Exception as e:
        update.message.reply_text(f"حدث خطأ: {str(e)}")

# دالة لتنزيل صور/فيديوهات البروفايل من Instagram
def download_profile(update, context):
    username = ' '.join(context.args)
    if not username:
        update.message.reply_text("يرجى إرسال اسم المستخدم مثل: /profile username")
        return

    try:
        api_url = f"https://api.instagram.io/profile/info?username={username}"  # مثال لواجهة API
        response = requests.get(api_url)
        data = response.json()

        # تنزيل الصورة
        profile_pic_url = data['profile_pic_url']
        image_content = requests.get(profile_pic_url).content
        with open("profile_pic.jpg", "wb") as f:
            f.write(image_content)

        update.message.reply_text("تم تنزيل صورة البروفايل! جاري الإرسال...")
        context.bot.send_photo(chat_id=update.message.chat_id, photo=open("profile_pic.jpg", "rb"))
    except Exception as e:
        update.message.reply_text(f"حدث خطأ: {str(e)}")

# إعداد البوت
def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # إضافة الأوامر للبوت
    dp.add_handler(CommandHandler("tiktok", download_tiktok))
    dp.add_handler(CommandHandler("youtube", download_youtube))
    dp.add_handler(CommandHandler("profile", download_profile))

    # تشغيل البوت
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()

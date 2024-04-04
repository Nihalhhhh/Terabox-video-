import requests
from telegram.ext import Updater, CommandHandler

# Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual bot token
TOKEN = '6435807387:AAEQJNhA-diZlUySxcg-vFi8dtS3JE_1Rv4'

def start(update, context):
    update.message.reply_text("Welcome to Terabox Video Downloader Bot! Send me the link of the Terabox video you want to download.")

def download_video(update, context):
    video_url = update.message.text

    # Assuming the video URL is in the format provided by Terabox
    # Replace 'api.terabox.me' with the actual Terabox API endpoint
    api_url = 'https://api.terabox.me/v1/download?link=' + video_url

    response = requests.get(api_url)
    if response.status_code == 200:
        # Assuming the video is available for download
        video_download_link = response.json().get('download_link')
        update.message.reply_text("Here's your video download link: {}".format(video_download_link))
    else:
        update.message.reply_text("Sorry, something went wrong. Please make sure the provided link is correct.")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("download", download_video))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

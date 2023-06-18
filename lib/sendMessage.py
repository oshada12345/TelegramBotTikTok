import os
from telethon import TelegramClient, events, sync
from dotenv import load_dotenv

load_dotenv()

apiid = '21204722'
apihash = '4f5b4bbc15e7f9df9961ac92e8fd219b'
tokenbot = '6179143538:AAHL47_OiZ0hmLUd7yJWsUhMCdFvHtpKIv4'


def sendMessage(chat_id: int, message: str, message_id: int, file_path: str = None):
    try:
        if not os.path.exists("session"):
            os.makedirs("session")
        app = TelegramClient(session=f"session/bot",
                             api_id=apiid, api_hash=apihash)
        app.start(bot_token=tokenbot)
        if file_path:
            app.send_message(entity=chat_id, file=file_path, message=message,
                             reply_to=message_id, parse_mode="markdown", link_preview=False)
        else:
            app.send_message(entity=chat_id, message=message,
                             reply_to=message_id, parse_mode="markdown", link_preview=False)
        app.disconnect()
    except Exception as e:
        app.disconnect()
        print(f"- {e}")


from wxpy import *

bot=Bot()


# 机器人账号自身
myself = bot.self

# 向文件传输助手发送消息
bot.file_helper.send('Hello from wxpy!')

tuling = Tuling(api_key='0794b7651b33474f8b96c5ab873e6004')

# 自动回复所有文字消息
@bot.register(msg_types=TEXT)
def auto_reply_all(msg):
    tuling.do_reply(msg)


# 开始运行
bot.join()
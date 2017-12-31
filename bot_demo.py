from twx.botapi import TelegramBot

bot = TelegramBot('479026602:AAEvg7k6azp0SAvzO5N4O7DpnhU6kzMaQRg')
log_ = open("log.txt", "r")
log = log_.read()
log_.close()
updates = bot.get_updates().wait()
pan = len(updates)
i = 0
mulai = 0
for updates_ in updates:
	if str(updates[i].update_id) == str(log):
		break
	mulai = i+1
	i += 1
while True:
	updates = bot.get_updates().wait()
	pan = len(updates)
	if pan > mulai:
		if not log == str(updates[pan-1].update_id):
			save = open('log.txt', 'w+')
			save.write(str(updates[mulai].update_id))
			save.close()
			user_id = updates[mulai].message.chat.id
			if updates[mulai].message.text == '/start':
				result = bot.send_message(user_id, 'terimakasih telah memulai').wait()
			elif updates[mulai].message.text == '/info':
				result = bot.send_message(user_id, 'ini adalah bot telegram percobaan').wait()
			else:
				result = bot.send_message(user_id, 'command kamu salah kakak :P').wait()
			mulai += 1
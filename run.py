from __future__ import unicode_literals
from pyrogram import Client, MessageHandler
import pyrogram
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import out
import os
import misc


robomode = False

def handleMemes(client, message):
	print(message)
	global robomode

	import os

	if message["outgoing"]: # check if the message is outgoing and not incoming
		
		send_to = message.chat.id # define the origin of the message
		first_word = message["text"].split()[0] # define the origin of the message

		if message["reply_to_message"]: # if the message is a reply message...
			reply_message = message["reply_to_message"]["message_id"] #... define the destination of the message

		reply_message_bool = message["reply_to_message"] # boolean varirable if the user is replying to a message or not

		if robomode: # this is a consistant module..
			# the robo mode function will change the users messages from normal messages to a uppercase message with
			# code markdown
			app.edit_message_text(send_to, message.message_id, "`" + str(message.text).upper() + "`", parse_mode="markdown")

		if first_word == ".simply":

			# the one does not simply meme
			if len(message["text"]) > 8:
				app.delete_messages(send_to,message["message_id"])
				out.memes.oneDoesNotSimply(message["text"][8:].upper())
				app.send_photo(send_to,"out.jpg")
				os.remove("out.jpg")
			else:
				out.memes.oneDoesNotSimply("tell me what to do".upper())
				app.send_photo(send_to,"out.jpg")
				os.remove("out.jpg")

		# the history aliens meme
		elif first_word == ".aliens":
			app.delete_messages(send_to, message["message_id"])
			if len(message["text"]) > 8:
				out.memes.historyAliensGuy(message["text"][8:])
			else:
				out.memes.historyAliensGuy("Aliens".upper())
			if not reply_message_bool:
				app.send_photo(send_to,"out.jpg")
			else:
				app.send_photo(send_to,"out.jpg",reply_to_message_id=reply_message)
			os.remove("out.jpg")

		# the toystory meme
		elif first_word == ".toystory":
			if len(message["text"]) > 10:
				out.memes.toyStoryMeme(message["text"][10:])
			else:
				out.memes.toyStoryMeme("Memes")
			app.delete_messages(send_to, message["message_id"])
			if not reply_message_bool:
				app.send_photo(send_to, "out.jpg")
			else:
				app.send_photo(send_to, "out.jpg", reply_to_message_id=reply_message)
			os.remove("out.jpg")
			
		elif first_word == ".nrv":
			app.delete_messages(send_to, message["message_id"])
			if not reply_message_bool:
				app.send_photo(send_to, "templates/nervous-guy.jpg")
			else:
				app.send_photo(send_to, "templates/nervous-guy.jpg", reply_to_message_id=reply_message)

		elif first_word == ".process":
			app.delete_messages(send_to, message["message_id"])
			misc.processing(app, send_to, message.text[9:])
			
		elif first_word == ".robomode":
			app.delete_messages(send_to, message.message_id)
			if robomode:
				robomode = False
			else:
				robomode = True

		elif first_word == ".speak":
			from gtts import gTTS 
			import os 
			app.delete_messages(send_to, message["message_id"])
			if len(message.text) > 7:
				mytext = message.text[7:]
				language = 'en'
				myobj = gTTS(text=mytext, lang=language, slow=False) 
				myobj.save("outvoice.mp3")
				if not reply_message_bool:
					app.send_voice(send_to, "outvoice.mp3")
				else:
					app.send_voice(send_to, "outvoice.mp3", reply_to_message_id=reply_message)
				os.remove("outvoice.mp3")

		elif first_word == ".iminhell":
			app.delete_messages(send_to, message["message_id"])
			if not reply_message_bool:
				app.send_voice(send_to, "templates/im-in-hell.mp3")
			else:
				app.send_voice(send_to, "templates/im-in-hell.mp3", reply_to_message_id=reply_message)

		elif first_word == ".no":
			app.delete_messages(send_to, message["message_id"])
			if not reply_message_bool:
				app.send_voice(send_to, "templates/no-no-noo.mp3")
			else:
				app.send_voice(send_to, "templates/no-no-noo.mp3", reply_to_message_id=reply_message)

		elif first_word == ".stonks":
			app.delete_messages(send_to, message["message_id"])
			if not reply_message_bool:
				app.send_photo(send_to, "templates/stonks.png")
			else:
				app.send_photo(send_to, "templates/stonks.png", reply_to_message_id=reply_message)

		elif first_word == ".entirestock":
			app.delete_messages(send_to, message["message_id"])
			if not reply_message_bool:
				app.send_photo(send_to, "templates/ill-take-your-entire-stock.jpg")
			else:
				app.send_photo(send_to, "templates/ill-take-your-entire-stock.jpg", reply_to_message_id=reply_message)

		elif first_word == ".noyou":
			app.delete_messages(send_to, message["message_id"])
			if not reply_message_bool:
				app.send_photo(send_to, "templates/no-u.jpg")
			else:
				app.send_photo(send_to, "templates/no-u.jpg", reply_to_message_id=reply_message)

		elif first_word == ".nouno":
			app.delete_messages(send_to, message["message_id"])
			if not reply_message_bool:
				app.send_photo(send_to, "templates/no-uno.jpg")
			else:
				app.send_photo(send_to, "templates/no-uno.jpg", reply_to_message_id=reply_message)

		elif first_word == ".bigbrain":
			app.delete_messages(send_to, message["message_id"])
			if not reply_message_bool:
				app.send_photo(send_to, "templates/big-brain.jpg")
			else:
				app.send_photo(send_to, "templates/big-brain.jpg", reply_to_message_id=reply_message)	

		elif first_word == ".detroit2":
			app.delete_messages(send_to, message["message_id"])
			if not reply_message_bool:
				app.send_photo(send_to, "templates/dbh-painting-meme-2.jpg")
			else:
				app.send_photo(send_to, "templates/dbh-painting-meme-2.jpg", reply_to_message_id=reply_message)	

		elif first_word == ".excellentmove":
			app.delete_messages(send_to, message["message_id"])
			if not reply_message_bool:
				app.send_photo(send_to, "templates/excellent-move.png")
			else:
				app.send_photo(send_to, "templates/excellent-move.png", reply_to_message_id=reply_message)	

		elif first_word == ".detroit":
			app.delete_messages(send_to, message["message_id"])
			if reply_message_bool:
				if message["reply_to_message"]["media"]:
					from PIL import Image
					import numpy as np
					app.download_media(message["reply_to_message"], "in-data.png")
					img = Image.open("templates/dbh-painting-meme.png")
					background = Image.open("downloads/in-data.png")
					size = (2560,1600)
					small_image = (920,1150)
					edited_image = background
					edited_image = edited_image.resize(size,Image.ANTIALIAS)
					scaled_image = background.resize(small_image, Image.ANTIALIAS)
					average_tuple = misc.average_colour(background)
					edited_image = Image.new("RGBA", (2560,1600), "#F00")
					scaled_image = scaled_image.convert('RGBA')
					scaled_image = scaled_image.rotate(4, expand=1 ).resize(small_image)
					edited_image.paste(scaled_image, (845, 248),scaled_image)
					edited_image.paste(img, (0,0), img)
					edited_image.save('out.png',"PNG")
					app.send_photo(send_to, "out.png")
				else:
					app.send_message(send_to, "Dear Sam,\n\nReply to a message with a photo.\n\nSincerly,\nYour subconsious")
			else:
				app.send_message(send_to, "Dear Sam,\n\nReply to a text to get this to work.\n\nSincerly,\nYour subconsious")

		elif first_word == ".artist":
			app.delete_messages(send_to, message["message_id"])
			if reply_message_bool:
				if message["reply_to_message"]["media"]:
					from PIL import Image
					import numpy as np
					app.download_media(message["reply_to_message"], "in-data.png")
					img = Image.open("templates/artistmeme.png")
					background = Image.open("downloads/in-data.png")
					size = (960,960)
					small_image = (430,480)
					edited_image = background
					edited_image = edited_image.resize(size,Image.ANTIALIAS)
					scaled_image = background.resize(small_image, Image.ANTIALIAS)
					average_tuple = misc.average_colour(background)
					edited_image = Image.new("RGBA", (960,960), "#FFF")
					scaled_image = scaled_image.convert('RGBA')
					scaled_image = scaled_image.rotate( 15, expand=1 ).resize(small_image)
					edited_image.paste(scaled_image, (545, 530),scaled_image)
					edited_image.paste(img, (0,0), img)
					edited_image.save('out.png',"PNG")
					app.send_photo(send_to, "out.png")
				else:
					app.send_message(send_to, "Dear Sam,\n\nReply to a message with a photo.\n\nSincerly,\nYour subconsious")
			else:
				app.send_message(send_to, "Dear Sam,\n\nReply to a text to get this to work.\n\nSincerly,\nYour subconsious")

		elif first_word == ".ping":
			import time
			app.delete_messages(send_to, message["message_id"])
			last_message = app.send_message(send_to, "`System online. All commands available.`", parse_mode="markdown")
			time.sleep(1)
			app.delete_messages(send_to, last_message["message_id"])

		elif first_word == ".unocolor":
			from PIL import Image
			import numpy as np
			app.delete_messages(send_to, message["message_id"])
			color_hex = message["text"].split()[1]
			edited_image = Image.new("RGBA", (720,1099), color_hex)
			template_page = Image.open("templates/uno-reverse.png")
			edited_image.paste(template_page, (0,0), template_page)
			edited_image.save('out.png',"PNG")
			app.send_photo(send_to, "out.png")

		# elif first_word == ".getyoutube":
		# 	import youtube_dl
		# 	message_splitted = message["text"].split()
		# 	youtube_url = message_splitted[1]
		# 	print(youtube_url)
		# 	import youtube_dl
		# 	ydl_opts = {
		# 		'format': 'bestaudio/best',
		# 		'postprocessors': [{
		# 			'key': 'FFmpegExtractAudio',
		# 			'preferredcodec': 'mp3',
		# 			'preferredquality': '192',
		# 		}],
		# 	}
		# 	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		# 		ydl.download([youtube_url])

		elif first_word == ".jhonny":
			import cv2
			import matplotlib.pyplot as plt
			import numpy as np
			from PIL import Image
			face_cascade = cv2.CascadeClassifier('cascades/facial.xml')
			app.delete_messages(send_to, message["message_id"])
			if reply_message_bool:
				if message["reply_to_message"]["media"]:
					app.download_media(message["reply_to_message"], "in-data.png")
					img = cv2.imread('downloads/in-data.png',1)
					img_pil = im = Image.open(r'downloads/in-data.png')
					template_image = Image.open(r'templates/heres-jhonny.png')
					background_image = Image.new("RGBA", (1600,900), "#FFF")
					faces = face_cascade.detectMultiScale(img, 1.3, 5)
					if len(faces) != 0:
						print("Faces found!")
						x = faces[0][0]
						y = faces[0][1]
						w = faces[0][2]
						h = faces[0][3]
						cropped_face = img_pil.crop((x, y-30, w+x, h+y+30)).resize((750, 893))
						background_image.paste(cropped_face, (int(650-(w/2)),int(100-(h/2))))
						final_image = background_image.paste(template_image, (0,0),template_image)
						background_image.save("output.png")
						app.send_photo(send_to, "output.png")
					else:
						app.send_message(send_to, "I can't detect a face in this image")
				else:
					app.send_message(send_to, "Reply to a message with an image.")
			else:
				app.send_message(send_to, "Reply to a message with an image.")
		
		elif first_word == ".recogfaces":
			import cv2
			import matplotlib.pyplot as plt
			import numpy as np
			from PIL import Image
			app.delete_messages(send_to, message["message_id"])
			face_cascade = cv2.CascadeClassifier('cascades/eye.xml')
			if reply_message_bool:
				if message["reply_to_message"]["media"]:
					app.download_media(message["reply_to_message"], "in-data.png")
					img = cv2.imread('downloads/in-data.png',1)
					gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
					faces = face_cascade.detectMultiScale(gray, 1.3, 5)
					if len(faces) != 0:
						for (x,y,w,h) in faces:
							cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
							roi_gray = gray[y:y+h, x:x+w]
							roi_color = img[y:y+h, x:x+w]
						cv2.imwrite('output.png',img)
						app.send_photo(send_to, "output.png")
					else:
						app.send_message(send_to, "`Error : Cannot find faces in this image.`", parse_mode="markdown")
				else:
					app.send_message(send_to, "'Error : This function needs you to reply to a message with an image.`", parse_mode="markdown")
			else:
				app.send_message(send_to, "`Error : This function needs you to reply to a message.`", parse_mode="markdown")
		
		elif first_word == ".googly":
			import cv2
			import matplotlib.pyplot as plt
			import numpy as np
			from PIL import Image
			app.delete_messages(send_to, message["message_id"])
			face_cascade = cv2.CascadeClassifier('cascades/eye.xml')
			if reply_message_bool:
				if message["reply_to_message"]["media"]:
					app.download_media(message["reply_to_message"], "in-data.png")
					img = cv2.imread('downloads/in-data.png',1)
					img_pil = Image.open(r'downloads/in-data.png')
					goog_eye = Image.open(r'templates/googly-eye.png')
					gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
					eye = face_cascade.detectMultiScale(gray, 1.3, 5)
					if len(eye) != 0:
						edited_image = img_pil
						for (x,y,w,h) in eye:
							cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
							roi_gray = gray[y:y+h, x:x+w]
							roi_color = img[y:y+h, x:x+w]
							currently_scaled = goog_eye.resize((w,h))
							edited_image.paste(currently_scaled, (x,y), currently_scaled)
						edited_image.save("output.png")
						app.send_photo(send_to, "output.png")
					else:
						app.send_message(send_to, "`Error : Cannot find eyes in this image.`", parse_mode="markdown")
				else:
					app.send_message(send_to, "`Error : This function needs you to reply to a message with an image.`", parse_mode="markdown")
			else:
				app.send_message(send_to, "`Error : This function needs you to reply to a message.`", parse_mode="markdown")
		
		elif first_word == ".threaten":
			app.delete_messages(send_to, message["message_id"])
			app.send_photo(message["reply_to_message"]["from_user"]["id"], "templates/i-will-kill-you.jpg")	

		elif first_word == ".help":
			import time
			app.delete_messages(send_to, message["message_id"])
			last_message = app.send_message(send_to,	".simply\n" +
														".aliens\n" +
														".toystory\n" +
														".nrv\n" +
														".robomode\n" +
														".speak\n" +
														".stinks\n" +
														".noyou\n" +
														".nouno\n" +
														".bigbrain\n" +
														".detroit\n" +
														".detroit2\n" +
														".excellentmove\n" +
														".artist\n" +
														".ping\n" +
														".unocolor\n" +
														".jhonny\n" +
														".recogfaces\n" +
														".googly")
			time.sleep(5)
			app.delete_messages(send_to, last_message["message_id"])

		elif first_word == ".isthis":
			from PIL import Image
			from PIL import ImageFont
			from PIL import ImageDraw

			message_parts = message["text"][7:].split(",")
			app.delete_messages(send_to, message["message_id"])

			if reply_message_bool:
				if len(message_parts) >= 2:
					
					target_id = message["reply_to_message"]["from_user"]["id"]
					profile_picture = app.get_profile_photos(chat_id=target_id, limit = 1)[0]
					app.download_media(profile_picture, "downloads\in-data.png")

					meme = Image.open(r'templates/is-this-meme.jpg')
					profile_picture = Image.open(r'downloads/in-data.png')
					profile_picture_mask = Image.open(r'templates/is-this-meme-mask.png')

					scaled_profile_picture = profile_picture.resize((412, 470))
					meme.paste(scaled_profile_picture, (250, 170), profile_picture_mask)

					subtext = "Is this " + message_parts[0].lower() + "?"
					uppertext = message_parts[1].lower()
					font = ImageFont.truetype("impact.ttf", 60)
					draw = ImageDraw.Draw(meme)

					text_w, text_h = draw.textsize(subtext, font)
					half_text_w = text_w / 2
					width_post = (1400 / 2) - half_text_w
					
					draw.text((width_post, 680),subtext,(255,255,255),font=font)

					text_w, text_h = draw.textsize(uppertext, font)
					half_text_w = text_w / 2
					width_post = 1058 - half_text_w

					draw.text((width_post, 208),uppertext,(255,255,255),font=font)

					meme.save("out.png")
					app.send_photo(send_to, "out.png")



app = Client("ArkangelDev")
my_handler = MessageHandler(handleMemes)
app.add_handler(my_handler)
app.run()

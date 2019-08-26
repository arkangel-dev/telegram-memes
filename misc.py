import pyrogram
import time
from PyDictionary import PyDictionary

def processing(app, send_to, message):
	if (not message):
		message = "processing"
	message_id = app.send_message(send_to, "`" + message + "...`", parse_mode="markdown").message_id
	counter = 0
	stringDot = "."
	for x in range(0, 27):
		if (counter == 3):
			stringDot = "."
			counter = 0
		
		counter += 1
		try:
			app.edit_message_text(send_to, message_id, "`" + message + stringDot + "`", parse_mode="markdown")
		except pyrogram.errors.exceptions.bad_request_400.MessageIdInvalid as e:
			# app.send_message(send_to, "`<<" + str(e) + ">>` \n``AHHHHHHH... Im dying!``", parse_mode="markdown")
			
			return
		stringDot += "."
		time.sleep(1)

def getMeaning(app, send_to, word):
	returnObject = "The meaning of " + str(word).lower() + " is the following : \n\n"
	dictionary=PyDictionary()
	data = dictionary.meaning(word.lower())
	print(data)
	for y in data:
		returnObject += y + "\n"
		for x in data[y]:
			returnObject += "🔸 `" + str(x).capitalize() + "`\n"
		print(y)
	
		app.send_message(send_to, returnObject, parse_mode="markdown")
	
def average_colour(image):
	colour_tuple = [None, None, None]
	for channel in range(3):
		# Get data for one channel at a time
		pixels = image.getdata(band=channel)
		values = []
		for pixel in pixels:
			values.append(pixel)
		colour_tuple[channel] = sum(values) / len(values)
	return tuple(colour_tuple)
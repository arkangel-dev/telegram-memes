import pyrogram
import time
from PyDictionary import PyDictionary
from PIL import Image, ImageDraw, ImageFont



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

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import sys

def drawText(msg, pos, img):
    draw = ImageDraw.Draw(img)
    fontSize = 56
    lines = []

    font = ImageFont.truetype("impact.ttf", fontSize)
    w, h = draw.textsize(msg, font)

    imgWidthWithPadding = img.width * 0.99

    # 1. how many lines for the msg to fit ?
    lineCount = 1
    if(w > imgWidthWithPadding):
        lineCount = int(round((w / imgWidthWithPadding) + 1))

    if lineCount > 2:
        while 1:
            fontSize -= 2
            font = ImageFont.truetype("impact.ttf", fontSize)
            w, h = draw.textsize(msg, font)
            lineCount = int(round((w / imgWidthWithPadding) + 1))
            print("try again with fontSize={} => {}".format(fontSize, lineCount))
            if lineCount < 3 or fontSize < 10:
                break


    print("img.width: {}, text width: {}".format(img.width, w))
    print("Text length: {}".format(len(msg)))
    print("Lines: {}".format(lineCount))


    # 2. divide text in X lines
    lastCut = 0
    isLast = False
    for i in range(0,lineCount):
        if lastCut == 0:
            cut = (len(msg) / lineCount) * i
        else:
            cut = lastCut

        if i < lineCount-1:
            nextCut = (len(msg) / lineCount) * (i+1)
        else:
            nextCut = len(msg)
            isLast = True

        print("cut: {} -> {}".format(cut, nextCut))

        # make sure we don't cut words in half
        if nextCut == len(msg) or msg[nextCut] == " ":
            print("may cut")
        else:
            print("may not cut")
            while msg[nextCut] != " ":
                nextCut += 1
            print("new cut: {}".format(nextCut))

        line = msg[cut:nextCut].strip()

        # is line still fitting ?
        w, h = draw.textsize(line, font)
        if not isLast and w > imgWidthWithPadding:
            print("overshot")
            nextCut -= 1
            while msg[nextCut] != " ":
                nextCut -= 1
            print("new cut: {}".format(nextCut))

        lastCut = nextCut
        lines.append(msg[cut:nextCut].strip())

    print(lines)

    # 3. print each line centered
    lastY = -h
    if pos == "bottom":
        lastY = img.height - h * (lineCount+1) - 10

    for i in range(0,lineCount):
        w, h = draw.textsize(lines[i], font)
        textX = img.width/2 - w/2
        #if pos == "top":
        #    textY = h * i
        #else:
        #    textY = img.height - h * i
        textY = lastY + h
        draw.text((textX-2, textY-2),lines[i],(0,0,0),font=font)
        draw.text((textX+2, textY-2),lines[i],(0,0,0),font=font)
        draw.text((textX+2, textY+2),lines[i],(0,0,0),font=font)
        draw.text((textX-2, textY+2),lines[i],(0,0,0),font=font)
        draw.text((textX, textY),lines[i],(255,255,255),font=font)
        lastY = textY
    return img

def sendSimpleImage(app,send_to, img, message):
	app.delete_messages(send_to, message["message_id"])
	reply_message_bool = message["reply_to_message"]
	if reply_message_bool: 
		reply_message = message["reply_to_message"]["message_id"]
	if not reply_message_bool:
		app.send_photo(send_to, img)
	else:
		app.send_photo(send_to, img, reply_to_message_id=reply_message)


def sendSticker(app,send_to, sticker, message):
    app.delete_messages(send_to, message["message_id"])
    reply_message_bool = message["reply_to_message"]
    if reply_message_bool: 
        reply_message = message["reply_to_message"]["message_id"]

    if not reply_message_bool:
        app.send_sticker(send_to, sticker)
    else:
        app.send_sticker(send_to, sticker, reply_to_message_id=reply_message)



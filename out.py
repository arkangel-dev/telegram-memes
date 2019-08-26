from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw



def drawTextWithOutline(draw, text, x, y, fsize):
    draw.text((x-2, y-2), text,(0,0,0),font=fsize)
    draw.text((x+2, y-2), text,(0,0,0),font=fsize)
    draw.text((x+2, y+2), text,(0,0,0),font=fsize)
    draw.text((x-2, y+2), text,(0,0,0),font=fsize)
    draw.text((x, y), text, (255,255,255), font=fsize)
    return


class memes:
	def oneDoesNotSimply(text):
		"""
		The "one does not simply" meme from Lord of the Rings. 
		More : https://knowyourmeme.com/memes/one-does-not-simply-walk-into-mordor
		"""
		img = Image.open("templates/one-does-not-simply.jpg")
		draw = ImageDraw.Draw(img)
		font = ImageFont.truetype("impact.ttf", 42)
		w, h = draw.textsize(text, font)
		drawTextWithOutline(draw,text, img.width/2 - w/2, 280, font)
		img.save("out.jpg")

	def historyAliensGuy(text):
		"""
		History.com's Aliens guy42
		More : https://knowyourmeme.com/memes/ancient-aliens
		"""
		img = Image.open("templates/history-aliens.jpg")
		draw = ImageDraw.Draw(img)
		font = ImageFont.truetype("impact.ttf", 50)
		w, h = draw.textsize(text, font)
		drawTextWithOutline(draw,text, img.width/2 - w/2, 377, font)
		img.save("out.jpg")

	def toyStoryMeme(text):
		img = Image.open("templates/woody-buzz.jpg")
		draw = ImageDraw.Draw(img)
		font = ImageFont.truetype("impact.ttf", 45)
		w, h = draw.textsize(text, font)
		w1, h1 = draw.textsize(text + " Everywhere", font)
		drawTextWithOutline(draw,str(text).capitalize(), img.width/2 - w/2, 2, font)
		drawTextWithOutline(draw,str(text).capitalize() + " Everywhere", img.width/2 - w1/2, 250, font)
		img.save("out.jpg")


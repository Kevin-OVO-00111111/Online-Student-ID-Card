from PIL import Image, ImageDraw, ImageFont

img = Image.new("RGB", (400, 200), "white")
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("fonts/mingliub.ttf", 40)
draw.text((50, 50), "測試中文字", font=font, fill="black")
img.show()
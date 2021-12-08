from PIL import Image, ImageDraw
def createImg(txt) :
    text = txt + str(i)

    new = Image.new('RGB', (200, 200), color=(255, 148, 91))

    d = ImageDraw.Draw(new)
    # d.text((width,height),text,fill=(R,G,B))
    d.text((50, 100), text, fill=(255, 255, 255))
    name = "img/" + text + ".jpg"
    new.save(name)
for i in range(50):
    createImg("Rép ")
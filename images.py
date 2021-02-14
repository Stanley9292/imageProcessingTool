from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')

print(img)
print(img.format)
print(img.size)
print(img.mode)
print(dir(img))

filtered_image = img.filter(ImageFilter.BLUR)
filtered_image = img.convert('L')

crooked = filtered_image.rotate(180)

crooked.save("blurred.png", 'png')

crooked.show()


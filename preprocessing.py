import os
from PIL import Image, ImageFile
"""
RESIZE IMAGES WITH PADDING


"""
#desired picture size in px
desired_size = 75

TESTING = False
if TESTING:
	dirs = ["TestImages"]
else:
	dirs = ["Cat", "Dog"]

for d in dirs:
	image_names = os.listdir(d)
	for img_name in image_names:
		try:
			img = Image.open(os.path.join(d, img_name))
		except Exception as e:
			print(str(e), img_name)

		old_size = img.size
		ratio = float(desired_size)/max(old_size)
		new_size = tuple([int(x*ratio) for x in old_size])
		img = img.resize(new_size, Image.ANTIALIAS)
		new_img = Image.new("RGB", (desired_size, desired_size))
		new_img.paste(img, ((desired_size-new_size[0])//2,
                    (desired_size-new_size[1])//2))
		new_img = new_img.convert('L')
		save_path = os.path.join(os.path.join(d,"resized"), img_name)
		new_img.save(save_path, format="jpeg")

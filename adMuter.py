from PIL import Image
from PIL import ImageFilter
import tesserocr
import sys

# Open the image file
image = Image.open('adZoom.jpg')

# Get the time stamp

# 1850, 1100
# 2700, 1800

# Cropped image of above dimension
# (It will not change original image)
# im1 = im.crop((left, top, right, bottom))

# Crop the time
image = image.crop((1850, 1100, 2800, 1800))

# Scale the image
width, height = image.size
newsize = (int(width/4), int(height/4))
image = image.resize(newsize)

# Convert to greyscale
# image = image.convert('L')

# image = image.filter(ImageFilter.SHARPEN);
# image = image.filter(ImageFilter.MaxFilter(7))
# image = image.filter(ImageFilter.MinFilter(7))
# image = image.filter(ImageFilter.SHARPEN);

# image.save('bw.png')

api = tesserocr.PyTessBaseAPI()
api.SetImage(image)
text = api.GetUTF8Text()

# Print the extracted text
print('"'+text+'"')

# convert any ; into :
text = text.replace(";",":")

adFound = False

# Look for exactly one ":"
if(text.count(":") == 1):
	
	# Look for minutes on the left
	minutes = text.split(":")[0][-1]

	# Look for seconds on the right
	seconds = text.split(":")[1][:2]

	if(minutes.isdigit() and seconds.isdigit()):
		print("Found an Ad!")
		print("Mute for",minutes,":",seconds)
		adFound = True

if not adFound:
	print("Not an Ad")

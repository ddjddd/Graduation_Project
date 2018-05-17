import requests
from io import BytesIO
from PIL import Image, ImageDraw
import cognitive_face as CF

KEY = '5d2f03e34f454a91ba2cce29492bbc60'  # Replace with a valid subscription key (keeping the quotes in place).
CF.Key.set(KEY)

BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)

image_path = "../resource/image/image1.jpg"
image_data = open(image_path, "rb").read()

# You can use this example JPG or replace the URL below with your own URL to a JPEG image.
# img_url = 'https://raw.githubusercontent.com/Microsoft/Cognitive-Face-Windows/master/Data/detection1.jpg'
img_url = 'https://i.ytimg.com/vi/yv2vnXjP3E0/maxresdefault.jpg'
faces = CF.face.detect(image_path, attributes="age,gender,emotion")


print(faces)

#Convert width height to a point in a rectangle
def getRectangle(faceDictionary):
    rect = faceDictionary['faceRectangle']
    left = rect['left']
    top = rect['top']
    bottom = left + rect['height']
    right = top + rect['width']
    return ((left, top), (bottom, right))

#Download the image from the url
response = requests.get(img_url)
img = Image.open(BytesIO(response.content))

#For each face returned use the face rectangle and draw a red box.
draw = ImageDraw.Draw(img)
for face in faces:
    draw.rectangle(getRectangle(face), outline='red')

#Display the image in the users default image browser.
img.show()


import openai
import requests
from PIL import Image
import config

#  OpenAI API KEY
openai.api_key = config.openai_token

#  Prompt
prompt = input('Enter your prompt: ')
print('Generating . . .')

#  OpenAI Model
response = openai.Image.create(
    prompt=prompt,
    n=1,
    size='1024x1024')

#  URL of generated image
image_url = response['data'][0]['url']

# Download and save the image
response = requests.get(image_url)
image_path = 'images/image.jpg'
with open(image_path, 'wb') as file:
    file.write(response.content)
print('Generated !')

#  SHOW GENERATED IMAGE
img = Image.open(image_path)
img.show()
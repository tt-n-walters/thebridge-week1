import requests
import time

while True:
  response = requests.get("https://random.dog/woof")

  image_link = response.text
  print("https://random.dog/" + image_link)

  time.sleep(5)
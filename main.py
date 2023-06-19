import streamlit as st
import requests

#st.set_page_config(layout="wide")
#Prepare API key and URL
api_key = "ecvh6WQArTASQ1sCd81lMHcSmBoyWtjniQmlhuh4"
url = "https://api.nasa.gov/planetary/apod?api_key=ecvh6WQArTASQ1sCd81lMHcSmBoyWtjniQmlhuh4"
#Get request data as a dicionary
request = requests.get(url)
content = request.json()
print(content)
#Get date and title
date = content['date']
st.title("Astronomy photo of the day: " + date)
title = content['title']
st.write(title)
#Download the Image
image_url = content["hdurl"]
image_request = requests.get(image_url)
with open("image.jpg", "wb") as file:
    file.write(image_request.content)
st.image("image.jpg")
#Get Description
description = content['explanation']
st.write(description)



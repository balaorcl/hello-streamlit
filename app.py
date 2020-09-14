import streamlit as st

# Text/Title
st.title("Streamlit Tutorials")

# Header/Subheader
st.header("This is a header")
st.subheader("This is a subheader")

# Text
st.text("Hello Streamlit")

# Markdown
st.markdown("### This is a markdown")

# Error/Colorful Text
st.success("Successful")

st.info("Information!")

st.warning("This is a warning")

st.error("This is an error Danger")

st.exception("NameError('name three not defined')")

#Get Help Info About Python
st.help(range)

# Writing Text
st.write("Text with write")

st.write(range(10))

# Images
from PIL import Image
img = Image.open("example.jpg")
st.image(img, width=300, caption="Simple Image")

# For Video
# vid_file = open("example.mp4", "rb").read()
# st.video(vid_file)

# Audio
# audio_file = open("example.mp3", "rb").read()
# st.audio(audio_file,format="audio/mp3")

# Widget
# Checkbox
if st.checkbox("Show/Hide"):
    st.text("Showing or Hiding Widget")

# Radio button
status = st.radio("What's your status", ("Active", "Inactive"))

if status == "Active":
    st.success("You are Active")
else:
    st.warning("Inactive, Activate")    

# SelectBox
occupation = st.selectbox("Your Occupation", ["Programmer", 
                                              "Data Scientist",
                                              "Doctor"])
st.write("You selected this option", occupation)         

# Multiselect
location = st.multiselect("Where do you work?", 
                          ("London","New York","Accra", "Kiev","Nepal"))
st.write("You selected", len(location), "locations ")                          

# Slider
level = st.slider("What is your level?", 1, 5)

# Buttons
st.button("Simple Button")

if st.button("About"):
    st.text("Streamlit is Cool")

# Text Input
firstname = st.text_input("Enter Your First Name", "Type Here..")
if st.button("Submit"):
    result = firstname.title()
    st.success(result)

# Text Area
message = st.text_area("Enter Your message", "Type Here..")
if st.button("Submit1"):
    result = message.title()
    st.success(result)

# Date Input
import datetime
today = st.date_input("Today is", datetime.datetime.now())







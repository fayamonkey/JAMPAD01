import streamlit as st

st.set_page_config(page_title="Jam Pad", layout="centered")

st.title("🎶 Jam Pad 🎶")
st.write("Click a button to play a sound effect and spice up your Zoom calls!")

# A dictionary of 9 sound labels mapped to direct links to .mp3 files.
# These sample sounds are from various free sources. Feel free to replace
# the URLs with your own. Make sure they are direct links to the MP3 files.
sound_urls = {
    "Applause": "https://www.soundjay.com/human/applause-01.mp3",
    "Air Horn": "https://www.soundjay.com/misc/air-horn-01.mp3",
    "Boo": "https://www.soundjay.com/human/boo-01.mp3",
    "Laugh Track": "https://www.soundjay.com/human/laugh-01.mp3",
    "Drum Roll": "https://www.soundjay.com/misc/drum-roll-01.mp3",
    "Tada": "https://www.soundjay.com/human/child-woohoo-1.mp3",
    "Aww": "https://www.soundjay.com/human/crowd-aww-01.mp3",
    "Oooooh": "https://www.soundjay.com/human/crowd-ohh-01.mp3",
    "Sad Trombone": "https://www.soundjay.com/human/sad-trombone-01.mp3",
}

# Create a 3x3 grid of buttons using columns
# The approach below: we chunk the dictionary items in groups of 3
sound_items = list(sound_urls.items())
for i in range(0, 9, 3):
    cols = st.columns(3)
    for j in range(3):
        # Make sure we don't go out of range if your dict has fewer than 9 items
        if i + j < len(sound_items):
            sound_label, sound_url = sound_items[i + j]
            if cols[j].button(sound_label):
                # Insert an HTML <audio> snippet that autoplays the chosen sound
                st.markdown(
                    f"""
                    <audio autoplay>
                    <source src="{sound_url}" type="audio/mpeg">
                    </audio>
                    """,
                    unsafe_allow_html=True
                )

st.write("---")
st.write("Feel free to replace the sound URLs in the code with your own favorites!")


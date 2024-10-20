import streamlit as st
import random

# Title
st.title("🎃 Halloween Avatar Generator 🎃")

# Avatar customization options
st.sidebar.header("Select Your Preferences")

# Option 1: Choose a costume
costume_options = ["Witch", "Vampire", "Ghost", "Zombie"]
selected_costume = st.sidebar.selectbox("Choose a Costume", costume_options)

# Option 2: Choose a hat
hat_options = ["Pointy Hat", "Top Hat", "No Hat"]
selected_hat = st.sidebar.selectbox("Choose a Hat", hat_options)

# Option 3: Choose a color
selected_color = st.sidebar.color_picker("Pick a Color", "#FF5733")

# Option 4: Choose an accessory
accessory_options = ["Broom", "Cape", "Lantern", "None"]
selected_accessory = st.sidebar.selectbox("Choose an Accessory", accessory_options)

# Generate random avatar based on selections
def generate_avatar():
    costume = random.choice(costume_options)
    hat = random.choice(hat_options)
    color = selected_color
    accessory = random.choice(accessory_options)
    return costume, hat, color, accessory

if st.button("Generate Avatar"):
    costume, hat, color, accessory = generate_avatar()
    st.write(f"### Your Random Halloween Avatar")
    st.write(f"- **Costume:** {costume}")
    st.write(f"- **Hat:** {hat}")
    st.write(f"- **Color:** {color}")
    st.write(f"- **Accessory:** {accessory}")
    st.markdown(f"<div style='color:{color}; font-size:100px;'>👻</div>", unsafe_allow_html=True)
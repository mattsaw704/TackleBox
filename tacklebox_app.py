import streamlit as st

# Define gear categories and items
tacklebox = {
    "Rods & Reels": ["Spinning Rod & Reel", "Baitcasting Combo", "Fly Rod"],
    "Line Types": ["Monofilament", "Braided Line", "Fluorocarbon"],
    "Hooks": ["Worm Hooks", "Treble Hooks", "Circle Hooks"],
    "Lures & Baits": ["Soft Plastics", "Hard Baits", "Spinnerbaits & Buzzbaits", "Jigs", "Live Bait"],
    "Terminal Tackle": ["Sinkers/Weights", "Swivels", "Bobbers/Floats"],
    "Tools & Accessories": ["Needle-nose Pliers", "Line Clippers", "Fish Gripper", "Measuring Tape", "Tacklebox Organizer"],
    "Specialty Gear": ["Fish Finder (Virtual)", "Polarized Glasses (Virtual)", "Digital Logbook"]
}

# Initialize session state for uploaded images
if "images" not in st.session_state:
    st.session_state.images = {}

st.title("🎣 Virtual Fishing Tacklebox")

# Search bar
search_query = st.text_input("🔍 Search for gear")

# Filter and display gear items
for category, items in tacklebox.items():
    filtered_items = [item for item in items if search_query.lower() in item.lower()]
    if filtered_items:
        st.subheader(f"📦 {category}")
        for item in filtered_items:
            col1, col2 = st.columns([1, 3])
            with col1:
                if item in st.session_state.images:
                    st.image(st.session_state.images[item], width=100)
                else:
                    st.image("https://via.placeholder.com/100", width=100)
            with col2:
                st.markdown(f"**{item}**")
                uploaded_file = st.file_uploader(f"Upload image for {item}", type=["png", "jpg", "jpeg"], key=item)
                if uploaded_file:
                    st.session_state.images[item] = uploaded_file

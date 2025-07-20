# app.py
# This is the main file for your ClimaFit website, now with a refined header layout!

import streamlit as st
import requests
import random # For simulating body type detection
from outfit_data import outfits, BODY_TYPES, OCCASIONS, STYLES # Your outfit catalog

# --- IMPORTANT: Your OpenWeatherMap API Key! ---
# This is your specific API key.
# Make sure your actual API key is pasted here correctly.
WEATHER_API_KEY = "d9f0422cdfdb96db5a5fdb74667cbcf5" # <<< Your working API key should be here!
BASE_WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather"

# --- Function to Get Weather (Your AI Assistant's "Weather Reporter") ---
def get_weather(city_name):
    params = {
        "q": city_name,
        "appid": WEATHER_API_KEY,
        "units": "metric"
    }
    try:
        response = requests.get(BASE_WEATHER_URL, params=params)
        response.raise_for_status()
        data = response.json()
        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]
        return temp, description
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching weather for {city_name}: {e}. Please check city name or your API key.")
        return None, None

# --- Function to Recommend Outfits (The AI's "Brain"!) ---
def recommend_outfits(body_type, current_temp, weather_desc_lower, occasion, style):
    recommended = []
    for outfit in outfits:
        temp_match = (outfit["suitable_weather_temps_min"] <= current_temp <= outfit["suitable_weather_temps_max"])
        weather_keyword_match = any(kw in weather_desc_lower for kw in outfit["suitable_weather_keywords"])
        body_type_match = body_type in outfit["suitable_body_types"]
        occasion_match = occasion in outfit["suitable_occasions"]
        style_match = style in outfit["style_keywords"]

        score = 0
        if temp_match and weather_keyword_match:
            score += 2
        if body_type_match:
            score += 1
        if occasion_match:
            score += 1
        if style_match:
            score += 1

        if score >= 2:
            recommended.append({
                "outfit": outfit,
                "score": score,
                "matched_criteria": {
                    "weather": temp_match and weather_keyword_match,
                    "body_type": body_type_match,
                    "occasion": occasion_match,
                    "style": style_match
                }
            })
    recommended.sort(key=lambda x: x["score"], reverse=True)
    return recommended

# --- Streamlit Website Layout & Logic ---

st.set_page_config(layout="wide", page_title="ClimaFit")

# --- Session state for simulated login and camera ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""
if "show_login_form" not in st.session_state:
    st.session_state.show_login_form = False
if "captured_image" not in st.session_state:
    st.session_state.captured_image = None
if "identified_body_type" not in st.session_state:
    st.session_state.identified_body_type = None

# --- TOP HEADER & DYNAMIC BUTTONS ---
# Use a container for the entire header section to keep it grouped
with st.container():
    # Create columns for the logo/title block and the dynamic buttons (login/logout)
    header_main_col, header_buttons_col = st.columns([4, 1])

    with header_main_col:
        # Nested columns for logo and text
        logo_col, text_col = st.columns([0.5, 3]) # Adjust ratio as needed for your logo size

        with logo_col:
            # Your custom logo from local folder!
            # Adjust width as needed to fit your logo's aspect ratio.
            st.image("outfit_images/image.png", width=250) # Reduced width for better alignment

        with text_col:
            # --- INCREASED SIZE OF CLIMAFIT HEADER HERE! ---
            # Using st.markdown with H1 for largest possible text
            st.markdown("# ClimaFit") 
            st.markdown("### Your Personalized Outfit Recommender ☀️") # Main tagline
            st.markdown("*Made with ❤️ for fashion enthusiasts everywhere!*") # Secondary tagline

    with header_buttons_col:
        st.write("") # Add some space to push buttons down slightly
        st.write("") # More space

        # --- Login/Logout Button ---
        if st.session_state.logged_in:
            st.success(f"Welcome, {st.session_state.username}!")
            if st.button("Logout"):
                st.session_state.logged_in = False
                st.session_state.username = ""
                st.session_state.show_login_form = False
                st.session_state.captured_image = None
                st.session_state.identified_body_type = None
                st.rerun()
        else:
            if st.button("Login / Sign Up"):
                st.session_state.show_login_form = not st.session_state.show_login_form

            if st.session_state.show_login_form:
                with st.expander("Access Account", expanded=True):
                    st.subheader("Login / Sign Up")
                    auth_option = st.radio("Choose:", ["Login", "Sign Up"], key="auth_option_expander")

                    with st.form("auth_form_expander"):
                        username = st.text_input("Username (e.g., your email)", key="username_expander")
                        password = st.text_input("Password", type="password", key="password_expander")

                        if auth_option == "Login":
                            if st.form_submit_button("Login", use_container_width=True):
                                if username and password:
                                    st.session_state.logged_in = True
                                    st.session_state.username = username
                                    st.success(f"Logged in as {username}!")
                                    st.session_state.show_login_form = False
                                    st.rerun()
                                else:
                                    st.error("Please enter both username and password.")
                        elif auth_option == "Sign Up":
                            if st.form_submit_button("Sign Up", use_container_width=True):
                                if username and password:
                                    st.session_state.logged_in = True
                                    st.session_state.username = username
                                    st.success(f"Account created for {username} and logged in!")
                                    st.session_state.show_login_form = False
                                    st.rerun()
                                else:
                                    st.error("Please enter both username and password.")
                    st.markdown("*(Note: This is a frontend-only simulated login/signup for demonstration.)*")


st.write("---") # Separator line after header

# --- Main Application Content (Always visible, but features enabled only if logged in) ---
control_column, display_column = st.columns([1, 3])

with control_column:
    st.header("Your Preferences")

    is_disabled = not st.session_state.logged_in

    city = st.text_input("Enter your City:", value="Hyderabad", disabled=is_disabled)
    weather_info_placeholder = st.empty()

    current_temp, current_weather_desc = None, None
    if city and not is_disabled:
        current_temp, current_weather_desc = get_weather(city)
        if current_temp is not None:
            weather_info_placeholder.info(f"Weather in {city}: **{current_weather_desc.title()}**, **{current_temp}°C**")
    elif is_disabled:
        weather_info_placeholder.info("Login to enable weather features.")

    st.markdown("---")

    # --- Camera Input for User Photo and Body Shape Analysis ---
    st.subheader("Capture Your Look (Optional)")
    
    captured_file = st.camera_input("Take a picture", disabled=is_disabled)

    if captured_file is not None:
        st.session_state.captured_image = captured_file
        st.image(st.session_state.captured_image, caption="Your captured photo", use_container_width=True)
        
        if st.button("Analyze My Body Shape from Photo", disabled=is_disabled):
            with st.spinner("Analyzing your body shape... (Simulated AI)"):
                simulated_body_type = random.choice(BODY_TYPES)
                st.session_state.identified_body_type = simulated_body_type
                st.success(f"AI identified your body shape as: **{simulated_body_type}**")
                st.info("*(Note: This is a simulated AI feature for demonstration. A real implementation would use advanced Computer Vision.)*")
            st.rerun()

    if st.session_state.identified_body_type:
        st.write(f"**AI Suggested Body Type:** {st.session_state.identified_body_type}")
        default_body_type_index = BODY_TYPES.index(st.session_state.identified_body_type)
    else:
        default_body_type_index = 0

    st.markdown("---")

    selected_body_type = st.selectbox("Select your Body Type:", BODY_TYPES, index=default_body_type_index, disabled=is_disabled)
    selected_occasion = st.selectbox("Select Occasion:", OCCASIONS, disabled=is_disabled)
    selected_style = st.selectbox("Select Style Preference:", STYLES, disabled=is_disabled)

    st.markdown("---")

    # --- NEW: My Digital Closet Section ---
    st.subheader("My Digital Closet")
    st.info("Upload your clothing items here! (Simulated AI Categorization)")

    uploaded_clothing_file = st.file_uploader("Upload a clothing item image:", type=["jpg", "jpeg", "png"], disabled=is_disabled)

    if uploaded_clothing_file is not None:
        st.image(uploaded_clothing_file, caption="Uploaded Item", use_container_width=True)
        if st.button("Analyze & Add to Closet", disabled=is_disabled):
            with st.spinner("Analyzing clothing item... (Simulated AI)"):
                # Simulate AI identifying clothing type and color
                simulated_clothing_type = random.choice(["Top", "Bottom", "Dress", "Outerwear", "Shoes", "Accessory"])
                simulated_clothing_color = random.choice(["Red", "Blue", "Green", "Black", "White", "Gray", "Yellow", "Pink"])
                
                new_closet_item = {
                    "image_data": uploaded_clothing_file.getvalue(), # Store bytes data
                    "type": simulated_clothing_type,
                    "color": simulated_clothing_color
                }
                st.session_state.digital_closet_items.append(new_closet_item)
                st.success(f"AI identified: **{simulated_clothing_color} {simulated_clothing_type}** added to your closet!")
                st.rerun() # Rerun to update the closet display

    if st.session_state.digital_closet_items:
        st.markdown("---")
        st.subheader("Your Closet Items:")
        # Display closet items in a grid
        closet_cols = st.columns(3)
        for i, item in enumerate(st.session_state.digital_closet_items):
            with closet_cols[i % 3]: # Display up to 3 items per row
                st.image(item["image_data"], caption=f"{item['color']} {item['type']}", use_container_width=True)
    else:
        st.info("Your digital closet is empty. Upload items to start building it!")

    st.markdown("---") # Separator before recommendations button

    get_recommendations_button = st.button("✨ Get Outfit Recommendations", disabled=is_disabled)

with display_column:
    st.header("Your Top Picks!")
    recommendation_display_area = st.empty()

    if is_disabled:
        recommendation_display_area.info("Please login to get personalized outfit recommendations!")
    elif get_recommendations_button:
        if current_temp is None:
            recommendation_display_area.error("Please make sure weather data is loaded successfully before getting recommendations.")
        else:
            with st.spinner("Generating your personalized outfits..."):
                top_outfits = recommend_outfits(
                    selected_body_type,
                    current_temp,
                    current_weather_desc.lower(),
                    selected_occasion,
                    selected_style
                )

                if top_outfits:
                    recommendation_display_area.empty()
                    st.subheader("Here are your Top Picks!")
                    st.write("")

                    # Custom CSS for the card effect
                    st.markdown("""
                        <style>
                        .outfit-card {
                            border: 1px solid #ddd;
                            border-radius: 10px;
                            padding: 15px;
                            margin-bottom: 20px;
                            box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
                            background-color: #f9f9f9;
                            display: flex;
                            flex-direction: column;
                            height: 100%; /* Ensure cards in a row have equal height */
                        }
                        .outfit-card img {
                            border-radius: 8px;
                            margin-bottom: 10px;
                        }
                        .outfit-card h5 {
                            color: #333;
                            margin-bottom: 5px;
                        }
                        .outfit-card p {
                            font-size: 0.9em;
                            color: #555;
                            flex-grow: 1; /* Allow description to take available space */
                        }
                        .outfit-card .ai-says {
                            font-style: italic;
                            color: #007bff; /* A nice blue color for AI text */
                            font-size: 0.85em;
                            margin-top: 10px;
                        }
                        .outfit-card .score {
                            font-size: 0.75em;
                            color: #888;
                            text-align: right;
                            margin-top: 5px;
                        }
                        </style>
                    """, unsafe_allow_html=True)

                    # Display up to 6 recommendations in a grid
                    cols_per_row = 3
                    num_recommendations_to_show = min(len(top_outfits), 6)
                    
                    for i in range(num_recommendations_to_show):
                        if i % cols_per_row == 0:
                            current_row_cols = st.columns(cols_per_row)
                        
                        with current_row_cols[i % cols_per_row]:
                            rec_item = top_outfits[i]
                            outfit = rec_item["outfit"]
                            
                            with st.container():
                                st.markdown(f'<div class="outfit-card">', unsafe_allow_html=True)
                                st.image(outfit["image_path"], caption=outfit["name"], use_container_width=True)
                                st.markdown(f'<h5>{outfit["name"]}</h5>', unsafe_allow_html=True)
                                st.write(f"{outfit['description']}")

                                justification = outfit["justification_template"].format(
                                    body_type=selected_body_type,
                                    weather_desc=current_weather_desc.lower(),
                                    occasion=selected_occasion.lower(),
                                    style=selected_style.lower()
                                )
                                st.markdown(f'<p class="ai-says"><b>AI Says:</b> <i>{justification}</i></p>', unsafe_allow_html=True)
                                st.markdown(f'<p class="score">Score: {rec_item["score"]}</p>', unsafe_allow_html=True)
                                st.markdown(f'</div>', unsafe_allow_html=True)

                else:
                    recommendation_display_area.warning("Oops! No outfits found matching all your criteria. Try adjusting your preferences a little!")

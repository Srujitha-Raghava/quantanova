# outfit_data.py
# This file stores a comprehensive set of outfits for StyleCast AI.
# It's the AI's detailed fashion encyclopedia!

# IMPORTANT: Image paths are now set to LOCAL paths, assuming you have downloaded
# the images and placed them in the 'outfit_images/' folder.
# This ensures your demo is robust and works offline!

outfits = [
    {
        "id": "o_1_casual_summer",
        "name": "Sunny Day Casual Look",
        "image_path": "outfit_images/outfit_1.jpg", # Local path
        "suitable_weather_temps_min": 25, # Temperatures in Celsius
        "suitable_weather_temps_max": 40,
        "suitable_weather_keywords": ["sunny", "warm", "hot", "clear"],
        "suitable_body_types": ["Rectangle", "Hourglass", "Pear", "Inverted Triangle", "Oval"],
        "suitable_occasions": ["Casual", "Everyday", "Outdoor", "Beach"],
        "style_keywords": ["light", "comfortable", "minimalist", "relaxed"],
        "description": "A light cotton t-shirt with denim shorts and sneakers. Perfect for a relaxed sunny day.",
        "justification_template": "This **{style}** outfit is perfect for your **{body_type}** shape, ideal for **{weather_desc}** weather, and fits a **{occasion}** vibe."
    },
    {
        "id": "o_2_work_professional",
        "name": "Professional Office Attire",
        "image_path": "outfit_images/outfit_2.png", # Local path
        "suitable_weather_temps_min": 10,
        "suitable_weather_temps_max": 25,
        "suitable_weather_keywords": ["mild", "cloudy", "cool"],
        "suitable_body_types": ["Inverted Triangle", "Rectangle", "Hourglass"],
        "suitable_occasions": ["Work", "Formal", "Business Meeting"],
        "style_keywords": ["classic", "elegant", "professional"],
        "description": "A tailored blazer over a silk blouse with a pencil skirt and heels. Sharp and chic for the office.",
        "justification_template": "This **{style}** ensemble is perfect for your **{body_type}** profile, suitable for **{weather_desc}** conditions, and highly recommended for a **{occasion}**."
    },
    {
        "id": "o_3_cozy_winter",
        "name": "Cozy Winter Layers",
        "image_path": "outfit_images/outfit_3.jpg", # Local path
        "suitable_weather_temps_min": -5,
        "suitable_weather_temps_max": 10,
        "suitable_weather_keywords": ["cold", "snow", "freezing", "chilly"],
        "suitable_body_types": ["Rectangle", "Pear", "Oval", "Hourglass", "Inverted Triangle"],
        "suitable_occasions": ["Casual", "Everyday", "Outdoor"],
        "style_keywords": ["warm", "layered", "comfortable"],
        "description": "A thick sweater, tailored wool coat, scarf, and boots. Ideal for cold, winter days.",
        "justification_template": "This warm and **{style}** outfit is great for your **{body_type}** shape when the weather is **{weather_desc}**, fitting a **{occasion}**."
    },
    {
        "id": "o_4_rainy_day_chic",
        "name": "Rainy Day Chic",
        "image_path": "outfit_images/outfit_4.jpg", # Local path
        "suitable_weather_temps_min": 5,
        "suitable_weather_temps_max": 20,
        "suitable_weather_keywords": ["rain", "drizzle", "cloudy"],
        "suitable_body_types": ["Hourglass", "Inverted Triangle", "Rectangle", "Pear"],
        "suitable_occasions": ["Everyday", "Work", "Casual"],
        "style_keywords": ["practical", "chic", "elegant"],
        "description": "A stylish trench coat, slim-fit jeans, and waterproof boots. Perfect for a rainy day.",
        "justification_template": "This **{style}** outfit is ideal for your **{body_type}** shape in **{weather_desc}** weather, suitable for a **{occasion}**."
    },
    {
        "id": "o_5_party_glam",
        "name": "Party Night Glam",
        "image_path": "outfit_images/outfit_5.jpg", # Local path
        "suitable_weather_temps_min": 15,
        "suitable_weather_temps_max": 30,
        "suitable_weather_keywords": ["clear", "mild", "warm"],
        "suitable_body_types": ["Hourglass", "Pear", "Rectangle", "Oval"],
        "suitable_occasions": ["Party", "Evening"],
        "style_keywords": ["trendy", "elegant", "glamorous"],
        "description": "A sparkling cocktail dress with heels and statement jewelry. Ready for a night out!",
        "justification_template": "For a **{occasion}** event, this **{style}** dress complements your **{body_type}** shape perfectly in **{weather_desc}** conditions."
    },
    {
        "id": "o_6_sporty_active",
        "name": "Sporty Active Wear",
        "image_path": "outfit_images/outfit_6.jpg", # Local path
        "suitable_weather_temps_min": 5,
        "suitable_weather_temps_max": 30,
        "suitable_weather_keywords": ["clear", "mild", "sunny", "cloudy"],
        "suitable_body_types": ["Rectangle", "Inverted Triangle", "Oval", "Hourglass"],
        "suitable_occasions": ["Sports", "Outdoor", "Casual"],
        "style_keywords": ["comfortable", "sporty", "active"],
        "description": "Breathable leggings, a performance top, and athletic shoes. Ideal for your workout.",
        "justification_template": "This **{style}** activewear is great for your **{body_type}** shape, suitable for **{weather_desc}** conditions and **{occasion}** activities."
    },
    {
        "id": "o_7_boho_chic",
        "name": "Boho Chic Ensemble",
        "image_path": "outfit_images/outfit_7.jpg", # Local path
        "suitable_weather_temps_min": 18,
        "suitable_weather_temps_max": 30,
        "suitable_weather_keywords": ["sunny", "mild", "warm"],
        "suitable_body_types": ["Pear", "Rectangle", "Hourglass", "Oval"],
        "suitable_occasions": ["Casual", "Outdoor", "Everyday", "Festival"],
        "style_keywords": ["boho", "comfortable", "trendy", "relaxed"],
        "description": "A flowy maxi dress with a denim vest and sandals. Perfect for a relaxed, artistic look.",
        "justification_template": "Embrace your **{body_type}** shape with this **{style}** outfit, ideal for **{weather_desc}** weather and a **{occasion}** setting."
    },
    {
        "id": "o_8_minimalist_elegance",
        "name": "Minimalist Elegance",
        "image_path": "outfit_images/outfit_8.jpg", # Local path
        "suitable_weather_temps_min": 15,
        "suitable_weather_temps_max": 28,
        "suitable_weather_keywords": ["mild", "clear", "cloudy"],
        "suitable_body_types": ["Rectangle", "Hourglass", "Inverted Triangle", "Oval"],
        "suitable_occasions": ["Work", "Formal", "Everyday", "Evening"],
        "style_keywords": ["minimalist", "elegant", "classic"],
        "description": "A crisp white button-down shirt, tailored black pants, and simple loafers. Effortlessly chic.",
        "justification_template": "This **{style}** look is perfect for your **{body_type}** profile, suitable for **{weather_desc}** conditions and a **{occasion}**."
    },
    {
        "id": "o_9_winter_formal",
        "name": "Winter Formal Evening",
        "image_path": "outfit_images/outfit_9.jpg", # Local path
        "suitable_weather_temps_min": 0,
        "suitable_weather_temps_max": 15,
        "suitable_weather_keywords": ["cold", "chilly", "clear"],
        "suitable_body_types": ["Hourglass", "Rectangle", "Oval", "Inverted Triangle"],
        "suitable_occasions": ["Formal", "Party", "Evening"],
        "style_keywords": ["elegant", "classic", "glamorous"],
        "description": "A long-sleeved velvet gown with closed-toe heels and a warm wrap. Sophisticated for cool evenings.",
        "justification_template": "For a **{occasion}** event in **{weather_desc}** weather, this **{style}** gown will flatter your **{body_type}** shape beautifully."
    },
    {
        "id": "o_10_summer_work",
        "name": "Summer Business Casual",
        "image_path": "outfit_images/outfit_10.jpg", # Local path
        "suitable_weather_temps_min": 20,
        "suitable_weather_temps_max": 35,
        "suitable_weather_keywords": ["warm", "sunny", "hot"],
        "suitable_body_types": ["Pear", "Rectangle", "Hourglass", "Oval"],
        "suitable_occasions": ["Work", "Everyday"],
        "style_keywords": ["comfortable", "professional", "light"],
        "description": "Light linen trousers, a breathable blouse, and comfortable flats. Ideal for a warm office day.",
        "justification_template": "This **{style}** ensemble is great for your **{body_type}** shape, perfect for **{weather_desc}** weather, and suitable for **{occasion}**."
    },
    {
        "id": "o_11_rainy_casual",
        "name": "Cozy Rainy Day",
        "image_path": "outfit_images/outfit_11.jpg", # Local path
        "suitable_weather_temps_min": 8,
        "suitable_weather_temps_max": 18,
        "suitable_weather_keywords": ["rain", "drizzle", "cloudy"],
        "suitable_body_types": ["Oval", "Rectangle", "Pear", "Hourglass"],
        "suitable_occasions": ["Casual", "Everyday"],
        "style_keywords": ["comfortable", "cozy", "practical"],
        "description": "A comfy hooded sweatshirt, joggers, and rain boots. Stay dry and warm on a wet day.",
        "justification_template": "For a **{occasion}** day in **{weather_desc}** weather, this **{style}** outfit offers comfort and protection for your **{body_type}** shape."
    },
    {
        "id": "o_12_sporty_cold",
        "name": "Cold Weather Workout",
        "image_path": "outfit_images/outfit_12.jpg", # Local path
        "suitable_weather_temps_min": -10,
        "suitable_weather_temps_max": 5,
        "suitable_weather_keywords": ["cold", "freezing", "snow"],
        "suitable_body_types": ["Inverted Triangle", "Rectangle", "Oval"],
        "suitable_occasions": ["Sports", "Outdoor"],
        "style_keywords": ["sporty", "warm", "active"],
        "description": "Thermal base layers, a fleece jacket, and insulated running pants. Ready for cold outdoor activities.",
        "justification_template": "This **{style}** activewear is ideal for your **{body_type}** shape in **{weather_desc}** conditions, perfect for **{occasion}**."
    },
    {
        "id": "o_13_trendy_street",
        "name": "Trendy Street Style",
        "image_path": "outfit_images/outfit_13.jpg", # Local path
        "suitable_weather_temps_min": 10,
        "suitable_weather_temps_max": 25,
        "suitable_weather_keywords": ["mild", "clear", "cloudy"],
        "suitable_body_types": ["Rectangle", "Hourglass", "Inverted Triangle", "Pear"],
        "suitable_occasions": ["Casual", "Party", "Everyday"],
        "style_keywords": ["trendy", "boho", "edgy"],
        "description": "Oversized graphic tee, ripped jeans, and chunky sneakers. A modern, edgy look.",
        "justification_template": "Show off your **{body_type}** shape with this **{style}** street look, great for **{weather_desc}** weather and a **{occasion}**."
    },
    {
        "id": "o_14_elegant_evening",
        "name": "Elegant Evening Wear",
        "image_path": "outfit_images/outfit_14.jpg", # Local path
        "suitable_weather_temps_min": 18,
        "suitable_weather_temps_max": 28,
        "suitable_weather_keywords": ["mild", "clear"],
        "suitable_body_types": ["Hourglass", "Pear", "Oval", "Rectangle"],
        "suitable_occasions": ["Formal", "Party", "Evening"],
        "style_keywords": ["elegant", "classic", "glamorous"],
        "description": "A sophisticated midi dress with delicate heels and a clutch. Perfect for a refined event.",
        "justification_template": "This **{style}** dress is a perfect match for your **{body_type}** shape, ideal for a **{occasion}** in **{weather_desc}** conditions."
    },
    {
        "id": "o_15_outdoor_adventure",
        "name": "Outdoor Adventure Gear",
        "image_path": "outfit_images/outfit_15.jpg", # Local path
        "suitable_weather_temps_min": 5,
        "suitable_weather_temps_max": 25,
        "suitable_weather_keywords": ["clear", "cloudy", "windy", "mild"],
        "suitable_body_types": ["Rectangle", "Inverted Triangle", "Oval", "Pear"],
        "suitable_occasions": ["Outdoor", "Sports"],
        "style_keywords": ["comfortable", "practical", "sporty"],
        "description": "Hiking pants, a moisture-wicking top, and sturdy hiking boots. Built for the trails.",
        "justification_template": "For your **{body_type}** shape and **{occasion}** adventures, this **{style}** gear is perfect for **{weather_desc}** weather."
    },
    {
        "id": "o_16_casual_chic_spring",
        "name": "Casual Chic Spring",
        "image_path": "outfit_images/outfit_16.jpg", # Local path
        "suitable_weather_temps_min": 15,
        "suitable_weather_temps_max": 25,
        "suitable_weather_keywords": ["mild", "sunny", "clear"],
        "suitable_body_types": ["Pear", "Rectangle", "Hourglass", "Oval"],
        "suitable_occasions": ["Everyday", "Casual"],
        "style_keywords": ["classic", "comfortable", "chic"],
        "description": "A light knit sweater, cropped trousers, and ballet flats. Effortlessly stylish for spring.",
        "justification_template": "This **{style}** outfit is great for your **{body_type}** shape in **{weather_desc}** weather, fitting a **{occasion}**."
    },
    {
        "id": "o_17_business_travel",
        "name": "Business Travel Comfort",
        "image_path": "outfit_images/outfit_17.jpg", # Local path
        "suitable_weather_temps_min": 10,
        "suitable_weather_temps_max": 25,
        "suitable_weather_keywords": ["mild", "cloudy", "clear"],
        "suitable_body_types": ["Rectangle", "Inverted Triangle", "Oval", "Hourglass"],
        "suitable_occasions": ["Work", "Everyday"],
        "style_keywords": ["comfortable", "professional", "practical"],
        "description": "Wrinkle-resistant blazer, comfortable dress pants, and stylish walking shoes. Ideal for business trips.",
        "justification_template": "For your **{body_type}** shape and a **{occasion}** trip in **{weather_desc}** conditions, this **{style}** outfit offers both comfort and professionalism."
    },
    {
        "id": "o_18_summer_party",
        "name": "Summer Garden Party",
        "image_path": "outfit_images/outfit_18.jpg", # Local path
        "suitable_weather_temps_min": 20,
        "suitable_weather_temps_max": 35,
        "suitable_weather_keywords": ["sunny", "warm", "clear"],
        "suitable_body_types": ["Hourglass", "Pear", "Rectangle", "Oval"],
        "suitable_occasions": ["Party", "Outdoor"],
        "style_keywords": ["elegant", "boho", "light"],
        "description": "A floral midi dress, wedge sandals, and a light cardigan. Perfect for an outdoor summer gathering.",
        "justification_template": "This **{style}** dress is a fantastic choice for your **{body_type}** shape, perfect for a **{occasion}** in **{weather_desc}** weather."
    },
    {
        "id": "o_19_cold_formal",
        "name": "Cold Weather Formal",
        "image_path": "outfit_images/outfit_19.jpg", # Local path
        "suitable_weather_temps_min": -5,
        "suitable_weather_temps_max": 8,
        "suitable_weather_keywords": ["cold", "chilly", "clear"],
        "suitable_body_types": ["Rectangle", "Inverted Triangle", "Oval"],
        "suitable_occasions": ["Formal", "Work", "Evening"],
        "style_keywords": ["elegant", "classic", "warm"],
        "description": "A sophisticated wool coat over a tailored jumpsuit with ankle boots. Ideal for cold formal events.",
        "justification_template": "This **{style}** ensemble is perfect for your **{body_type}** shape, providing warmth and elegance for a **{occasion}** in **{weather_desc}** weather."
    },
    {
        "id": "o_20_casual_winter_layers",
        "name": "Urban Winter Layers",
        "image_path": "outfit_images/outfit_20.jpg", # Local path
        "suitable_weather_temps_min": -10,
        "suitable_weather_temps_max": 0,
        "suitable_weather_keywords": ["very cold", "snow", "freezing"],
        "suitable_body_types": ["Rectangle", "Pear", "Hourglass", "Inverted Triangle", "Oval"],
        "suitable_occasions": ["Casual", "Everyday", "Outdoor"],
        "style_keywords": ["warm", "layered", "comfortable", "trendy"],
        "description": "A puffer jacket, thick scarf, beanie, and thermal jeans with snow boots. Stay super warm and stylish.",
        "justification_template": "For extreme **{weather_desc}** conditions, this **{style}** layered look is essential for your **{body_type}** shape, keeping you cozy for **{occasion}** activities."
    },
    {
        "id": "o_21_spring_casual",
        "name": "Light Spring Casual",
        "image_path": "outfit_images/outfit_21.jpg", # Local path
        "suitable_weather_temps_min": 10,
        "suitable_weather_temps_max": 20,
        "suitable_weather_keywords": ["mild", "sunny", "clear", "breezy"],
        "suitable_body_types": ["Rectangle", "Hourglass", "Pear", "Inverted Triangle", "Oval"],
        "suitable_occasions": ["Casual", "Everyday", "Outdoor"],
        "style_keywords": ["light", "comfortable", "classic"],
        "description": "A light denim jacket over a striped top, with chinos and loafers. Perfect for a breezy spring day.",
        "justification_template": "This **{style}** outfit is ideal for your **{body_type}** shape in **{weather_desc}** weather, suitable for a **{occasion}**."
    },
    {
        "id": "o_22_summer_evening",
        "name": "Summer Evening Out",
        "image_path": "outfit_images/outfit_22.jpg", # Local path
        "suitable_weather_temps_min": 22,
        "suitable_weather_temps_max": 30,
        "suitable_weather_keywords": ["warm", "clear", "mild"],
        "suitable_body_types": ["Hourglass", "Rectangle", "Pear"],
        "suitable_occasions": ["Party", "Evening", "Casual"],
        "style_keywords": ["elegant", "light", "trendy"],
        "description": "A satin slip dress with a light blazer and strappy heels. Perfect for a warm evening event.",
        "justification_template": "For a **{occasion}** in **{weather_desc}** conditions, this **{style}** dress will flatter your **{body_type}** shape beautifully."
    },
    {
        "id": "o_23_autumn_work",
        "name": "Autumn Work Chic",
        "image_path": "outfit_images/outfit_23.jpg", # Local path
        "suitable_weather_temps_min": 10,
        "suitable_weather_temps_max": 18,
        "suitable_weather_keywords": ["cool", "cloudy", "crisp"],
        "suitable_body_types": ["Inverted Triangle", "Rectangle", "Oval"],
        "suitable_occasions": ["Work", "Everyday"],
        "style_keywords": ["professional", "classic", "layered"],
        "description": "A fitted turtleneck, plaid trousers, and ankle boots. Smart and cozy for autumn workdays.",
        "justification_template": "This **{style}** look is perfect for your **{body_type}** profile, ideal for **{weather_desc}** conditions and a **{occasion}**."
    },
    {
        "id": "o_24_beach_vacation",
        "name": "Beach Vacation Ready",
        "image_path": "outfit_images/outfit_24.jpg", # Local path
        "suitable_weather_temps_min": 28,
        "suitable_weather_temps_max": 40,
        "suitable_weather_keywords": ["hot", "sunny", "humid", "beach"],
        "suitable_body_types": ["Rectangle", "Pear", "Hourglass", "Oval", "Inverted Triangle"],
        "suitable_occasions": ["Outdoor", "Casual", "Beach"],
        "style_keywords": ["light", "comfortable", "relaxed"],
        "description": "A vibrant swimsuit with a sheer cover-up, flip-flops, and sunglasses. Essential for a hot beach day.",
        "justification_template": "This **{style}** outfit is ideal for your **{body_type}** shape, perfect for a **{occasion}** in **{weather_desc}** weather."
    },
    {
        "id": "o_25_hiking_gear",
        "name": "Rugged Hiking Outfit",
        "image_path": "outfit_images/outfit_25.jpg", # Local path
        "suitable_weather_temps_min": 0,
        "suitable_weather_temps_max": 20,
        "suitable_weather_keywords": ["clear", "cloudy", "windy", "cool"],
        "suitable_body_types": ["Rectangle", "Inverted Triangle", "Oval", "Pear"],
        "suitable_occasions": ["Sports", "Outdoor"],
        "style_keywords": ["practical", "comfortable", "sporty"],
        "description": "Durable hiking pants, a moisture-wicking top, and sturdy hiking boots. Built for the trails.",
        "justification_template": "For your **{body_type}** shape and **{occasion}** adventures, this **{style}** gear is perfect for **{weather_desc}** weather."
    },
    {
        "id": "o_26_formal_event",
        "name": "Black Tie Event",
        "image_path": "outfit_images/outfit_26.jpg", # Local path
        "suitable_weather_temps_min": 10,
        "suitable_weather_temps_max": 25,
        "suitable_weather_keywords": ["mild", "clear"],
        "suitable_body_types": ["Hourglass", "Rectangle", "Inverted Triangle"],
        "suitable_occasions": ["Formal", "Party", "Evening"],
        "style_keywords": ["elegant", "glamorous", "classic"],
        "description": "A classic tuxedo/evening gown with formal shoes and minimal accessories. For the most prestigious events.",
        "justification_template": "This **{style}** ensemble is ideal for a **{occasion}** event in **{weather_desc}** conditions, perfectly suiting your **{body_type}** shape."
    },
    {
        "id": "o_27_casual_weekend",
        "name": "Weekend Brunch Look",
        "image_path": "outfit_images/outfit_27.jpg", # Local path
        "suitable_weather_temps_min": 15,
        "suitable_weather_temps_max": 28,
        "suitable_weather_keywords": ["mild", "sunny", "clear"],
        "suitable_body_types": ["Pear", "Rectangle", "Hourglass", "Oval"],
        "suitable_occasions": ["Casual", "Everyday", "Outdoor"],
        "style_keywords": ["comfortable", "trendy", "relaxed"],
        "description": "High-waisted jeans, a cute top, and stylish sandals. Perfect for a relaxed weekend brunch.",
        "justification_template": "This **{style}** outfit is great for your **{body_type}** shape, ideal for **{weather_desc}** weather, and fits a **{occasion}** vibe."
    },
    {
        "id": "o_28_cold_rainy",
        "name": "Heavy Rain Protection",
        "image_path": "outfit_images/outfit_28.jpg", # Local path
        "suitable_weather_temps_min": 0,
        "suitable_weather_temps_max": 10,
        "suitable_weather_keywords": ["heavy rain", "stormy", "cold"],
        "suitable_body_types": ["Rectangle", "Oval", "Inverted Triangle"],
        "suitable_occasions": ["Everyday", "Outdoor"],
        "style_keywords": ["practical", "warm", "comfortable"],
        "description": "A heavy waterproof jacket, insulated pants, and tall rain boots. For severe rainy and cold weather.",
        "justification_template": "For extreme **{weather_desc}** conditions, this **{style}** outfit provides maximum protection for your **{body_type}** shape, suitable for **{occasion}**."
    },
    {
        "id": "o_29_summer_sport",
        "name": "Summer Sports Day",
        "image_path": "outfit_images/outfit_29.jpg", # Local path
        "suitable_weather_temps_min": 25,
        "suitable_weather_temps_max": 40,
        "suitable_weather_keywords": ["hot", "sunny", "clear"],
        "suitable_body_types": ["Rectangle", "Inverted Triangle", "Hourglass", "Oval"],
        "suitable_occasions": ["Sports", "Outdoor"],
        "style_keywords": ["sporty", "light", "comfortable"],
        "description": "Athletic shorts, a breathable tank top, and running shoes. Perfect for hot weather sports.",
        "justification_template": "This **{style}** activewear is ideal for your **{body_type}** shape in **{weather_desc}** weather, perfect for **{occasion}** activities."
    },
    {
        "id": "o_30_classic_work",
        "name": "Classic Work Attire",
        "image_path": "outfit_images/outfit_30.jpg", # Local path
        "suitable_weather_temps_min": 10,
        "suitable_weather_temps_max": 25,
        "suitable_weather_keywords": ["mild", "clear", "cloudy"],
        "suitable_body_types": ["Rectangle", "Hourglass", "Pear", "Inverted Triangle", "Oval"], # "All" body types for a classic suit
        "suitable_occasions": ["Work", "Business Meeting"],
        "style_keywords": ["classic", "professional", "elegant"],
        "description": "A well-fitted suit with a crisp shirt and polished shoes. Timeless and professional.",
        "justification_template": "This **{style}** outfit is a timeless choice for your **{body_type}** shape, ideal for **{weather_desc}** conditions and a **{occasion}**."
    },
]

# These are the lists of options that the user will choose from in the website dropdown menus.
# Make sure these lists match the values used in your 'suitable_body_types', 'suitable_occasions', 'style_keywords' above!
BODY_TYPES = ["Rectangle", "Pear", "Hourglass", "Inverted Triangle", "Oval"]
OCCASIONS = ["Casual", "Work", "Formal", "Party", "Outdoor", "Sports", "Everyday", "Beach", "Evening", "Festival"]
STYLES = ["Minimalist", "Boho", "Classic", "Trendy", "Elegant", "Comfortable", "Professional", "Light", "Warm", "Layered", "Practical", "Chic", "Glamorous", "Sporty", "Active", "Relaxed", "Edgy"]

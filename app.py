import streamlit as st
from datetime import datetime, timedelta
import time

# Define the elements and their string theory mappings with emojis, including lengthy explanations
elements = {
    0: {
        "name": "Fire (Type I)", 
        "emoji": "🔥", 
        "qualities": "Heat, transformation, dynamism",
        "explanation": """
🔥 **Fire Element in Panchabhuta and Type I String Theory** 🔥  
In ancient Vedic philosophy, Fire (Tejas or Agni) represents heat, light, transformation, energy, and dynamism. It's the spark of change, the force that consumes and renews, like a blazing inferno turning wood to ash, symbolizing evolution and power! 💥  
In string theory, Type I corresponds to this fiery essence with its open and closed unoriented strings, allowing dynamic interactions through joining and splitting – just like fire's transformative flames! It includes the SO(32) gauge group for balanced forces amid chaos, anomaly cancellations ensuring stability in the heat of creation. Imagine strings vibrating wildly, producing the five fundamental interactions, echoing fire's role in cosmic alchemy. 🌟🔥🌀
"""
    },
    1: {
        "name": "Water (Type IIA)", 
        "emoji": "💧", 
        "qualities": "Fluidity, cohesion, adaptability",
        "explanation": """
💧 **Water Element in Panchabhuta and Type IIA String Theory** 💧  
Water (Apas or Jala) embodies fluidity, cohesion, adaptability, flow, and cooling in Vedic lore – the life-giving essence that shapes rivers, oceans, and rain, binding things together while adapting to any form! 🌊  
Type IIA string theory mirrors this with closed oriented strings, a non-chiral spectrum, and even-dimensional D-branes, dual to M-theory on a circle for smooth, winding transitions. It's like water's gentle flow across dimensions, cohesive and adaptable without breaks, enabling evolutionary changes in the cosmic sea! 🌀💦🌌
"""
    },
    2: {
        "name": "Air (Type IIB)", 
        "emoji": "🌬️", 
        "qualities": "Mobility, lightness, expansion",
        "explanation": """
🌬️ **Air Element in Panchabhuta and Type IIB String Theory** 🌬️  
Air (Vayu) signifies mobility, lightness, expansion, subtlety, and touch – the invisible force of wind that carries scents, sounds, and life, ever-expanding and free! ☁️  
In Type IIB, closed oriented strings are chiral and self-dual under S-duality, with odd-dimensional D-branes supporting infinite dualities and mirror symmetries. This evokes air's expansive nature, reflecting 'winds' of possibility, subtle yet pervasive, like breath animating the universe! 🌀🌪️✨
"""
    },
    3: {
        "name": "Earth (Heterotic SO(32))", 
        "emoji": "🌍", 
        "qualities": "Stability, solidity, grounding",
        "explanation": """
🌍 **Earth Element in Panchabhuta and Heterotic SO(32) String Theory** 🌍  
Earth (Prithvi) stands for stability, solidity, density, grounding, and support – the firm foundation of mountains and soil, providing structure and endurance to all life! 🏔️  
Heterotic SO(32) features closed strings with asymmetric movers, hybrid bosonic-superstring traits, and the SO(32) gauge group for consistent grounding. It's the solid base combining 26D and 10D aspects, supporting particle phenomena without collapse, like earth's unyielding core! ⚖️🌿🔒
"""
    },
    4: {
        "name": "Ether (Heterotic E8×E8)", 
        "emoji": "✨", 
        "qualities": "Space, subtlety, connectivity",
        "explanation": """
✨ **Ether Element in Panchabhuta and Heterotic E8×E8 String Theory** ✨  
Ether (Akasha) is space, void, subtlety, all-pervasiveness, and connectivity – the unseen medium that holds everything, carrying vibrations and unifying the cosmos! 🌌  
Heterotic E8×E8 uses closed strings with exceptional gauge groups, modeling hidden sectors and compactifications, unifying in M-theory. It pervades hidden dimensions like ether's subtle void, connecting elements in an all-encompassing unity! 🕳️🔗🌠
"""
    }
}

# Function to map datetime to element index (pseudo-scientific vibration calc)
def get_element_index(birth_dt):
    # Sum components for 'vibration'
    vibration = birth_dt.year + birth_dt.month + birth_dt.day + birth_dt.hour + birth_dt.minute + birth_dt.second
    # Modulo 5 for 5 elements
    return vibration % 5

# Streamlit app
st.title("💥 Big Bang Elemental Convergence: Your Personal String Element! 🌌")

st.markdown("""
Welcome to this fun app for discovering your personal element based on your birthday! 🎉  
Inspired by string theory and ancient Panchabhuta elements, enter your birth date and exact time (down to seconds).  
We'll map your birth moment to a vibrating string and element, revealing your inherent qualities and a detailed explanation! 🚀  
Imagine the Big Bang as the singularity where all elements converged, birthing your unique essence.  
""")

# Define calendar range from 1900 to 2100
min_birth_date = datetime(1900, 1, 1)
max_birth_date = datetime(2100, 12, 31)

# Single input for birthday with combined date and time
st.header("Your Birthday 🎂")
col_date, col_time = st.columns(2)
with col_date:
    date = st.date_input("Birth Date", value=datetime(1993, 7, 12), min_value=min_birth_date, max_value=max_birth_date)
with col_time:
    time_input = st.time_input("Birth Time", value=datetime(1993, 7, 12, 12, 26, 0).time(), step=timedelta(minutes=1))
sec = st.slider("Birth Second", 0, 59, 0)
birth = datetime(date.year, date.month, date.day, time_input.hour, time_input.minute, sec)

if st.button("Reveal Your Element! 🔮"):
    # Get element
    idx = get_element_index(birth)
    elem = elements[idx]
    
    st.header("Your Elemental Mapping 🌟")
    st.markdown(f"**Your Element:** {elem['name']} {elem['emoji']} - {elem['qualities']}")
    
    # Add lengthy explanation
    st.header("Detailed Explanation of Your Element and String 📚")
    st.markdown(elem['explanation'])
    
    # Fun animation
    with st.spinner("Vibrating strings in higher dimensions..."):
        time.sleep(1)
    st.balloons()

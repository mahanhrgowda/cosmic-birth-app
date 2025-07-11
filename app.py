import streamlit as st
from datetime import datetime
import numpy as np
import pytz

# Title with emoji
st.title("Cosmic Birth Explorer 🌟🔮")

# Fun intro
st.write("Enter your name, birth details, and let's uncover the mystical energies of your birth! 🎉 Using the triple helix model, block universe theory, and the mantra 'Om Śrīṁ Bhūṁ Nīlāṁ Agni-Nābhiṁ Prabodhaya Svāhā', we'll map your birth to divine strings in spacetime! ✨")

# Input Section
name = st.text_input("Your Name", value="Explorer")
date = st.date_input("Birth Date", value=datetime(1993, 7, 12).date())
time = st.time_input("Birth Time", value=datetime.strptime("12:26 PM", "%I:%M %p").time())
tz = st.selectbox("Time Zone", pytz.all_timezones, index=pytz.all_timezones.index("Asia/Kolkata"))

if st.button("Explore My Cosmos! 🚀"):
    # Fun effects
    st.balloons()

    # Convert to UTC
    tz_obj = pytz.timezone(tz)
    dt = datetime.combine(date, time).replace(tzinfo=tz_obj)
    dt_utc = dt.astimezone(pytz.UTC)
    st.write(f"Hello, {name}! Your birth in UTC: {dt_utc.strftime('%Y-%m-%d %H:%M:%S')} ⏰")

    # Calculate Z-value (simplified for fun)
    ref_date = datetime(1900, 1, 1, 0, 0, 0, tzinfo=pytz.UTC)
    seconds = (dt_utc - ref_date).total_seconds()
    z_value = seconds / (7.44 * 365.25 * 24 * 3600)  # Scaled from years
    st.write(f"Your Cosmic Z-Value: {z_value:.2f} 🌌")

    # Dominant Energy (Shri, Bhu, Nila) with emoji
    phase = np.sin(0.5 * z_value)
    if phase > 0.33:
        energy = "Śrī (Prosperity) 💰✨ - You're a wealth magnet!"
    elif phase > -0.33:
        energy = "Bhū (Material Grounding) 🌍🏔️ - You're rooted like the Earth!"
    else:
        energy = "Nīlā (Compassion) ❤️🙏 - Your heart unites the world!"
    st.write(f"Dominant Divine Energy: {energy}")

    # Map to String Theory Types with fun descriptions
    if phase > 0.33:
        string_type = "Open String - Dynamic and interactive, like a cosmic party starter! 🎉"
    elif phase > -0.33:
        string_type = "Closed String - Stable and gravitational, holding everything together! ⚓"
    else:
        string_type = "Heterotic String - Unifying and hybrid, the bridge between worlds! 🌉"
    st.write(f"Your String Type in String Theory: {string_type}")

    # Mantra Interpretation with linkage
    st.subheader("Your Mantra Magic 🔮")
    st.write("The mantra 'Om Śrīṁ Bhūṁ Nīlāṁ Agni-Nābhiṁ Prabodhaya Svāhā' awakens fiery energy at the cosmic center! 🌋")
    st.write("Link to Three Basic Strings: Śrīṁ (Open String - Prosperity), Bhūṁ (Closed String - Grounding), Nīlāṁ (Heterotic String - Compassion). Your birth resonates with this divine wave! 🌊")

    # Convergence Point Fun Fact
    convergence_year = 1900 + z_value * 7.44
    st.write(f"Your Birth Convergence Year: {int(convergence_year)} CE - A cosmic alignment point! ⭐")

    # Fun Visualization (simple plot)
    st.subheader("Your Spacetime Wave 📈")
    fig, ax = plt.subplots()
    x = np.linspace(0, 10, 100)
    y = np.sin(x + phase)  # Wave based on phase
    ax.plot(x, y, color='blue')
    ax.set_title("Your Personal Spacetime Wave 🌊")
    ax.set_xlabel("Cosmic Flow")
    ax.set_ylabel("Time Strand")
    st.pyplot(fig)

    # More fun effects
    st.success("Mind and heart titillated? Share your cosmic story! 😊")
    st.confetti()  # Assuming Streamlit supports or simulate with text
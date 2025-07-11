import streamlit as st
from datetime import datetime
from astropy.time import Time
from astropy.coordinates import get_sun, solar_system_ephemeris

st.title("Cosmic String Guna Oracle")
st.markdown("""
Discover your personal link between String Theory and the ancient Gunas based on your birth date and time! 
This fun app uses real astronomical data to determine your 'cosmic vibration' rooted in science.
""")

birth_date = st.date_input("Enter your birth date")
birth_time = st.time_input("Enter your birth time (UTC)")

if st.button("Reveal Your Cosmic String!"):
    if birth_date and birth_time:
        birth_datetime = datetime.combine(birth_date, birth_time)
        astro_time = Time(birth_datetime.isoformat())
        
        with solar_system_ephemeris.set('builtin'):
            sun = get_sun(astro_time)
        
        ra_deg = sun.ra.deg
        sector = int((ra_deg % 360) // 120)
        
        mappings = [
            {
                "theory": "Type II",
                "guna": "Sattva",
                "qualities": "purity, harmony, knowledge, balance",
                "description": "Type II theories feature closed, oriented strings with full supersymmetry, providing a balanced, symmetric framework that unifies forces in a harmonious 10-dimensional spacetime. This mirrors sattva's illuminating, equilibrating quality."
            },
            {
                "theory": "Type I",
                "guna": "Rajas",
                "qualities": "passion, activity, energy, change",
                "description": "Type I incorporates both open and closed unoriented strings, enabling dynamic interactions via endpoints that attach to branes, mediating gauge forces. This active nature aligns with rajas' energetic, motion-driven quality."
            },
            {
                "theory": "Heterotic",
                "guna": "Tamas",
                "qualities": "inertia, dullness, ignorance, stability",
                "description": "Heterotic theories use closed strings with asymmetric modes—one side bosonic, the other supersymmetric—creating a rigid, inertial structure. This reflects tamas' quality of inertia and delusion, providing foundational stability."
            }
        ]
        
        your_mapping = mappings[sector]
        
        st.success(f"Based on the Sun's position at your birth (RA: {ra_deg:.2f}°), your cosmic sector is {sector}!")
        st.markdown(f"### Your String Theory Type: **{your_mapping['theory']}**")
        st.markdown(f"### Linked Guna: **{your_mapping['guna']}**")
        st.markdown(f"**Qualities:** {your_mapping['qualities']}")
        st.markdown(f"**Scientific-Philosophical Insight:** {your_mapping['description']}")
        
        st.markdown("""
        #### Full Analogy Table for Reference
        | String Theory Family | Linked Guna | Qualities | Analogical Link |
        |----------------------|-------------|-----------|-----------------|
        | **Type II** | **Sattva** | purity, harmony, knowledge | Balanced, symmetric framework mirroring sattva's clarity. |
        | **Type I** | **Rajas** | passion, activity, energy | Dynamic interactions aligning with rajas' energy. |
        | **Heterotic** | **Tamas** | inertia, dullness, stability | Rigid structure reflecting tamas' inertia. |
        """)
        
        st.info("Fun Twist: Just like strings vibrate to create the universe, your birth moment vibrates with these qualities! Share your results. 🚀🧘‍♂️")
    else:
        st.warning("Please enter both date and time.")

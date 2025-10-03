import streamlit as st
from openai import OpenAI

# 🌿 Page setup
st.set_page_config(page_title="ManaShuddhi", layout="centered")

st.title("🌤️ ManaShuddhi")
st.subheader("A soulful space to return to your higher self")

st.markdown("""
Welcome, radiant soul. 🌸  
Take a moment.  
Breathe.  
Allow yourself to soften into presence.  
""")

# 🌱 Reflection form
with st.form("soulful_reflection_form"):
    mood = st.text_input("💖 How are you feeling in this moment?")
    intention = st.text_input("🎯 What would you like to invite into your life today?")
    noise = st.text_area("🌪️ What's clouding your mind or pulling your energy?")
    submitted = st.form_submit_button("✨ Reflect with ManaShuddhi")

# ✨ Generate soulful reflection
if submitted:
    if not (mood.strip() and intention.strip() and noise.strip()):
        st.warning("Please fill in all the fields to receive your reflection.")
    else:
        with st.spinner("🌬️ Channeling peace and clarity..."):
            # Prepare prompt
            prompt = f"""
You are a gentle, poetic mindfulness coach and soul guide.

Create a short, soulful reflection based on the following:
- Mood: {mood}
- Intention: {intention}
- Mental Noise: {noise}

Include and beautifully weave in these healing elements:
- Sky gazing therapy (lightness, expansion, freedom)
- Embracing nature (trees, breeze, sunlight, water)
- No-mind therapy (stillness, presence, awareness)
- Shell therapy (gentle safety, protection, sacred space)
- Being surrounded by an aura of love and serenity
- Breathing awareness (“vibe with your breath”)
- Aura cleansing (release of energy blocks)
- Awakening to pure consciousness
- Soothe the vagus nerve (rest-digest state, calming tone)
- Mindfulness, gratitude, inner smile, and silence
"""

            # New OpenAI API client
            client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[
                    {"role": "system", "content": "You are a gentle soul coach and poetic mindfulness guide."},
                    {"role": "user", "content": prompt},
                ],
                temperature=0.8,
            )

            # Get the generated text
            output = response.choices[0].message.content
            st.success("🌈 Your Reflection from ManaShuddhi:")
            st.markdown(output)

# Optional soothing background
st.markdown("---")
st.markdown("🎵 **Optional: Soothing Background Sound**")
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", format="audio/mp3")

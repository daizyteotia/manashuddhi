import streamlit as st
import openai

# Load OpenAI API key from Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

# 🌿 Page setup
st.set_page_config(page_title="ManaShuddhii", layout="centered")

st.title("🌤️ ManaShuddhii")
st.subheader("a soulful space to return to your higher self")

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
    submitted = st.form_submit_button("✨ Reflect with ManaShuddhii")

# ✨ Generate soulful reflection
if submitted:
    if not (mood.strip() and intention.strip() and noise.strip()):
        st.warning("Please fill in all the fields to receive your reflection.")
    else:
        with st.spinner("🌬️ Channeling peace and clarity..."):
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

Use poetic, soft, uplifting language. Speak like a spiritual guide or gentle energy healer. Use line breaks for rhythm. Create a sense of beauty, peace, and soul restoration.
"""

            response = openai.ChatCompletion.create(
                model="gpt-4-0613",
                messages=[
                    {"role": "system", "content": "You are a gentle soul coach and poetic mindfulness guide."},
                    {"role": "user", "content": prompt},
                ],
                temperature=0.8,
            )
            output = response["choices"][0]["message"]["content"]

            st.success("🌈 Your Reflection from ManaShuddhii:")
            st.markdown(output)

st.markdown("---")

st.markdown("🎵 **Optional: Soothing Background Sound**")
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", format="audio/mp3")

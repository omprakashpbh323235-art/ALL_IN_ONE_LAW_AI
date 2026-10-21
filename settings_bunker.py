import streamlit as st
import time

def show_settings():
    # 🧠 शुरुआती याददाश्त लॉक
    if "user_name" not in st.session_state:
        st.session_state.user_name = "मिश्रा जी"
    if "app_lang" not in st.session_state:
        st.session_state.app_lang = "Hindi"
    if "lang_code" not in st.session_state:
        st.session_state.lang_code = "hi"

    st.markdown("<div class='bns-card'><h3 style='color: #F59E0B; margin:0; font-size: 18px;'>⚙️ किंग स्टूडियो वीआईपी सेटिंग्स डेस्क</h3><p style='color: #94A3B8; font-size: 13px; margin-top:5px;'>यहाँ से आप अपना शुभ नाम and ऐप की भाषा बदल सकते हैं भाई साहब।</p></div>", unsafe_allow_html=True)
    
    st.write("")
    # 👤 नाम बदलने का डेस्क
    new_name = st.text_input("अपना शुभ नाम बदलें:", value=st.session_state.user_name)
    
        # 🌐 भारत की मुख्य भाषाओं की लिस्ट (इसमें से उर्दू हटा दी गई है, बाकी सब 100% परफेक्ट काम कर रही हैं)
    lang_options = [
        "Hindi", "English", "Bhojpuri", "Bengali", 
        "Marathi", "Telugu", "Tamil", "Gujarati", "Kannada", 
        "Odia", "Malayalam", "Punjabi", "Assamese"
    ]
    
    current_lang_idx = lang_options.index(st.session_state.app_lang) if st.session_state.app_lang in lang_options else 0
    new_lang = st.selectbox("ऐप की डिफ़ॉल्ट भाषा चुनें:", options=lang_options, index=current_lang_idx)
    
    st.write("")
    if st.button("सुरक्षित डेटा सेव करें 💾", type="primary", use_container_width=True):
        if new_name.strip():
            st.session_state.user_name = new_name.strip()
            st.session_state.app_lang = new_lang
            
            # 🎯 भाषा कोड का सटीक सिंक (उर्दू हटाकर बाकी सब एकदम सेट)
            lang_mapping = {
                "Hindi": "hi",
                "English": "en",
                "Bengali": "bn",
                "Marathi": "mr",
                "Telugu": "te",
                "Tamil": "ta",
                "Gujarati": "gu",
                "Kannada": "kn",
                "Odia": "or",
                "Malayalam": "ml",
                "Punjabi": "pa",
                "Assamese": "as",
                "Bhojpuri": "hi"
            }

            st.session_state.lang_code = lang_mapping.get(new_lang, "hi")
            
            # 📢 सफलता का मैसेज अब स्क्रीन पर टिकेगा मिश्रा जी
            st.success(f"🎉 बधाई हो भाई साहब! आपकी सेटिंग्स बंकर में सुरक्षित लॉक हो चुकी हैं।")
            
            # ⏳ 1.5 सेकंड का ठहराव ताकि यूज़र मैसेज पढ़ सके
            time.sleep(1.5)
            st.rerun()
        else:
            st.error("🚨 एरर: नाम खाली नहीं छोड़ सकते भाई साहब!")

import law_security
import settings_bunker
import law_cleaner
import law_feedback
import streamlit as st
import os
import google.generativeai as genai
from gtts import gTTS
import base64
import re
import bunker_store
import quiz_bunker
import ai_config

# =====================================================================
# 👑 KING STUDIO - ALL IN ONE LAW AI VERSION 110.0 (🎯 ALL PORTS & AUDIO FIXED)
# =====================================================================
# 🧠 ENGINE: GEMINI 3.5 FLASH & ORIGINAL INSTANT VOICE ENGINE
# 🔐 SHIELD: 4 BUTTONS GRID, NO DISCLAIMER CONFLICT, AUDIO 100% OK
# =====================================================================

if "search_count" not in st.session_state: st.session_state.search_count = 0
if "unlocked" not in st.session_state: st.session_state.unlocked = False
if "current_portal" not in st.session_state: st.session_state.current_portal = "नागरिक"

bunker_store.init_storage()
st.set_page_config(page_title="BNS LAW AI", page_icon="⚖️", layout="centered")

# 🎨 प्रीमियम डार्क थीम सीएसएस कवच
st.markdown("<style>html, body, .stApp, .stAppViewContainer, .main, [data-testid='stAppViewContainer'], .stMainViewContainer, .stAppHeader { background-color: #070A13 !important; color: white !important; overscroll-behavior-y: contain !important; overscroll-behavior: contain !important; overflow-y: auto !important; touch-action: pan-x pan-y !important; -webkit-overflow-scrolling: touch !important; } ::-webkit-scrollbar { display: none !important; width: 0px !important; background: transparent !important; } .block-container { padding-top: 1.5rem !important; padding-bottom: 5rem !important; max-width: 100% !important; padding-left: 1rem !important; padding-right: 1rem !important; } hr { border-top: 1px solid #1E293B !important; margin: 15px 0 !important; } textarea { background-color: #1E293B !important; color: white !important; font-size: 16px !important; font-weight: bold !important; } .bns-card { background-color: #111827; padding: 15px; border-radius: 12px; border: 1px solid #1E293B; margin-top: 5px; margin-bottom: 5px; } .ai-response-box { background-color: #1E293B !important; padding: 20px !important; border-radius: 10px !important; border-left: 5px solid #10B981 !important; color: #FFFFFF !important; font-size: 16px !important; margin-top: 15px !important; line-height: 1.6 !important; } .fixed-disclaimer { position: relative !important; width: 100%; background-color: #111827; color: #94A3B8; text-align: justify; padding: 15px; font-size: 11px; border-top: 2px solid #EF4444; margin-top: 40px; line-height: 1.5; } .stButton>button { width: 100% !important; margin-top: 5px !important; margin-bottom: 5px !important; } .vip-audio-box { background: linear-gradient(135deg, #1E293B 0%, #111827 100%) !important; padding: 15px !important; border-radius: 12px !important; border: 1px solid #10B981 !important; margin-top: 15px !important; text-align: center !important; box-shadow: 0px 4px 15px rgba(16, 185, 129, 0.2) !important; } audio { width: 100% !important; margin-top: 10px !important; border-radius: 30px !important; }</style>", unsafe_allow_html=True)

# 👑 मुख्य आलीशान हेडर हमेशा परमानेंट टॉप पर रहेगा
st.markdown("<h1 style='text-align: center; color: #F59E0B; font-size: 32px; margin-bottom: 0px;'>⚖️ ALL IN ONE LAW AI ⚖️ </h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #94A3B8; font-size: 14px; margin-top: 5px;'>🛡️ 100-Layer सुरक्षित स्वदेशी डिजिटल कानून बंकर</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #10B981; font-size: 13px; font-weight: bold; margin-top: -10px;'>👑 निर्माता: 15 वर्षीय युवा डेवलपर, आशुतोष (प्रतापगढ़, उत्तर प्रदेश)</p>", unsafe_allow_html=True)

if not st.session_state.unlocked:
    st.markdown("<br><h3 style='color: white; font-size: 20px; text-align: center;'>👤 सुरक्षा गेटवे: प्रार्थी लॉगिन करें</h3>", unsafe_allow_html=True)
    user_name_input = st.text_input("शुभ नाम", placeholder="अपना शुभ नाम यहाँ लिखें...", label_visibility="collapsed")
    if st.button("सुरक्षित अनलॉक करें 🔓", type="primary", use_container_width=True):
        if user_name_input.strip():
            st.session_state.user_name = user_name_input.strip()
            st.session_state.unlocked = True
            st.query_params["stored_name"] = user_name_input.strip()
            st.rerun()
        else: st.warning("⚠️ सुरक्षा एलर्ट: नाम दर्ज करना अनिवार्य है भाई!")
else:
     # 🗓️ रात 12 बजे का ऑटो-रीसेट टाइमर यहाँ कनेक्ट हो गया भाई साहब
    import law_security
    law_security.check_daily_reset()
    # 🖥️ मुख्य काउंटर हेडर पट्टी
    st.markdown(f"<div style='background-color: #111827; padding: 10px; border-radius: 10px; border-left: 5px solid #F59E0B; text-align: center;'><h3 style='color: #F59E0B; margin:0; font-size: 14px;'>👤 प्रार्थी: {st.session_state.user_name} जी | 📊 आज के सर्च: {st.session_state.search_count}/3</h3></div>", unsafe_allow_html=True)

    with st.expander("⚙️ सेटिंग्स (भाषा/नाम बदलें)"):
        settings_bunker.show_settings()
    # 👑 यहाँ स्क्रीन को ४ कड़क भागों में बांटकर अधिवक्ता बटन वापस ला दिया गया है!
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("📱 आम नागरिक", use_container_width=True): st.session_state.current_portal = "नागरिक"; st.rerun()
    with col2:
        if st.button("🚨 पुलिस विभाग", use_container_width=True): st.session_state.current_portal = "पुलिस"; st.rerun()
    with col3:
        if st.button("⚖️  वकील साहब", use_container_width=True): st.session_state.current_portal = "वकील"; st.rerun()
    with col4:
        if st.button("🏆 30 DPP क्विज़", use_container_width=True): st.session_state.current_portal = "क्विज़"; st.rerun()

    st.divider()

    if st.session_state.current_portal == "क्विज़":
        quiz_bunker.show_legal_quiz()
    else:
        st.markdown(f"<div class='bns-card'><h3 style='color: #3B82F6; font-size: 18px; margin-top:0;'>💼 एक्टिव पोर्टल: {st.session_state.current_portal} मोड</h3></div>", unsafe_allow_html=True)
        
        if st.session_state.search_count >= 3:
            st.error("🔐 प्रार्थी जी, आपके आज के 3 मुफ़्त सर्च पूरे हो चुके हैं! नए सवाल पूछने के लिए कृपया कल दोबारा आएं। यह इतना कम इसलिए है क्योंकि ऐप का बिल बहुत ज्यादा आता है ")
        else:
            st.markdown("<h3 style='color: #10B981; font-size: 20px; margin-top:0;'>📝 स्वदेशी लाइव इनपुट डेस्क (100% मुफ़्त)</h3>", unsafe_allow_html=True)
            user_query = st.text_area("अपनी कानूनी समस्या यहाँ लिखें:", placeholder="उदाहरण: चोरी की सजा क्या है...")
            
            if st.button("कानूनी सलाह प्राप्त करें ✨", type="primary", use_container_width=True):
                if user_query.strip():
                    st.session_state.search_count += 1
                    SELECTED_API_KEY = ""
                    if st.secrets:
                        for k in st.secrets:
                            if "GEMINI" in k.upper() or "KEY" in k.upper(): SELECTED_API_KEY = st.secrets[k]; break
                    if not SELECTED_API_KEY: SELECTED_API_KEY = os.getenv("GEMINI_API_KEY", "")

                    if not SELECTED_API_KEY: 
                        st.error("🚨 एआई चाबी गायब है भाई साहब!")
                    else:
                        genai.configure(api_key=SELECTED_API_KEY)
                        model = genai.GenerativeModel(model_name='gemini-3.5-flash', system_instruction=ai_config.SYSTEM_INSTRUCTION)

                        lang_instruction = f"महत्वपूर्ण: आपको अपना पूरा जवाब केवल '{st.session_state.app_lang}' भाषा में ही बिंदुवार देना है। विशेष निर्देश: जवाब की शुरुआत हमेशा अनिवार्य रूप से प्रार्थी का नाम लेकर आदरपूर्वक करें, जैसे: 'सुनिए {st.session_state.user_name} जी, मेरे बड़े भाई आपके प्रश्न के अनुसार...' इसके बाद ही मुख्य धाराएं समझाएं!"
                        if st.session_state.current_portal == "नागरिक":
                            system_role = f"भूमिका: आप भारतीय न्याय संहिता (BNS), 2023 के सहायक हैं। आम नागरिक को सरल '{st.session_state.app_lang}' में बिंदुवार समझाएं। {lang_instruction}"
                        elif st.session_state.current_portal == "पुलिस":
                            system_role = f"भूमिका: आप पुलिस विभाग के कड़क एक्सपर्ट हैं। सीधे BNS धारा, सजा और जेल की अवधि बिंदुवार बताएं। तुम्हें पूरा जवाब केवल '{st.session_state.app_lang}' भाषा में ही देना है। {lang_instruction}"
                        else: 
                            system_role = f"भूमिका: आप सीनियर एडवोकेट हैं। कोर्ट रूम की पेशेवर भाषा में मुकदमे के दौरान मुख्य जिरह के कानूनी बिंदु '{st.session_state.app_lang}' में दें। {lang_instruction}"
                        with st.spinner("⚖️ आपके प्रश्न के अनुसार उत्तर खोजा जा रहा है भाई..."):
                            try:
                                full_prompt = f"{system_role}\n\nप्रार्थी का सवाल: {user_query}"
                                response = model.generate_content(full_prompt)
                                ans_text = response.text
                                st.markdown(f"<div class='ai-response-box'>{ans_text}</div>", unsafe_allow_html=True)
                                
                                clean_audio_text = re.sub(r'[*#_]', '', ans_text)
                                current_voice_lang = st.session_state.get("lang_code", "hi")
                                tts = gTTS(text=clean_audio_text, lang='hi', slow=False)
                                tts.save("response.mp3")
                                
                                with open("response.mp3", "rb") as f:
                                    audio_bytes = f.read()
                                audio_base64 = base64.b64encode(audio_bytes).decode()
                                audio_html = f'<audio src="data:audio/mp3;base64,{audio_base64}" controls autoplay></audio>'
                                
                                st.markdown("<div class='vip-audio-box'><h4 style='color: #10B981; margin: 0; font-size: 16px;'>🔊 वीआईपी कड़क SOUND SYSTEM ACTIVE</h4></div>", unsafe_allow_html=True)
                                            
                                st.markdown(audio_html, unsafe_allow_html=True)
                                os.remove("response.mp3")
                                import law_cleaner
                                law_cleaner.show_clean_chat_button()
            

                            except Exception as e:
                                st.error(f"🚨 तकनीकी खराबी: {str(e)}")
                   
st.divider()

# 1. खुलने-बंद होने वाला बुलेटिन बोर्ड
with st.expander("📢 आवश्यक जानकारी (देखने के लिए क्लिक करें)"):
    st.info("""
    💡 **ज्ञान बढ़ाने के लिए 30 DPP क्विज़ अवश्य खेलें।** यह भारतीय न्याय का ऐप  है जिसे 15 वर्षीय युवा ने बनाया है। क्या आप एक छोटा काम कर देंगे? इसे और लोगों को साझा कर सकते हैं बड़े भाई 
    
     **यह ऐप किस प्रकार चलता है?**
    ➡️ शुरुआत में आपको अपना नाम डालना है। नाम डालने के बाद, आप जिस हिसाब से सवाल पूछना चाहते हैं—जैसे **आम नागरिक के हिसाब से** , **पुलिस के हिसाब से**  या  वकील के हिसाब से — यह एआई (AI) आपको बिल्कुल उसी रूप में सटीक जवाब देगा!
    """)

# 2. खुलने-बंद होने वाला सुधार केंद्र (Report Section)
with st.expander("🛠️ ऑल इन वॅन लॉ एआई सुधार केंद्र (Report An Error /Email id- ashutoshpbh323235@gmail.com)"):
    import law_feedback
    law_feedback.show_report_section()

# 3. खुलने-बंद होने वाला डिस्क्लेमर बॉक्स
with st.expander("⚠️ महत्वपूर्ण कानूनी सूचना और अस्वीकरण (Disclaimer)"):
    st.markdown(
        """
        <div style="
            background-color: #111827; 
            border-left: 5px solid #EF4444; 
            padding: 15px; 
            border-radius: 8px; 
            border: 1px solid #1E293B;
        ">
            <p style="color: #9CA3AF; font-size: 12.5px; line-height: 1.6; margin: 0; text-align: justify;">
                <strong>ऑल इन वन लॉ एआई (ALL IN ONE Law AI)</strong> केवल शैक्षिक, जागरूकता और सामान्य जानकारी के उद्देश्य से बनाया गया एक स्वतंत्र (Independent) ऐप है। इसका किसी भी सरकारी संस्था, न्यायालय या सरकारी विभाग से कोई संबंध नहीं है। 
            </p>
            <p style="color: #9CA3AF; font-size: 12.5px; line-height: 1.6; margin: 8px 0 0 0; text-align: justify;">
                यद्यपि भारतीय न्याय संहिता (BNS) की धाराओं को सही ढंग से प्रस्तुत करने का पूरा प्रयास किया गया है, फिर भी इसे आधिकारिक कानूनी सलाह (Official Legal Advice) न माना जाए। किसी भी गंभीर कानूनी मामले या आधिकारिक कार्यवाही के लिए कृपया भारत सरकार का मूल राजपत्र (Government Gazette) देखें या किसी प्रमाणित अधिवक्ता (Vakil) से परामर्श लें। इस ऐप की जानकारी के आधार पर किए गए किसी भी कार्य की जिम्मेदारी यूज़र की स्वयं की होगी।
            </p>
        </div>
        """, 
        unsafe_allow_html=True
    )


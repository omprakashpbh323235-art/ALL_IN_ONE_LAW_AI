import streamlit as st

def show_clean_chat_button():
    """यह फंक्शन स्क्रीन पर एक साफ सुथरा 'क्लीन चैट' बटन दिखाएगा और क्लिक करने पर सब खाली कर देगा"""
    
    # लाल रंग का कड़क बटन जो पूरी चौड़ाई कवर करेगा
    if st.button("🧹 चैट पूरी तरह साफ करें (Clean Chat)", type="secondary", use_container_width=True):
        
        # 🧠 स्ट्रीमलिट की याददाश्त (Memory) में से चैट हिस्ट्री और पुरानी सलाह को डिलीट करना
        keys_to_clear = ["messages", "user_query", "ai_response", "audio_path"]
        
        for key in keys_to_clear:
            if key in st.session_state:
                del st.session_state[key]
        
        # यूज़र को सफलता का संदेश दिखाना और ऐप को रीस्टार्ट (रीफ्रेश) करना
        st.toast("🔄 चैट को पूरी तरह साफ कर दिया गया है भाई साहब!", icon="🧹")
        st.rerun()

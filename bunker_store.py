import streamlit as st

def init_storage():
    # 🧠 सीक्रेट डिजिटल लॉकर: नाम, सर्च काउंट, डायमंड वॉलेट और डेली क्विज़ लॉक भाई साहब
    if "unlocked" not in st.session_state: st.session_state.unlocked = False
    if "user_name" not in st.session_state: st.session_state.user_name = ""
    if "search_count" not in st.session_state: st.session_state.search_count = 0
    if "current_portal" not in st.session_state: st.session_state.current_portal = "नागरिक"
    if "diamonds" not in st.session_state: st.session_state.diamonds = 0.0
    if "quiz_played_today" not in st.session_state: st.session_state.quiz_played_today = False

    qp = st.query_params
    if "stored_name" in qp and not st.session_state.unlocked:
        st.session_state.user_name = qp["stored_name"]
        st.session_state.unlocked = True
    if "stored_diamonds" in qp:
        st.session_state.diamonds = float(qp["stored_diamonds"])

def update_diamonds(amount):
    st.session_state.diamonds = max(0.0, st.session_state.diamonds + amount)
    st.query_params["stored_diamonds"] = str(st.session_state.diamonds)

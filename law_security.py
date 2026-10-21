import streamlit as st
import datetime

def check_daily_reset():
    """यह फंक्शन हर सेकंड चेक करेगा कि रात के 12 बज गए हैं या नहीं, और बजते ही कोटा 0 कर देगा"""
    
    # 🗓️ आज की तारीख को लाइव ट्रैक करना
    current_date = str(datetime.date.today())
    
    # 🧠 अगर तारीख बदल गई है (रात के 12 बज चुके हैं) या यूज़र पहली बार आया है
    if "last_search_date" not in st.session_state or st.session_state.last_search_date != current_date:
        st.session_state.last_search_date = current_date
        st.session_state.search_count = 0  # 🔄 कोटा अपने आप वापस 0 हो गया भाई साहब!

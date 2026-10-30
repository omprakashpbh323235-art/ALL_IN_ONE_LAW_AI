import streamlit as st

def show_report_section():
    st.markdown("<hr style='border-top: 1px dashed #EF4444; margin: 20px 0;'>", unsafe_allow_html=True)
    
    # खूबसूरत रिपोर्ट बॉक्स डिजाइन
    st.markdown(
        """
        <div style="
            background-color: #1E293B; 
            border: 1px solid #374151; 
            padding: 15px; 
            border-radius: 8px; 
            text-align: center;
        ">
            <span style="color: #F59E0B; font-size: 14px; font-weight: bold;">
                🛠️ प्रतापगढ़ लॉ एआई सुधार केंद्र (Report An Error)
            </span>
            <p style="color: #9CA3AF; font-size: 12px; margin: 5px 0 10px 0;">
                यदि आपको एआई द्वारा दी गई किसी धारा या कानूनी जानकारी में कोई त्रुटि/गलती लगती है, तो कृपया हमें तुरंत सूचित करें ताकि हम इसे सुधार सकें।
            </p>
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    # आपका असली ईमेल सेट कर दिया गया है भाई साहब
    email_url = "ashutoshpbh323235@gmail.com"
    
    st.link_button("⚠️ गलत जानकारी की रिपोर्ट करें (Report Error)", email_url, use_container_width=True)

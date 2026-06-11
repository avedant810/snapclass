import streamlit as st


def footer_home():
    logo_url = "https://media.licdn.com/dms/image/v2/D560BAQEj2KVS7uNdKw/company-logo_200_200/B56ZwTamT8JMAI-/0/1769852266237/teamvedant_logo?e=2147483647&v=beta&t=FuN8SSc6mrV2HvT20aX2EhZjttlj-_hDvwzxMnpk_wg"
    
    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center">
        <p style="font-weight:bold; color:white;"> Created with ❤️ by </p>  
        <img src='{logo_url}' style='max-height:25px' />
        </div>
                
                """, unsafe_allow_html=True)


def footer_dashboard():
    logo_url = "https://media.licdn.com/dms/image/v2/D560BAQEj2KVS7uNdKw/company-logo_200_200/B56ZwTamT8JMAI-/0/1769852266237/teamvedant_logo?e=2147483647&v=beta&t=FuN8SSc6mrV2HvT20aX2EhZjttlj-_hDvwzxMnpk_wg"
    
    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center">
        <p style="font-weight:bold; color:black;"> Created with ❤️ by </p>  
        <img src='{logo_url}' style='max-height:25px' />
        </div>
                
                """, unsafe_allow_html=True)
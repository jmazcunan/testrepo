import streamlit as st

st.write("Hola")

st.markdown("""
<a href="intent://arvr.google.com/scene-viewer/1.0?file=https://raw.githubusercontent.com/jmazcunan/testrepo/blob/main/test001.glb#Intent;scheme=https;package=com.google.android.googlequicksearchbox;action=android.intent.action.VIEW;S.browser_fallback_url=https://developers.google.com/ar;end;">Link</a>
""",unsafe_allow_html=False)

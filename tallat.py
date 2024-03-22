import streamlit as st

st.write("TallaT AR")


import streamlit.components.v1 as components


# components.html("""<a href="intent://arvr.google.com/scene-viewer/1.0?file=https://raw.githubusercontent.com/jmazcunan/testrepo/main/test001.glb#Intent;scheme=https;package=com.google.android.googlequicksearchbox;action=android.intent.action.VIEW;S.browser_fallback_url=https://developers.google.com/ar;end;">Link</a>
# """)

# components.html("""<a href="intent://arvr.google.com/scene-viewer/1.0?file=https://raw.githubusercontent.com/jmazcunan/testrepo/main/Silla1.glb#Intent;scheme=https;package=com.google.android.googlequicksearchbox;action=android.intent.action.VIEW;S.browser_fallback_url=https://developers.google.com/ar;end;">Link HQ</a>
# """)

# components.html("""<a href="intent://arvr.google.com/scene-viewer/1.0?file=https://raw.githubusercontent.com/jmazcunan/testrepo/main/clean_chair.glb#Intent;scheme=https;package=com.google.android.googlequicksearchbox;action=android.intent.action.VIEW;S.browser_fallback_url=https://developers.google.com/ar;end;">Link processed</a>
# """)

# components.html("""<a href="intent://arvr.google.com/scene-viewer/1.0?file=https://raw.githubusercontent.com/jmazcunan/testrepo/main/fett_clean2.glb#Intent;scheme=https;package=com.google.android.googlequicksearchbox;action=android.intent.action.VIEW;S.browser_fallback_url=https://developers.google.com/ar;end;">Funko Boba Fett</a>
# """)

# components.html("""<a href="intent://arvr.google.com/scene-viewer/1.0?file=https://raw.githubusercontent.com/jmazcunan/testrepo/main/copa_superliga2.glb#Intent;scheme=https;package=com.google.android.googlequicksearchbox;action=android.intent.action.VIEW;S.browser_fallback_url=https://developers.google.com/ar;end;">Copa SL</a>
# """)





# components.html("""<script type="module" src="https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js"></script>

# <model-viewer camera-controls touch-action="pan-y" autoplay ar ar-modes="webxr scene-viewer" scale="0.2 0.2 0.2" shadow-intensity="1" src="https://raw.githubusercontent.com/jmazcunan/testrepo/main/untitled.glb" alt="An animated 3D model of a robot"></model-viewer>""")

tab1, tab2, tab3 = st.tabs(["Circular", "Cuadrado", "Rectangular"])

with tab1:
  
  components.html("""<script type="module" src="https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js"></script>
<style>
model-viewer {
  width: 350px;
  height: 400px;
}
</style>


<model-viewer src="https://raw.githubusercontent.com/jmazcunan/testrepo/main/pinilla01.glb"
              ios-src="https://raw.githubusercontent.com/jmazcunan/testrepo/main/pinilla01.usdz"
              alt="model viewer"
              ar
              auto-rotate
              camera-controls></model-viewer>""", width=350, height=400)

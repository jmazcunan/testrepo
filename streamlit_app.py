import streamlit as st

st.write("AR viewer")


import streamlit.components.v1 as components


components.html("""<a href="intent://arvr.google.com/scene-viewer/1.0?file=https://raw.githubusercontent.com/jmazcunan/testrepo/main/test001.glb#Intent;scheme=https;package=com.google.android.googlequicksearchbox;action=android.intent.action.VIEW;S.browser_fallback_url=https://developers.google.com/ar;end;">Link</a>
""")

components.html("""<a href="intent://arvr.google.com/scene-viewer/1.0?file=https://raw.githubusercontent.com/jmazcunan/testrepo/main/Silla1.glb#Intent;scheme=https;package=com.google.android.googlequicksearchbox;action=android.intent.action.VIEW;S.browser_fallback_url=https://developers.google.com/ar;end;">Link HQ</a>
""")

components.html("""<a href="intent://arvr.google.com/scene-viewer/1.0?file=https://raw.githubusercontent.com/jmazcunan/testrepo/main/clean_chair.glb#Intent;scheme=https;package=com.google.android.googlequicksearchbox;action=android.intent.action.VIEW;S.browser_fallback_url=https://developers.google.com/ar;end;">Link processed</a>
""")

components.html("""<a href="intent://arvr.google.com/scene-viewer/1.0?file=https://raw.githubusercontent.com/jmazcunan/testrepo/main/fett_clean2.glb#Intent;scheme=https;package=com.google.android.googlequicksearchbox;action=android.intent.action.VIEW;S.browser_fallback_url=https://developers.google.com/ar;end;">Funko Boba Fett</a>
""")

components.html("""<a href="intent://arvr.google.com/scene-viewer/1.0?file=https://raw.githubusercontent.com/jmazcunan/testrepo/main/copa_superliga2.glb#Intent;scheme=https;package=com.google.android.googlequicksearchbox;action=android.intent.action.VIEW;S.browser_fallback_url=https://developers.google.com/ar;end;">Copa SL</a>
""")



components.html("""<script type="module" src="https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js"></script>

<title>Page Title</title>
</head>
<body>

<model-viewer src="https://raw.githubusercontent.com/jmazcunan/testrepo/main/sl_clean_0.2_met.glb"
              ios-src="https://raw.githubusercontent.com/jmazcunan/testrepo/main/sl_clean.usdz"
              alt="A 3D model of an astronaut"
              ar
              auto-rotate
              camera-controls></model-viewer>""")


components.html("""<script type="module" src="https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js"></script>

<model-viewer camera-controls touch-action="pan-y" autoplay ar ar-modes="webxr scene-viewer" scale="0.2 0.2 0.2" shadow-intensity="1" src="https://raw.githubusercontent.com/jmazcunan/testrepo/main/untitled.glb" alt="An animated 3D model of a robot"></model-viewer>"""

#components.html("""<script type="module" src="https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js"></script>
#<model-viewer src="https://raw.githubusercontent.com/jmazcunan/testrepo/main/sl_clean_0.2.glb" ios-src="https://raw.githubusercontent.com/jmazcunan/testrepo/main/sl_clean.usdz" ar ar-modes="scene-viewer webxr quick-look" camera-controls poster="poster.webp" shadow-intensity="1.03" exposure="0.95">
#    <div class="progress-bar hide" slot="progress-bar">
#        <div class="update-bar"></div>
#    </div>
#    <button slot="ar-button" id="ar-button">
#        View in your space
#    </button>
#    <div id="ar-prompt">
#        <img src="https://modelviewer.dev/shared-assets/icons/hand.png">
#    </div>
#</model-viewer>
#""")



#components.html("""<script type="module" src="https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js"></script>

#<model-viewer src="https://modelviewer.dev/shared-assets/models/Astronaut.glb"
#              ios-src="https://modelviewer.dev/shared-assets/models/Astronaut.usdz"
#              alt="A 3D model of an astronaut"
#              ar
#              auto-rotate
#              camera-controls></model-viewer>""")

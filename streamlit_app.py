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

<model-viewer src="https://raw.githubusercontent.com/jmazcunan/testrepo/main/sl_clean_0.2.glb"
              ios-src="https://raw.githubusercontent.com/jmazcunan/testrepo/main/sl_clean.usdz"
              alt="A 3D model of an astronaut"
              ar
              auto-rotate
              camera-controls></model-viewer>""")




scripts_html = """<script type="module"
  src="https://unpkg.com/@google/model-viewer@3.1.1/dist/model-viewer.js">
</script>

<script nomodule
  src="https://unpkg.com/@google/model-viewer@0.3.1/dist/model-viewer-legacy.js">
</script>
"""
ar_html = """<div>
<model-viewer src=”{}” 
              ar
              alt=”{}”>
</model-viewer>
</div>
"""

#https://developers.google.com/ar/develop/webxr/model-viewer?hl=es-419
scripts_html = """<script type="module" src="https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js"></script>"""


ar_html = """<model-viewer src="{}"
              ios-src="https://modelviewer.dev/shared-assets/models/Astronaut.usdz"
              alt="{}"
              ar
              auto-rotate
              camera-controls></model-viewer>"""

components.html(scripts_html)


components.html(ar_html.format("https://raw.githubusercontent.com/jmazcunan/testrepo/main/sl_clean_0.2.glb", "3D model"), width = 600, height = 600)

components.html(ar_html.format("static/sl_clean_0.2.glb", "3D model"), width = 600, height = 600)

st.markdown(ar_html.format("static/sl_clean_0.2.glb", "3D model"), unsafe_allow_html=False)

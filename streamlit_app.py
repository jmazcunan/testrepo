import streamlit as st

st.write("AR viewer")


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



components.html("""<script type="module" src="https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js"></script>
<style>
model-viewer {
  width: 350px;
  height: 400px;
}
</style>


<model-viewer src="https://raw.githubusercontent.com/jmazcunan/testrepo/main/lamina.glb"
              ios-src="https://raw.githubusercontent.com/jmazcunan/testrepo/main/lamina.usdz"
              alt="model viewer"
              ar ar-placement="wall" 
              auto-rotate
              camera-controls></model-viewer>""", width=350, height=400)


# components.html("""<script type="module" src="https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js"></script>

# <model-viewer camera-controls touch-action="pan-y" autoplay ar ar-modes="webxr scene-viewer" scale="0.2 0.2 0.2" shadow-intensity="1" src="https://raw.githubusercontent.com/jmazcunan/testrepo/main/untitled.glb" alt="An animated 3D model of a robot"></model-viewer>""")

tab1, tab2, tab3 = st.tabs(["Caballo", "Annotations", "Animation"])

with tab1:
  
  
  components.html("""<script type="module" src="https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js"></script>
  <model-viewer id="animation-demo" autoplay ar ar-modes="webxr" scale="0.01 0.01 0.01" camera-orbit="90deg auto auto" shadow-intensity="1" camera-controls touch-action="pan-y" src="https://modelviewer.dev/shared-assets/models/Horse.glb" alt="A 3D model of a horse galloping.">
    <div slot="hotspot-nose" class="anchor" data-surface="0 0 228 113 111 0.217 0.341 0.442"></div>
    <div slot="hotspot-hoof" class="anchor" data-surface="0 0 752 733 735 0.132 0.379 0.489"></div>
    <div slot="hotspot-tail" class="anchor" data-surface="0 0 220 221 222 0.405 0.061 0.534"></div>
    <svg id="lines" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="lineContainer">
      <line class="line"></line>
      <line class="line"></line>
      <line class="line"></line>
    </svg>
  
    <div id="container">
      <button id="nose" class="label">Nose</button>
      <button id="hoof" class="label">Hoof</button>
      <button id="tail" class="label">Tail</button>
    </div>
  </model-viewer>
  
  <script type="module">
    const modelViewer1 = document.querySelector('#animation-demo');
    const lines = modelViewer1.querySelectorAll('line');
    let baseRect;
    let noseRect;
    let hoofRect;
    let tailRect;
    
    function onResize(){
      baseRect = modelViewer1.getBoundingClientRect();
      noseRect = document.querySelector('#nose').getBoundingClientRect();
      hoofRect = document.querySelector('#hoof').getBoundingClientRect();
      tailRect = document.querySelector('#tail').getBoundingClientRect();
    }
  
    modelViewer1.addEventListener('ar-status', onResize);
  
    modelViewer1.addEventListener('load', () => {
      onResize();
      // update svg
      function drawLine(svgLine, name, rect) {
        const hotspot = modelViewer1.queryHotspot('hotspot-' + name);
        svgLine.setAttribute('x1', hotspot.canvasPosition.x);
        svgLine.setAttribute('y1', hotspot.canvasPosition.y);
        svgLine.setAttribute('x2', (rect.left + rect.right) / 2 - baseRect.left);
        svgLine.setAttribute('y2', rect.top - baseRect.top);
      }
  
      // use requestAnimationFrame to update with renderer
      const startSVGRenderLoop = () => {
        drawLine(lines[0], 'nose', noseRect);
        drawLine(lines[1], 'hoof', hoofRect);
        drawLine(lines[2], 'tail', tailRect);
        requestAnimationFrame(startSVGRenderLoop);
      };
  
      startSVGRenderLoop();
    });
  </script>
  <style>
  model-viewer {
    width: 1000px;
    height: 1000px;
  }
    .anchor{
      display: none;
    }
  
    .lineContainer{
      pointer-events: none;
      display: block;
    }
  
    .line{
      stroke: #16a5e6;
      stroke-width: 2;
      stroke-dasharray: 2
    }
  
    #container{
      position: absolute;
      display: flex;
      justify-content: space-evenly;
      bottom: 8px;
      left: 8px;
      width: 100%;
    }
  
    .label{
      background: #fff;
      border-radius: 4px;
      border: none;
      box-sizing: border-box;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.25);
      color: rgba(0, 0, 0, 0.8);
      display: block;
      font-family: Futura, Helvetica Neue, sans-serif;
      font-size: 18px;
      font-weight: 700;
      max-width: 128px;
      padding: 0.5em 1em;
      bottom: 10px;
      pointer-events: none;
    }
  
    #animation-demo::part(default-ar-button){
      bottom: 64px;
    }
  
    /* This keeps child nodes hidden while the element loads */
    :not(:defined) > * {
      display: none;
    }
  </style>
  """, width=1000, height=1000)


with tab2:

  components.html("""<script type="module" src="https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js"></script>


  <style>
  model-viewer {
    width: 500px;
    height: 500px;
  }
  .hotspot{
    display: block;
    width: 20px;
    height: 20px;
    border-radius: 10px;
    border: none;
    background-color: blue;
    box-sizing: border-box;
    pointer-events: none;
  }

  .hotspot[slot="hotspot-hand"]{
    --min-hotspot-opacity: 0;
    background-color: red;
  }

  .hotspot[slot="hotspot-foot"]:not([data-visible]) {
    background-color: transparent;
    border: 3px solid blue;
  }

  .annotation{
    background-color: #888888;
    position: absolute;
    transform: translate(10px, 10px);
    border-radius: 10px;
    padding: 10px;
  }
  /* This keeps child nodes hidden while the element loads */
  :not(:defined) > * {
    display: none;
  }
</style>
<model-viewer id="hotspot-demo" ar ar-modes="webxr" camera-controls touch-action="pan-y" src="https://modelviewer.dev/shared-assets/models/Astronaut.glb" poster="https://modelviewer.dev/assets/poster-astronaut.webp" shadow-intensity="1" alt="A 3D model of an astronaut.">
  <button class="hotspot" slot="hotspot-visor" data-position="0 1.75 0.35" data-normal="0 0 1"></button>
  <button class="hotspot" slot="hotspot-hand" data-position="-0.54 0.93 0.1" data-normal="-0.73 0.05 0.69">
    <div class="annotation">This hotspot disappears completely</div>
  </button>
  <button class="hotspot" slot="hotspot-foot" data-position="0.16 0.1 0.17" data-normal="-0.07 0.97 0.23" data-visibility-attribute="visible"></button>
  <div class="annotation">This annotation is fixed in screen-space</div>
</model-viewer>
  """, width=600, height=600)
  
with tab3:
  components.html("""<script type="module" src="https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js"></script>
<style>
model-viewer {
  width: 350px;
  height: 600px;
}
.hotspot{
    display: block;
    width: 20px;
    height: 20px;
    border-radius: 10px;
    border: none;
    background-color: blue;
    box-sizing: border-box;
    pointer-events: none;
  }

  .hotspot[slot="hotspot-hand"]{
    --min-hotspot-opacity: 0;
    background-color: red;
  }
  .annotation{
    background-color: #888888;
    position: absolute;
    transform: translate(10px, 10px);
    border-radius: 10px;
    padding: 10px;
</style>


<model-viewer src="https://modelviewer.dev/shared-assets/models/RobotExpressive.glb"
              alt="Robot"
              ar
              auto-rotate
              camera-controls>
              <button class="hotspot" slot="hotspot-hand" data-surface="13 0 62 64 65 0.764 0.125 0.111">
              
                <div class="annotation">This hotspot disappears completely</div>
              </button>
  </model-viewer>""", width=500, height=800)

  components.html("""<script type="module" src="https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js"></script>
<style>
model-viewer {
  width: 350px;
  height: 600px;
}
.hotspot{
    display: block;
    width: 20px;
    height: 20px;
    border-radius: 10px;
    border: none;
    background-color: blue;
    box-sizing: border-box;
    pointer-events: none;
  }

  .hotspot[slot="hotspot-hand"]{
    --min-hotspot-opacity: 0;
    background-color: red;
  }
  .annotation{
    background-color: #888888;
    position: absolute;
    transform: translate(10px, 10px);
    border-radius: 10px;
    padding: 10px;
</style>


<model-viewer src="https://modelviewer.dev/shared-assets/models/RobotExpressive.glb"
              alt="Robot"
              autoplay
              scale="0.2 0.2 0.2" 
              shadow-intensity="1"
              ar
              auto-rotate
              camera-controls>
              <button class="hotspot" slot="hotspot-hand" data-surface="13 0 62 64 65 0.764 0.125 0.111">
              
                <div class="annotation">This hotspot disappears completely</div>
              </button>
  </model-viewer>""", width=500, height=800)


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

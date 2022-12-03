from streamlit_webrtc import webrtc_streamer,WebRtcMode,RTCConfiguration
import streamlit as st
import yolov5 as yl
import streamlit as st
from PIL import Image
import numpy as np
import bn
# RTC_CONFIGURATION = RTCConfiguration(
#     {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
# )


st.title("Inventory Management System")
option=st.selectbox("Mode",("None","Staff"))
if option=="Staff":
    st.title("Staff")
    st.sidebar.title('Options')
    d=st.sidebar.date_input('Date') 
    
    mode=st.sidebar.radio("Mode",("image","Video","data"))
    
    if mode=="image":
        # upload = st.sidebar.checkbox("Upload")
        model = yl.load("./best.pt")
        model.conf=st.sidebar.slider("Threshold freq.",0.01,1.00,0.15)
       #model.conf = 0.25  # NMS confidence threshold
        model.iou = 0.45  # NMS IoU threshold
        model.agnostic = False  # NMS class-agnostic
        model.multi_label = False  # NMS multiple labels per box
        model.max_det = 1000
        image = st.file_uploader("Upload an Image", type="jpg")
        image_name = None

        if image is not None:
            image_name = image.name
            image = Image.open(image)
            image = np.array(image)

            results = model(image)

            predictions = results.pred[0]
            boxes = predictions[:, :4]  # x1, y1, x2, y2
            scores = predictions[:, 4]
            categories = predictions[:, 5]

            results.save(save_dir="Images/output/")
            st.image("Images/output/image0.jpg")
    elif mode=="Video":
            st.title('🎥Object Detection Video')
            webrtc_streamer(key="Key")
           

            # ctx = webrtc_streamer(
            #     key='Staff-Cam', 

            #     mode=WebRtcMode.SENDRECV,
            #     rtc_configuration=RTC_CONFIGURATION,

            #     media_stream_constraints={
            #         "video": True,
            #         "audio": False
            #     }
            # )
    elif mode=="data" and st.button('Reset'):
        bn.clear()
    else:
        bn.func()
        


  
        

       
    dmode=st.sidebar.radio("Download Mode",("None","Excel","csv"))
    if dmode == 'CSV':
        st.sidebar.download_button(label='Download as CSV', data=bn.val(), file_name='data.csv', mime='text/csv')





        


        
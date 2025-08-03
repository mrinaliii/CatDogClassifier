import streamlit as st
import requests
from PIL import Image
import io

st.set_page_config(
    page_title="Cat vs Dog Classifier",
    page_icon="",
    layout="centered"
)

st.title(" Cat vs Dog Classifier")
st.markdown("Upload an image and let AI determine if it's a cat or dog!")

st.sidebar.header("⚙Configuration")
api_url = st.sidebar.text_input(
    "Modal API URL",
    value="https://manuisliterallykirby--cat-dog-classifier-fastapi-app.modal.run",
    help="Enter your Modal deployment URL (without /predict)"
)

st.sidebar.markdown("""
### How to use:
1. Upload an image of a cat or dog
2. Click 'Classify Image'
3. See the results!

### Supported formats:
- PNG, JPG, JPEG
- Max file size: 200MB
""")

uploaded_file = st.file_uploader(
    "Choose an image...",
    type=['png', 'jpg', 'jpeg'],
    help="Upload a clear image of a cat or dog for best results"
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Uploaded Image")
        st.image(image, caption="Your uploaded image", use_column_width=True)
    
    with col2:
        st.subheader("Classification")
        
        if not api_url.strip():
            st.warning("⚠️ Please enter your Modal API URL in the sidebar")
        else:
            if st.button("Classify Image", type="primary"):
                try:
                    with st.spinner("Thinking..."):
                        img_bytes = io.BytesIO()
                        image.save(img_bytes, format='PNG')
                        img_bytes.seek(0)
                        
                        files = {"file": ("image.png", img_bytes, "image/png")}
                        response = requests.post(
                            f"{api_url.strip().rstrip('/')}/predict",
                            files=files,
                            timeout=30
                        )
                        
                        if response.status_code == 200:
                            result = response.json()
                            
                            st.success("Classification Complete!")
                            
                            prediction_class = result.get('class', 'Unknown')
                            confidence = result.get('confidence', 0)
                            
                            if prediction_class.lower() == 'cat':
                                emoji = "🐱"
                                color = "#800000"
                            else:
                                emoji = "🐶"
                                color = "#1D0248"
                            
                            st.markdown(f"""
                            <div style="text-align: center; padding: 20px; background-color: #f0f2f6; border-radius: 10px; margin: 10px 0;">
                                <h2 style="color: {color}; margin: 0;">{emoji} {prediction_class}</h2>
                                <p style="font-size: 18px; margin: 10px 0;">Confidence: <strong>{confidence:.1%}</strong></p>
                            </div>
                            """, unsafe_allow_html=True)
                            
                            st.progress(confidence)
                            if confidence > 0.9:
                                st.info("Very confident prediction!")
                            elif confidence > 0.7:
                                st.info("Good confidence level")
                            else:
                                st.warning("Low confidence - try a clearer image")
                                
                        else:
                            st.error(f"API Error: {response.status_code} - {response.text}")
                            
                except requests.exceptions.Timeout:
                    st.error("Request timed out. Please try again.")
                except requests.exceptions.ConnectionError:
                    st.error("Could not connect to API. Check your URL.")
                except requests.exceptions.RequestException as e:
                    st.error(f"Request failed: {str(e)}")
                except Exception as e:
                    st.error(f"Unexpected error: {str(e)}")

else:
    st.info("Upload an image above to get started!")
    
    st.markdown("### Example Usage")
    st.markdown("Here's what you can expect:")
    
    example_col1, example_col2 = st.columns(2)
    
    with example_col1:
        st.markdown("**🐱 Cat Example**")
        st.markdown("- Clear image of a cat")
        st.markdown("- Good lighting")
        st.markdown("- Cat is main subject")
    
    with example_col2:
        st.markdown("**🐶 Dog Example**") 
        st.markdown("- Clear image of a dog")
        st.markdown("- Good lighting")
        st.markdown("- Dog is main subject")

st.markdown("---")
st.markdown(
    "Built by Mrinali Charhate",
    help="This app connects to Modal deployment for image classification"

)

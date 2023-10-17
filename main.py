import streamlit as st
import qrcode
from io import BytesIO
import base64

st.title("QR CODE GENERATOR")

link = st.text_input("Enter the URL:", placeholder="https://example.com")

if not link:
    st.warning("PLEASE ENTER THE URL")

def generate_qr_code(link):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=8,
    )
    qr.add_data(link)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img_bytes = BytesIO()
    img.save(img_bytes, format="PNG")
    img_bytes = img_bytes.getvalue()

    st.image(img_bytes, use_column_width=True, caption="Generated QR Code")
    img_base64 = base64.b64encode(img_bytes).decode()

    return img_base64

if st.button("Generate QR Code"):
    img_base64 = generate_qr_code(link)

    st.download_button(
        label="Download QR Code",
        data=img_base64,
        file_name='qrcode.png',
        key='download_qr_code',
    )

css = """
<style>
/* Add your custom CSS styles here */

/* Style the Generate QR Code button with light gray background */
button {
    background-color: #f0f0f0 !important; /* Light gray background */
    color: #333 !important; /* Dark gray text color */
    border: none !important;
    border-radius: 5px !important;
    padding: 10px 20px !important;
    text-align: center !important;
    text-decoration: none !important;
    display: inline-block !important;
    font-size: 16px !important;
    margin: 20px 0 !important;
    cursor: pointer !important;
}

/* Style the warning message with a transparent background */
div[data-baseweb="warning"] {
    color: red !important;
    font-size: 16px !important;
    background-color: transparent !important; /* Transparent background */
    margin: 10px 0 !important;
}

</style>
"""

st.markdown(css, unsafe_allow_html=True)

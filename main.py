import streamlit as st
import qrcode
from io import BytesIO

st.title("QR CODE GENERATOR")

link = st.text_input("Enter The URL:", placeholder="https://example.com")

if not link:
    st.success("PLEASE ENTER THE URL")
else:
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

        return img_bytes

    if st.button("Generate QR Code"):
            img_bytes = generate_qr_code(link)
            st.image(img_bytes, use_column_width=True, caption="Generated QR Code")
            st.download_button(
            label="Download QR Code",
            data=img_bytes,
            file_name='qrcode.png',
            key='download_qr_code',
        )

css = """
<style>
/* Add your custom CSS styles here */

.stApp {
            background-image: url('https://images.unsplash.com/photo-1569982175971-d92b01cf8694?auto=format&fit=crop&q=80&w=1935&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D');
            background-size: cover;
            background-repeat: no-repeat;
            font-family: 'Helvetica', sans-serif;
    }
    
    /* Style the text input field */
input[type="text"] {
    background-color: black
}

/* Style the Generate QR Code button with light gray background */
button {
    background-color: black !important; /* Light gray background */
    color: white !important; /* Dark gray text color */
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

/* Hide Streamlit Branding */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

</style>
"""

st.markdown(css, unsafe_allow_html=True)

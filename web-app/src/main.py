import requests
import streamlit as st


def get_result_from_api(image):
    url = "https://api-inequamath.chades.fr/full"
    # url = "http://172.17.0.1:90/full"

    files = {"image": image}
    response = requests.post(url, files=files)

    if response.status_code == 200:
        return response.json()
    else:
        return None


if __name__ == "__main__":
    st.set_page_config(
        page_title="Inequamath",
        page_icon="random",
        # layout="wide",
        initial_sidebar_state="auto",
        menu_items=None,
    )

    with st.expander("Image picker", expanded=True):
        upload_image = st.file_uploader("Upload image")
        camera_image = st.camera_input("Camera")

    image = None
    if upload_image is not None and camera_image is not None:
        selected = st.radio("Select image input", ("Uploaded file", "Camera file"))
        if selected == "Uploaded file":
            image = upload_image
        elif selected == "Camera file":
            image = camera_image
    elif upload_image is not None:
        image = upload_image
    elif camera_image is not None:
        image = camera_image

    if image is not None:
        left, right = st.columns((1, 1))
        left.image(image)

        with right:
            with st.spinner("Solving inequation ..."):
                result = get_result_from_api(image)
                # try:
                #     result = get_result_from_api(image)
                # except:
                #     result = None

        if result is not None:
            if type(result) is str:
                right.error(f"Error: {result}")
            else:
                right.write(f"Detected inequation: {result['base']}")
                right.subheader(f"Result: {result['result']}")
        else:
            right.error("Error solving inequation !")
    else:
        st.info("Upload an image or take a picture from your camera")

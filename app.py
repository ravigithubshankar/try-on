import streamlit as st
from PIL import Image
import os

def run(cloth, model):
    make_dir()
    cloth.save("/tmp/inputs/test/cloth/cloth.jpg")
    model.save("/tmp/inputs/test/image/model.jpg")

    # running script to compute the predictions
    os.system("rm -rf /tmp/output/")
    os.system("python /app/clothes-virtual-try-on/run.py")

    # loading output
    op = os.listdir("/tmp/output")[0]
    op = Image.open(f"/tmp/output/{op}")
    return op

def make_dir():
    os.makedirs("/tmp/inputs/test/cloth", exist_ok=True)
    os.makedirs("/tmp/inputs/test/image", exist_ok=True)
    os.makedirs("/tmp/output", exist_ok=True)

def main():
    st.title("Clothes Virtual Try ON")

    st.write("Upload the Cloth Image")
    cloth_input = st.file_uploader("Choose a cloth image", type=["jpg", "jpeg", "png"])

    st.write("Upload the Human Image")
    model_input = st.file_uploader("Choose a human image", type=["jpg", "jpeg", "png"])

    if st.button("Submit"):
        if cloth_input and model_input:
            cloth = Image.open(cloth_input)
            model = Image.open(model_input)
            
            result_image = run(cloth, model)
            
            st.image(result_image, caption='Final Prediction', use_column_width=True)
        else:
            st.warning("Please upload both images")

if __name__ == "__main__":
    main()

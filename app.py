import gradio as gr
import cv2
import numpy as np
from ultralytics import YOLO


model = YOLO(r"D:\Full_stack_ML\Internship\U\best.pt")

def process_image(image):
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)  
    results = model.predict(image, conf=0.15)
    
    if len(results[0].boxes.cls) == 1:
        mask_tensor = results[0].masks.data[0].cpu().numpy()
        mask = (mask_tensor * 255).astype(np.uint8)
        
        mask = cv2.resize(mask, (image.shape[1], image.shape[0]))
        kernel = np.ones((5, 5), np.uint8)
        mask = cv2.dilate(mask, kernel, iterations=2)
        mask = cv2.erode(mask, kernel, iterations=2)
        
        rgba_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGBA)
        rgba_image[:, :, 3] = mask
        
        return rgba_image
    else:
        return "Error: Uploaded image has more than one face. Please upload a different image."


demo = gr.Interface(
    fn=process_image,
    inputs=gr.Image(type="numpy"),
    outputs=gr.Image(type="numpy"),
    title="Face Segmentation",
    description="Upload an image"
)

if __name__ == "__main__":
    demo.launch()

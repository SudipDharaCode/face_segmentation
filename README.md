# Face Segmentation using YOLO and Gradio

This project is a **Face Segmentation Web App** that uses **YOLOv8** for detecting and segmenting a single face from an uploaded image. The app is built using **Gradio** for an interactive user interface.

## Features
- ✅ Detects and segments a **single face** from an uploaded image.
- ✅ Generates an **RGBA image** with the segmented face.
- ✅ Provides **error handling** if no face or multiple faces are detected.
- ✅ **Gradio UI** for easy interaction.

## Installation & Setup

### 1. Clone the Repository
```sh
git clone https://github.com/your-username/face-segmentation.git
cd face-segmentation
```

### 2. Install Dependencies
Make sure you have Python **3.8+** installed.  
Run the following command to install dependencies:
```sh
pip install -r requirements.txt
```

### 3. Add Model File
Place the **best.pt** model file inside the project folder.

### 4. Run the Application
```sh
python app.py
```
This will launch the **Gradio web interface**, and you can start uploading images.

## Usage
1. **Upload an image** containing a single face.
2. The app will segment the face and return an RGBA image with transparency.
3. If no face or multiple faces are detected, an **error message** will be displayed.

## Folder Structure
```
📂 face-segmentation/
 ├── 📜 app.py                # Main application file
 ├── 📜 requirements.txt       # Required dependencies
 ├── 📜 best.pt               # YOLO model file
 ├── 📜 README.md              # Project documentation
```

## Troubleshooting
- **Issue:** No face detected.  
  **Solution:** Try using an image with a clearly visible face.  

- **Issue:** More than one face detected.  
  **Solution:** Ensure that only **one** face is present in the image.  

- **Issue:** App crashes on startup.  
  **Solution:** Make sure `best.pt` is present in the project directory.


This project implements real-time face detection using Haar Cascade Classifiers provided by OpenCV.
It captures live video from a webcam, detects human faces in each frame, and highlights them using bounding boxes.

The project focuses on understanding classical computer vision techniques and real-time video processing using Python.

Technologies Used:
Python
OpenCV (cv2)
Haar Cascade Classifier
Webcam

How the Project Works:
1.Loads a pre-trained Haar Cascade XML file for face detection
2.Accesses the system webcam
3.Converts each video frame to grayscale
4.Detects faces using detectMultiScale()
5.Draws rectangles and labels around detected faces
6.Displays real-time detection until the user exits

How to Run the Project:
Step 1: Install required library
pip install opencv-python
Step 2: Run the Python file
python face_detection.py
Step 3: Provide Haar Cascade XML path
When prompted, enter the path to:
haarcascade_frontalface_default.xml(enter path of this file)
Step 4: Exit the application
Press q to stop the webcam and close the window.(if q is mentioned in code)

Output
Real-time webcam feed
Green rectangle drawn around detected faces
Text displayed: “Face Detected”

Key Concepts Covered:
Haar Cascade classifiers
Grayscale image processing
Real-time video capture
OpenCV drawing utilities


Limitations of Haar Cascades:
Works best for frontal faces
Performance decreases with:
1.Side or tilted faces
2.Poor lighting conditions
3.Occluded faces (mask, sunglasses)
Not as robust as deep learning–based detector


Possible Enhancements:
Replace Haar Cascade with DNN-based face detection
Add face count on screen
Improve accuracy using parameter tuning
Display FPS counter
Advanced models like YOLO,MediaPipe


Use Cases:
Beginner computer vision projects
Academic demonstrations
Learning classical face detection techniques
OpenCV practice projects


Author:
Abhiram Mutyampalli
Student | Aspiring AI / ML Engineer

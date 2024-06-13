Facial Recognition Project
This project implements a facial recognition system using Python, OpenCV, and the face_recognition library. The system is designed to recognize a specific individual from a set of images and draw a red box around any unrecognized faces, labeling them as "Unknown".

Table of Contents
Installation
Usage
Project Structure
How It Works
Example Code
Contributing
License
Installation
Clone the repository:
git clone https://github.com/thegreatgabuza/face_recognition_teegee.git
cd facial-recognition-project
Create a virtual environment and activate it:
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the required packages:
pip install -r requirements.txt
Usage
Place your images in the images directory. Ensure that the images you want to recognize are named appropriately.
Run the facial recognition script:
python recognize_faces.py
The script will process the images and display the results, drawing a red box around unrecognized faces and labeling them as "Unknown".
Project Structure
facial-recognition-project/
│
├── images/
│   ├── known_person1.jpg
│   ├── known_person2.jpg
│   └── ...
│
├── recognize_faces.py
├── requirements.txt
└── README.md
How It Works
Loading Images: The script loads images from the images directory.
Encoding Faces: It encodes the faces of known individuals.
Face Recognition: It compares faces in the images to the known faces.
Drawing Boxes: If a face is recognized, it draws a green box around it. If not, it draws a red box and labels it as "Unknown".

Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

License
This project is licensed under the MIT License. See the LICENSE file for details.

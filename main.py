import face_recognition
import cv2

# Paths to the images and corresponding names
image_paths = [
    "C:\\Users\\admin\\Downloads\\avatar.jpg",
    "C:\\Users\\admin\\Downloads\\thobani.jpg",
    "C:\\Users\\admin\\Downloads\\thobanis.jpg",
    "C:\\Users\\admin\\Downloads\\thoba.jpg"
]
names = ["Amanda", "Thobani", "TG at the Lab", "TG"]

# Load and encode the known faces
known_face_encodings = []
known_face_names = []

for path, name in zip(image_paths, names):
    try:
        image = face_recognition.load_image_file(path)
        encodings = face_recognition.face_encodings(image)
        if encodings:
            encoding = encodings[0]  # Use the first found face encoding
            known_face_encodings.append(encoding)
            known_face_names.append(name)
        else:
            print(f"No faces found in the image {path}")
    except Exception as e:
        print(f"Failed to process image {path}: {str(e)}")

# Initialize webcam
video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    if not ret:
        print("Failed to grab frame")
        break

    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    print(f"Detected {len(face_locations)} faces")  # Debugging line

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"
        box_color = (0, 0, 255)  # Red for unrecognized face

        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]
            box_color = (0, 255, 0)  # Green for recognized face

        cv2.rectangle(frame, (left, top), (right, bottom), box_color, 2)
        cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255), 1)

    cv2.imshow("Video", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()

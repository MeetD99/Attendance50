import dlib
import numpy as np
import cv2
import os
from scipy.spatial import distance

# Initialize dlib's face detector, shape predictor, and face recognition model
detector = dlib.get_frontal_face_detector()
shape_predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
face_recognition_model = dlib.face_recognition_model_v1("dlib_face_recognition_resnet_model_v1.dat")

def get_face_descriptor(image):
    detected_faces = detector(image, 1)
    if len(detected_faces) > 0:
        shape = shape_predictor(image, detected_faces[0])
        return np.array(face_recognition_model.compute_face_descriptor(image, shape))
    else:
        return None

def compare_faces(known_faces, face):
    return np.linalg.norm(known_faces - face, axis=1)

def add_student_face(student_image_path, known_face_encodings, known_face_names):
    # Check if the file is an image
    if not student_image_path.lower().endswith(('.png', '.jpg', '.jpeg')):
        print(f"Skipped non-image file: {student_image_path}")
        return

    student_image = cv2.imread(student_image_path)
    # Check if the image was loaded successfully
    if student_image is None:
        print(f"Failed to load image: {student_image_path}")
        return

    student_image_rgb = cv2.cvtColor(student_image, cv2.COLOR_BGR2RGB)
    face_descriptor = get_face_descriptor(student_image_rgb)
    if face_descriptor is not None:
        known_face_encodings.append(face_descriptor)
        known_face_names.append(os.path.basename(student_image_path))


# Prepare student faces
known_face_encodings = []
known_face_names = [] # To keep track of whose face it is

# Assuming student photos are in a folder named 'student_photos'
student_photos_path = 'dummies'
for student_photo in os.listdir(student_photos_path):
    add_student_face(os.path.join(student_photos_path, student_photo), known_face_encodings, known_face_names)

# Load the class photo
class_image = cv2.imread('classroom/group2.jpg')
class_image_rgb = cv2.cvtColor(class_image, cv2.COLOR_BGR2RGB)

# Detect and recognize faces in the class photo
for face in detector(class_image_rgb, 1):
    shape = shape_predictor(class_image_rgb, face)
    face_descriptor = np.array(face_recognition_model.compute_face_descriptor(class_image_rgb, shape))
    distances = compare_faces(known_face_encodings, face_descriptor)
    best_match_index = np.argmin(distances)
    if distances[best_match_index] < 0.5:  # Threshold for a match
        print(f"Match found: {known_face_names[best_match_index]}")
        student_name = known_face_names[best_match_index]

        # Draw a rectangle around the face
        x, y, w, h = face.left(), face.top(), face.width(), face.height()
        cv2.rectangle(class_image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Put text (student name) below the face
        cv2.putText(class_image, student_name, (x, y + h + 30), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0,0,255), 2)

# Display the resulting image
cv2.imshow('Class Photo with Matched Faces', class_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

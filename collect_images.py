import os
import cv2

DATA_DIR = './data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

number_of_classes = 26
dataset_size = 100

# Try with camera index 0 instead of 2
cap = cv2.VideoCapture(0)

# Check if camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

for j in range(number_of_classes):
    class_dir = os.path.join(DATA_DIR, str(j))
    if not os.path.exists(class_dir):
        os.makedirs(class_dir)

    print('Collecting data for class {}'.format(j))

    # Ready prompt
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break
            
        cv2.putText(frame, 'Ready? Press "Q" ! :)', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
        cv2.imshow('frame', frame)
        if cv2.waitKey(25) == ord('q'):
            break

    # Image collection
    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break
            
        cv2.imshow('frame', frame)
        key = cv2.waitKey(25)
        if key == 27:  # ESC to exit
            break
            
        cv2.imwrite(os.path.join(class_dir, '{}.jpg'.format(counter)), frame)
        counter += 1

cap.release()
cv2.destroyAllWindows()
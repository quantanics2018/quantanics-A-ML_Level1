import cv2
import glob
from vehicle_detector import VehicleDetector

# Load Vehicle Detector
vd = VehicleDetector()

# Load images from a folder
images_folder = glob.glob(r"D:\!!\Music\quantanics-A-ML_Level1\Vehicle detection using deep learning\*.jpeg")

vehicles_folder_count = 0

# Fixed dimensions for resizing
resize_width = 800
resize_height = 600

# Loop through all the images
for img_path in images_folder:
    print("Img path", img_path)
    img = cv2.imread(img_path)
    
    # Resize the image
    img = cv2.resize(img, (resize_width, resize_height))

    vehicle_boxes = vd.detect_vehicles(img)
    vehicle_count = len(vehicle_boxes)

    # Update total count
    vehicles_folder_count += vehicle_count

    for box in vehicle_boxes:
        x, y, w, h = box

        cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 3)

        cv2.putText(img, "Vehicles: " + str(vehicle_count), (20, 50), 0, 2, (100, 200, 0), 3)

    cv2.imshow("Cars", img)
    cv2.waitKey(0)

print("Total current count", vehicles_folder_count)

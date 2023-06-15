import os

image_folder = "./test/images"

# Iterate through the images in the folder
for filename in os.listdir(image_folder):
    if filename.endswith(".jpeg") or filename.endswith(".jpg") or filename.endswith(".png"):
        image_path = os.path.join(image_folder, filename)
        
        # Perform object detection on the current image
        # Use the YOLO command with the image_path as the source
        
        # Replace the following line with your YOLO command
        yolo_command = f"yolo task=detect mode=predict model=best.pt show=True conf=0.7 source={image_path}"
        
        # Execute the YOLO command
        os.system(yolo_command)
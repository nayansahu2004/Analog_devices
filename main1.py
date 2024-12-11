from ultralytics import YOLO

# Initialize the model
model = YOLO("yolov8.pt")

# Custom callback to print images and labels during training
def print_image_labels(batch):
    # Access the image and label filenames
    for img, lbl in zip(batch['img'], batch['label']):
        img_path = batch['path'][0]  # Image path (if available)
        lbl_path = img_path.replace(img_path.split('.')[-1], 'txt')  # Assuming label has .txt extension
        print(f"Image: {img_path}, Label: {lbl_path}")

# Train the model
results = model.train(
    data="config.yaml", 
    batch=16, 
    epochs=1, 
    imgsz=640,
    callbacks=[print_image_labels]  # Add custom callback
)


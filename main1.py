from ultralytics import YOLO
from ultralytics.yolo.engine.train import Trainer
from ultralytics.yolo.utils.datasets import LoadImagesAndLabels

# Custom class that inherits from LoadImagesAndLabels to log image-label pairs
class CustomDataset(LoadImagesAndLabels):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __getitem__(self, index):
        # Access the image and label paths
        img, lbl, img_path, lbl_path, shapes = super().__getitem__(index)
        print(f"Image: {img_path}, Label: {lbl_path}")
        return img, lbl, img_path, lbl_path, shapes

# Initialize YOLO model
model = YOLO("yolov8.pt")

# Override the default dataset loading method with the custom one
model.train(data="config.yaml", batch=16, epochs=1, imgsz=640, dataset=CustomDataset)

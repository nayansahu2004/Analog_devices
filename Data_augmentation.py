#This is the first line
import cv2
import albumentations as A
import numpy as np

for i in range(0, 10):
    # Load the image
    image_path = f"orange/image_{i + 1}.jpg"  # Assuming the images are in JPG format
    image = cv2.imread(image_path)

    # Check if the image was successfully loaded
    if image is None:
        raise FileNotFoundError(f"Image not found at {image_path}")

    # Resize and letterbox
    target_size = (640, 640)
    padding_color = (128, 128, 128)
    original_height, original_width = image.shape[:2]

    scale = min(target_size[0] / original_width, target_size[1] / original_height)
    new_width = int(original_width * scale)
    new_height = int(original_height * scale)

    resized_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_CUBIC)
    # letterboxed_image = np.full((target_size[1], target_size[0], 3), padding_color, dtype=np.uint8)

    # pad_x = (target_size[0] - new_width) // 2
    # pad_y = (target_size[1] - new_height) // 2
    # letterboxed_image[pad_y:pad_y + new_height, pad_x:pad_x + new_width] = resized_image

    # Normalize image for saving (optional, as cv2.imwrite handles uint8 directly)
    image_normalized = resized_image/255.0
    image_to_save = (image_normalized * 255).astype(np.uint8)

    # Apply Albumentations transforms
    transform = A.Compose([
        #A.HorizontalFlip(p=0.5),  # Flip the image horizontally
        A.RandomBrightnessContrast(brightness_limit=0.4, contrast_limit=0.2, p=0.5),  # Brightness and contrast
        A.ShiftScaleRotate(shift_limit=0.1, scale_limit=0.2, rotate_limit=40, p=0.5),  # Shift, scale, and rotate
        A.GaussianBlur(blur_limit=(3, 5), p=0.5),  # Gaussian blur
        A.HueSaturationValue(hue_shift_limit=5, sat_shift_limit=15, val_shift_limit=5, p=0.3)  # Color adjustments
    ])

    augmented_images = []
    for j in range(10):  # Generate 10 augmented images per input image
        augmented = transform(image=resized_image)
        augmented_image = augmented['image']
        augmented_images.append(augmented_image)

    # Save augmented images
    for j, aug_img in enumerate(augmented_images):
        save_path = f"C:\\Users\\Dell\\Desktop\\python\\processed_image\\saved_image_{i+1}_{j+1}.jpg"
        cv2.imwrite(save_path, aug_img)
    
    print(f"Augmented images for image_{i+1} saved!")

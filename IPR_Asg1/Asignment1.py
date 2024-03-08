import cv2

def resize_and_threshold(image_path, output_path, resize_width, resize_height, threshold_value):
    
    # Read the image from the specified path
    img = cv2.imread(image_path)

    if img is None:
        print(f"Error: Unable to load image at {image_path}")
        return

    # Resize the image
    resized_img = cv2.resize(img, (resize_width, resize_height))

    # Convert the resized image to grayscale
    gray_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)

    # Apply binary thresholding
    _, threshold_img = cv2.threshold(gray_img, threshold_value, 255, cv2.THRESH_BINARY)

    # Save the resulting image to the specified output path
    cv2.imwrite(output_path, threshold_img)

    print(f"Output saved at {output_path}")

if __name__ == "__main__":
    image_path = "download.jpg"  
    output_path = "update_image.jpg"  
    resize_width = 350  
    resize_height = 250  
    threshold_value = 127  

    resize_and_threshold(image_path, output_path, resize_width, resize_height, threshold_value)

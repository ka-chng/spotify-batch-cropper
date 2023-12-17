from PIL import Image
import os

def stretch_images(input_folder, output_folder, target_size=(300, 300)):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        with Image.open(input_path) as img:
            img = img.resize(target_size)
            img.save(output_path)

if __name__ == "__main__":
    input_folder = "input_images"
    output_folder = "output_images_stretched"

    stretch_images(input_folder, output_folder)

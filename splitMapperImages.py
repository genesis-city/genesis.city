import os
from PIL import Image

input_directory = 'testImagesInput'
output_directory = 'testImagesOutput'

def split_image(img_path, output_dir):
    try:
        # Parse the image name to get the central coordinates (OpenLayers coordinates)
        base_name = os.path.basename(img_path)
        base_name = os.path.splitext(base_name)[0]
        central_OL_x, centra_OL_y = map(int, base_name.split(','))

        # Convert OpenLayers coordinates to Decentraland coordinates
        n = 5
        pad = 30
        central_x = (central_OL_x - pad) * n
        central_y = (pad - centra_OL_y) * n
 
        # Open the image
        img = Image.open(img_path)
        img_width, img_height = img.size

        # Size of each parcel
        parcel_width = img_width // 5
        parcel_height = img_height // 5

        # Make sure the output directory exists
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Cut the image and save each parcel
        for i in range(5):
            for j in range(5):
                left = j * parcel_width
                upper = i * parcel_height
                right = left + parcel_width
                lower = upper + parcel_height
                parcel_img = img.crop((left, upper, right, lower))

                # Calculate the coordinates for each parcel
                parcel_x = central_x - 2 + j
                parcel_y = central_y + 2 - i

                # Save the parcel image with the new name
                parcel_name = f'{parcel_x},{parcel_y}.jpg'
                parcel_path = os.path.join(output_dir, parcel_name)
                parcel_img.save(parcel_path)

        print(f'Finished processing {img_path}')

    except Exception as e:
        print(f'Error processing {img_path}: {e}')

# Main function to process all images in a directory
def process_images(input_dir, output_dir):
    for filename in os.listdir(input_dir):
        if filename.endswith('.jpg'):
            img_path = os.path.join(input_dir, filename)
            split_image(img_path, output_dir)


# Run the main function
process_images(input_directory, output_directory)

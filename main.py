import pydicom
from pydicom.pixel_data_handlers.util import apply_voi_lut
from PIL import Image

# Function to convert DICOM to PIL image
def dicom_to_image(dicom_path):
    # Load the DICOM file
    dicom = pydicom.dcmread(dicom_path)

    # Apply VOI LUT if present (for better visualization)
    image = apply_voi_lut(dicom.pixel_array, dicom)

    # Normalize the image to 0-255 and convert to uint8
    image = (image - image.min()) / (image.max() - image.min()) * 255
    image = image.astype('uint8')

    # Convert to a PIL image
    pil_image = Image.fromarray(image)
    return pil_image

# List your DICOM file paths here
file_paths = [
    "01.dcm",
    "02.dcm",
    "03.dcm"
]

# Convert the DICOM files to images
dicom_images = [dicom_to_image(file_path) for file_path in file_paths]

# Ensure all images have the same width for stitching
widths, heights = zip(*(img.size for img in dicom_images))
max_width = max(widths)
resized_images = [
    img.resize((max_width, int(img.height * max_width / img.width))) if img.width != max_width else img
    for img in dicom_images
]

# Combine heights for a panoramic image
total_height = sum(img.height for img in resized_images)
panoramic_image = Image.new('L', (max_width, total_height))  # Grayscale image ('L')

# Stitch images together vertically
y_offset = 0
for img in resized_images:
    panoramic_image.paste(img, (0, y_offset))
    y_offset += img.height

# Save the resulting panoramic image
output_path = "lower_extremities_panoramic.jpg"
panoramic_image.save(output_path)
print(f"Panoramic image saved to {output_path}")

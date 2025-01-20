# DICOM Panoramic Image Stitcher

This Python script processes DICOM files containing X-rays of the lower extremities, converts them into images, and stitches them together to create a single panoramic view.

## Features

- Converts DICOM files to image format using `pydicom`.
- Normalizes and enhances the images for better visualization.
- Stitches the images vertically to produce a continuous panoramic image.
- Outputs the result as a single `.jpg` file.

## Requirements

Ensure you have Python 3.7+ installed. Install the required dependencies with:

```bash
pip install -r requirements.txt
```

## Dependencies

- **pydicom**: For reading and processing DICOM files.
- **Pillow**: For handling and manipulating images.

## Usage

1. Clone this repository:

- ```git clone https://github.com/Volodymyr0587/DICOM-Panoramic-Image-Stitcher```

- ```cd dicom-panoramic-stitcher```

2. Place your DICOM files in the same directory or update their paths in the script.

3. Update the file paths in ```main.py```:

```
file_paths = [
    "path/to/xray1.dcm",
    "path/to/xray2.dcm",
    "path/to/xray3.dcm"
]
```

4. Run the script:

```python main.py```

5. The stitched panoramic image will be saved as lower_extremities_panoramic.jpg.
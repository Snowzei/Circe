# Circe

[![Windows](https://img.shields.io/badge/Platform-Windows-blue)](https://www.microsoft.com/)
[![Python](https://img.shields.io/badge/Language-Python-brightgreen)](https://www.python.org/)
[![Pillow](https://img.shields.io/badge/Library-Pillow-yellow)](https://pillow.readthedocs.io/en/stable/)

A command-line tool to convert image files to either JPEG or PNG format.

## Installation

1. Clone the repository:

```
git clone https://github.com/Snowzei/Circe.git
cd circe
```

2. Install the required dependencies using pip:

```
pip install -r requirements.txt
```

## Usage

Run the script to convert image files in a specified directory to either JPEG or PNG format.

```
python circe.py /path/to/images -jpeg -o /output/directory
```

### Command-Line Arguments

- ```directory```: The directory containing image files to be converted.
- ```-j, --jpeg```: If provided, convert images to JPEG format; otherwise, convert to PNG (default).
- ```-o, --output```: Specify the output directory for converted images. If not provided, the converted images will be saved in the same directory as the original images.
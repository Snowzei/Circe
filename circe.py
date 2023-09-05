from PIL import Image
from os import makedirs, path, listdir
from argparse import ArgumentParser
from sys import exit

def convert_images_in_directory(directory:str, to_jpeg:bool=False, output_dir:str=None):
    """
    Convert image files in a specified directory to either JPEG or PNG format.

    Args:
        directory (str): The directory containing image files to be converted.
        to_jpeg (bool, optional): If True, convert images to JPEG format; otherwise, convert to PNG (default).
        output_dir (str, optional): The directory where converted images will be saved.
            If not provided, the converted images will be saved in the same directory as the original images.

    Raises:
        OSError: If the provided directory does not exist.
        
    Note:
        - Supported input image file extensions are ".heic" and ".cr2" (modify as needed).
        - The "converted_images" folder within the specified directory will not be processed.

    Example:
        convert_images_in_directory("/path/to/images", to_jpeg=True, output_dir="/output/directory")
    """
    # If output_dir is not provided, save in the same directory as the original images
    if output_dir is None:
        makedirs(path.join(directory, "converted_images"))
        output_dir = path.join(directory, "converted_images")
    else:
        makedirs(output_dir, exist_ok=True)
    
    # Get a list of all files in the directory
    files = listdir(directory)
    
    # Iterate through the files
    for file in files:
        file_name, file_extension = path.splitext(file)
        try:
            # Don't try to convert the converted_image folder because obviously the code will shit the bed
            if file_name == "converted_images":
                continue
            # Open and convert the image
            img = Image.open(path.join(directory, file))
            if to_jpeg:
                img = img.convert("RGB")
                img.save(path.join(output_dir, file_name + ".jpeg"), "JPEG")
            else:
                img.save(path.join(output_dir, file_name + ".png"), "PNG")
        except Exception as e:
            print(f"Error converting {file}: {str(e)}")

if __name__ == "__main__":
    """
    Main script to convert image files in a specified directory to either JPEG or PNG format.

    The script accepts command-line arguments to specify the input directory, the desired output format
    (JPEG or PNG), and the output directory for converted images.

    Command-Line Arguments:
        directory (str): The directory containing image files to be converted.
        -j, --jpeg (flag): If provided, convert images to JPEG format; otherwise, convert to PNG (default).
        -o, --output (str, optional): The directory where converted images will be saved.
            If not provided, the converted images will be saved in the same directory as the original images.

    Example:
        python script.py /path/to/images -jpeg -o /output/directory
    """
    parser = ArgumentParser(description="Convert image files to JPEG or PNG.")
    parser.add_argument("directory", help="The directory containing image files.")
    parser.add_argument("--j", "--jpeg", action="store_true", help="Convert to JPEG instead of PNG.")
    parser.add_argument("-o", "--output", help="Specify the output directory for converted images.")
    
    args = parser.parse_args()
    
    directory_path = args.directory
    convert_to_jpeg = args.jpeg
    output_directory = args.output
    
    # Check if the provided directory exists
    if not path.isdir(directory_path):
        print(f"Error: The specified directory '{directory_path}' does not exist.")
        exit(1)
    
    convert_images_in_directory(directory_path, convert_to_jpeg, output_directory)
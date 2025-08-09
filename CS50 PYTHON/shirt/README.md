# SHIRT

## Overview

This Python script provides a command-line tool for overlaying a shirt image onto portrait photographs. The program uses the Python Imaging Library (PIL) to crop input images to match a reference shirt template and composites them together using alpha masking.

## Features

- Command-line interface for batch processing

- Automatic image resizing and cropping to match shirt dimensions

- Support for multiple image formats (JPG, JPEG, PNG)

- Alpha channel masking for seamless shirt overlay

- Input validation and error handling

## Requirements

### Dependencies

- Python 3.x

- Pillow (PIL Fork)

### Installation

Install the required dependency using pip:

```

pip install Pillow

```

### Required Files

- `shirt.png` - The shirt template image (must be in the same directory as the script)

- Input portrait image

## Usage

### Command Syntax

```

python script_name.py input_image output_image

```

### Parameters

- `input_image` - Path to the source portrait image

- `output_image` - Path where the processed image will be saved

### Examples

```

python shirt_overlay.py portrait.jpg result.jpg
python shirt_overlay.py photo.png output.png
python shirt_overlay.py image.jpeg final.jpeg

```

## Supported File Formats

The following image formats are supported for both input and output:

- `.jpg`

- `.jpeg`

- `.png`

**Note:** Input and output files must have the same file extension.

## How It Works

### Process Flow

1. **Argument Validation** - Ensures exactly two arguments are provided

2. **Format Validation** - Checks that both input and output use supported formats

3. **Extension Matching** - Verifies input and output have identical file extensions

4. **Image Processing**:

- Opens the reference shirt template (`shirt.png`)

- Loads the input portrait image

- Crops and resizes the portrait to match shirt dimensions using `ImageOps.fit()`

- Overlays the shirt using alpha masking

- Saves the final composite image

### Image Processing Details

- **Cropping**: Uses `ImageOps.fit()` to resize and crop the input image to exactly match the shirt template dimensions

- **Masking**: Employs the shirt's alpha channel as a mask for seamless overlay

- **Composition**: The shirt is pasted onto the cropped portrait, preserving transparency

## Error Handling

The script includes comprehensive error handling for common issues:

- **Insufficient Arguments**: ``Too few command-line arguments''

- **Excess Arguments**: ``Too many command-line arguments''

- **Unsupported Format**: ``Invalid output''

- **Extension Mismatch**: ``Input and output have different extensions''

- **Missing Files**: ``Input does not exist''

## Technical Implementation

### Key Functions

#### main()

Handles command-line argument parsing and validation. Performs preliminary checks before delegating to the image processing function.

#### edit_photo(input, output)

Core image processing function that:

- Loads the shirt template and input image

- Performs cropping and resizing operations

- Applies the shirt overlay using alpha masking

- Saves the final result

### Dependencies Used

- `PIL.Image` - Core image manipulation

- `PIL.ImageOps` - Image operations including fitting/cropping

- `sys` - Command-line argument handling and program exit

- `os` - File path operations

## File Structure

```

project_directory/
├── script_name.py          # Main script file
├── shirt.png              # Required shirt template
├── input_image.jpg        # Your portrait image
└── output_image.jpg       # Generated result

```

## Code Overview

The main script contains two primary functions:

\vspace{10pt}

**Function: main()**

- Validates command-line arguments (exactly 2 required)

- Checks file extensions for supported formats

- Ensures input and output extensions match

- Calls the image editing function if all validations pass

\vspace{10pt}

**Function: edit_photo(input, output)**

- Opens the shirt template image

- Processes the input portrait image

- Applies cropping and fitting operations

- Composites the shirt overlay using masking

- Saves the final result

## Workflow Steps

1. Place `shirt.png` in the same directory as your script

2. Run the script with input and output file paths

3. The script automatically:

- Validates your arguments

- Loads both images

- Resizes the portrait to match the shirt dimensions

- Applies the shirt overlay

- Saves the composite image

## Algorithm Details

The image processing follows this sequence:

1. Load the shirt template to determine target dimensions

2. Open the input portrait image

3. Use `ImageOps.fit()` to crop and resize the portrait:

- Maintains aspect ratio

- Centers the crop automatically

- Matches exact shirt template size

4. Apply shirt overlay using alpha compositing

5. Save the final composite image

## Troubleshooting

### Common Issues

- **``Input does not exist''**: Verify the input file path is correct and the file exists

- **``Invalid output''**: Ensure output file uses .jpg, .jpeg, or .png extension

- **Missing shirt.png**: The shirt template must be in the same directory as the script

- **Extension mismatch**: Input and output must use the same file format

- **Permission errors**: Ensure you have write permissions for the output directory

### Best Practices

- Use high-resolution input images for better results

- Ensure the shirt.png template has proper alpha transparency

- Keep input images in standard aspect ratios

- Test with different image formats to find optimal results

## Performance Considerations

- Processing time depends on input image resolution

- Memory usage scales with image dimensions

- PNG files with transparency may take longer to process

- Consider batch processing for multiple images

## Compilation Instructions

To compile this README into a PDF:

```

pdflatex readme.tex

```

Or if you prefer XeLaTeX:

```

xelatex readme.tex

```


- Ensure file paths and permissions are correct

- Test with sample images to isolate issues

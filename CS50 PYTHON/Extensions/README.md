# Python Script for File Extension to MIME Type Conversion

## Overview

This Python script prompts the user for a filename, deduces its extension, and prints out the corresponding MIME (Multipurpose Internet Mail Extensions) type. It covers common filetypes and provides a default type for unknown extensions.

## Code

```python
name = input("Give me a filename:").lower()
stripped_name = name.strip()
ext = stripped_name.rsplit('.', 1)[-1]

if ext in ("gif", "png", "jpeg"):
print(f'image/{ext}')
elif ext in ("jpg"):
print('image/jpeg')
elif ext in ("pdf", "zip"):
print(f'application/{ext}')
elif ext == "txt":
print("text/plain")
else:
print("application/octet-stream")
```

## How It Works

1. Asks user to input a filename.

2. Strips whitespace and converts the filename to lowercase for robust matching.

3. Extracts the substring after the last period (`.`) as the file extension.

4. Prints the matching MIME type based on the extension:

- Image types: `gif`, `png`, `jpeg`, `jpg`

- Application types: `pdf`, `zip`

- Text type: `txt`

- Defaults to `application/octet-stream` for unknown or generic files

## Requirements

- Python 3.x

- No additional packages required

## Example Usage

```

Give me a filename: puppy.jpg
image/jpeg

Give me a filename: manual.PDF
application/pdf

Give me a filename: notes.txt
text/plain

Give me a filename: archive.rar
application/octet-stream

```

## Notes

- The script is case-insensitive and trims whitespace to prevent mismatches.

- Only the last extension is considered (for filenames like `file.tar.gz`, only `gz` is checked).

- Expandable by modifying or adding cases to the `if` statements.

- For full lists of MIME types, see: <https://www.iana.org/assignments/media-types/media-types.xhtml>

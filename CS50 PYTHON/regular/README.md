# um-count Python Project

*Your Name*

*July 21, 2025*

## Overview

**um-count** is a Python utility for counting occurrences of the filler word ``um'' in a given string of text. It provides a simple function, `count()`, which receives a string as input and returns the number of times ``um'' appears as a stand-alone word, regardless of surrounding punctuation or case.

## Files

- `um.py`: Contains the implementation of the `count` function.

- `test_um.py`: Contains test cases to validate the function.

## Requirements

- Python 3.6 or newer

## Getting Started

1. Clone or download this repository.

2. Ensure you have Python 3.6+ installed.

3. Place your `um.py` and test code (`test_um.py`) in the same directory.

## Usage

### Command Line

You can run the tests by simply executing `test_um.py`. For example:

\begin{lstlisting}[language=bash]
python test_um.py
\end{lstlisting}

### In Python Code

Import and call the `count` function as follows:

\begin{lstlisting}[language=Python]
from um import count

text = "Um, this is a test."
num_ums = count(text)
print(num_ums)  # Output: 1
\end{lstlisting}

## Testing

Three test cases are included:

- `test1`: No occurrences of ``um''.

- `test2`: One occurrence of ``um''.

- `test3`: Two occurrences of ``um'' with punctuation.

Add further tests as needed to `test_um.py`:

\begin{lstlisting}[language=Python]
def test_custom():
assert count("um um um!") == 3
\end{lstlisting}

## Implementation Details

Ensure your `count` function correctly counts occurrences of ``um'' as a word, surrounded by spaces or punctuation.

## Example Implementation

\begin{lstlisting}[language=Python]
import re

def count(text):
return len(re.findall(r'\bum\b', text, re.IGNORECASE))
\end{lstlisting}

## Contributing

Feel free to open issues or submit pull requests for improvements or bugfixes.

## License

This project is licensed under the MIT License.

## Contact

For questions or suggestions, please contact <your.email@example.com>.

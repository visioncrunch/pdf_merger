
---

# PDF Merger

This Python script merges multiple PDF files located in a specified folder into a single PDF file. It utilizes the PyPDF2 library for PDF manipulation.

## Features

- Merge multiple PDF files into one.
- Customizable source folder and output file path.
- Supports sorting of PDF files in ascending order for desired page sequence.
- Simple and easy-to-use script.

## Getting Started

### Prerequisites

- Python 3 installed on your system.
- PyPDF2 library installed. You can install it via pip:

    ```bash
    pip install PyPDF2
    ```

### Usage

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/your-username/pdf-merger.git
    ```

2. Navigate to the project directory:

    ```bash
    cd pdf-merger
    ```

3. Open the `pdf_merger.py` script in your preferred text editor.

4. Modify the `SOURCE_FOLDER` and `OUTPUT_FILE` variables at the top of the script to specify the source folder containing the PDF files to be merged and the desired output file path, respectively.

5. Save the changes to the script.

6. Run the script:

    ```bash
    python pdf_merger.py
    ```

7. The merged PDF file will be generated at the specified output file path.

## Notes

- Ensure that the PDF files in the source folder are named in a way that reflects the desired order of pages in the merged PDF.
- For best results, it's recommended to sort the PDF files in ascending order in the file explorer before running the script.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request with any improvements or suggestions.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This script was inspired by the need to efficiently merge multiple PDF files into one for various purposes.

---

Feel free to customize this README further to suit your project's specific requirements or style preferences. Let me know if you need any further assistance!

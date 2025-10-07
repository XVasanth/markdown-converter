# Markdown to PDF Converter

A simple web application built with Streamlit and Pandoc to convert Markdown (`.md`) files into high-quality PDFs.

## 🚀 Features

-   Select a folder on your local machine.
-   Lists all `.md` files found in the folder.
-   Option to "Select All" or choose specific files.
-   Converts selected files to PDF and saves them in an `output_pdfs` sub-directory.
-   Provides direct download links for the generated PDFs.

## ⚠️ Prerequisites

This application relies on external command-line tools. You **must** install them before running the app.

1.  **Python 3.8+**: Make sure you have a modern version of Python installed.

2.  **Pandoc**: The core conversion engine.
    -   **Installation Guide:** [pandoc.org/installing.html](https://pandoc.org/installing.html)

3.  **LaTeX Distribution**: Pandoc uses LaTeX to create PDFs. This is a large but necessary installation.
    -   **Windows**: [MiKTeX](https://miktex.org/download)
    -   **macOS**: [MacTeX](https://www.tug.org/mactex/)
    -   **Linux (Debian/Ubuntu)**: `sudo apt-get install texlive-full`

## ⚙️ How to Run Locally

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/your-username/markdown-converter.git](https://github.com/your-username/markdown-converter.git)
    cd markdown-converter
    ```

2.  **Create a Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install Python Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Streamlit App:**
    ```bash
    streamlit run app.py
    ```

Your web browser should open with the application running!

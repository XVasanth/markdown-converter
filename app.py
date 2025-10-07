# app.py

import streamlit as st
import pypandoc
import os
from pathlib import Path

# --- Page Configuration ---
st.set_page_config(
    page_title="MD to PDF Converter",
    page_icon="📄",
    layout="centered"
)

# --- Functions ---
def convert_to_pdf(md_file_path, output_folder):
    """Converts a single Markdown file to PDF using Pandoc."""
    try:
        output_filename = md_file_path.stem + ".pdf"
        output_path = output_folder / output_filename
        
        # Using xelatex for better Unicode/emoji support
        pypandoc.convert_file(
            str(md_file_path),
            'pdf',
            outputfile=str(output_path),
            extra_args=['--pdf-engine=xelatex']
        )
        return True, output_path
    except Exception as e:
        st.error(f"Error converting {md_file_path.name}: {e}")
        st.info("Please ensure Pandoc and a LaTeX distribution (like MiKTeX or TeX Live) are installed and in your system's PATH.")
        return False, None

# --- UI Layout ---
st.title("Markdown to PDF Converter 🚀")
st.write("Select a folder containing your Markdown (`.md`) files to convert them to PDF.")

# --- Prerequisite Information ---
with st.expander("⚠️ Important Prerequisites"):
    st.warning(
        """
        This app requires **Pandoc** and a **LaTeX** distribution to be installed on your system.
        
        1.  **Install Pandoc:** [pandoc.org/installing.html](https://pandoc.org/installing.html)
        2.  **Install LaTeX:** - **Windows:** [MiKTeX](https://miktex.org/download)
            - **macOS:** [MacTeX](https://www.tug.org/mactex/)
            - **Linux:** `sudo apt-get install texlive-full` (or similar for your distro)
        """
    )


# --- Folder Selection ---
folder_path_str = st.text_input(
    "Enter the path to the folder containing your Markdown files:",
    key="folder_path"
)

if folder_path_str:
    folder_path = Path(folder_path_str)
    
    # Check if the path is a valid directory
    if folder_path.is_dir():
        st.success(f"Valid folder selected: `{folder_path}`")
        
        # Find all Markdown files
        md_files = sorted(list(folder_path.glob("*.md")))
        
        if not md_files:
            st.warning("No Markdown (`.md`) files found in this folder.")
        else:
            st.markdown("---")
            st.subheader("Select Files to Convert")
            
            # File selection logic
            select_all = st.checkbox("Select All Files")
            
            if select_all:
                selected_files = md_files
            else:
                selected_files = st.multiselect(
                    "Choose Markdown files:",
                    options=md_files,
                    format_func=lambda file: file.name
                )
                
            # --- Conversion Button & Logic ---
            if st.button("Convert to PDF", type="primary"):
                if not selected_files:
                    st.error("Please select at least one file to convert.")
                else:
                    output_folder = folder_path / "output_pdfs"
                    output_folder.mkdir(exist_ok=True)
                    
                    st.markdown("---")
                    st.subheader("Conversion Progress & Results")
                    
                    progress_bar = st.progress(0)
                    total_files = len(selected_files)
                    
                    for i, file_path in enumerate(selected_files):
                        with st.spinner(f"Converting `{file_path.name}`..."):
                            success, pdf_path = convert_to_pdf(file_path, output_folder)
                        
                        if success:
                            st.success(f"Successfully converted `{file_path.name}`")
                            with open(pdf_path, "rb") as f:
                                st.download_button(
                                    label=f"Download `{pdf_path.name}`",
                                    data=f,
                                    file_name=pdf_path.name,
                                    mime="application/pdf"
                                )
                        
                        progress_bar.progress((i + 1) / total_files)

    else:
        st.error("The provided path is not a valid folder. Please check it and try again.")

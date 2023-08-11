import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path
import os

# Define the pattern to match the filenames
file_pattern = 'invoices/*.xlsx'

# Create a new folder
output_folder = "PDF Files"
os.makedirs(output_folder, exist_ok=True)

# Use glob to get a list of filenames matching the pattern
file_list = glob.glob(file_pattern)

# Loop through the filenames and read them into DataFrames
for file in file_list:
    df = pd.read_excel(file, sheet_name="Sheet 1")

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(auto=False, margin=0)
    pdf.add_page()
    filename = Path(file).stem
    invoice_nr = filename.split("-")[0]
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice nr.{invoice_nr}")

    # Save the pdf to a file
    pdf_output = os.path.join(output_folder, f'{filename}.pdf')
    pdf.output(pdf_output)

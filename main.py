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
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(auto=False, margin=0)
    pdf.add_page()

    filename = Path(file).stem
    invoice_nr, date = filename.split("-")

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice nr.{invoice_nr}", ln=1)

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Date:{date}", ln=1)

    df = pd.read_excel(file, sheet_name="Sheet 1")

    # Add a header
    pdf.set_font(family="Times", size=10, style="B")
    columns = df.columns
    columns = [item.replace("_", " ").title() for item in columns]
    pdf.cell(w=30, h=8, txt=columns[0], border=1)
    pdf.cell(w=50, h=8, txt=columns[1], border=1)
    pdf.cell(w=30, h=8, txt=columns[2], border=1)
    pdf.cell(w=30, h=8, txt=columns[3], border=1)
    pdf.cell(w=30, h=8, txt=columns[4], border=1, ln=1)

    # Add rows to the table
    for index, row in df.iterrows():
        pdf.set_font(family="Times", size=10)
        pdf.set_text_color(80, 80, 80)

        pdf.cell(w=30, h=8, txt=str(row["product_id"]), border=1)
        pdf.cell(w=50, h=8, txt=str(row["product_name"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["amount_purchased"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["total_price"]), border=1, ln=1)

    # Save the pdf to a file
    pdf_output = os.path.join(output_folder, f'{filename}.pdf')
    pdf.output(pdf_output)

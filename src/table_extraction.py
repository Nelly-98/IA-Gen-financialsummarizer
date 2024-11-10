import camelot

def extract_tables(pdf_path):
    tables = camelot.read_pdf(pdf_path, pages="all")
    return [table.df for table in tables]
import os

def save_summary_to_file(summary, filename="summary.txt"):
    with open(filename, "w") as file:
        file.write(summary)

def load_sample_documents(path="data/sample_reports/"):
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith(('.pdf', '.docx'))]

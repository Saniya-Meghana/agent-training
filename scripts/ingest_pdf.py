import sys
from app.services.ingest import build_index_from_pdf

if __name__ == '__main__':
    pdf_path = sys.argv[1]
    build_index_from_pdf(pdf_path)

from fastapi import APIRouter, UploadFile, File
from app.services.ingest import build_index_from_pdf

router = APIRouter()

@router.post("/pdf")
async def ingest_pdf(file: UploadFile = File(...)):
    contents = await file.read()
    temp_path = f"/tmp/{file.filename}"
    with open(temp_path, "wb") as f:
        f.write(contents)

    index, chunks = build_index_from_pdf(temp_path)
    os.remove(temp_path)

    return {"message": f"Indexed {len(chunks)} chunks from {file.filename}"}

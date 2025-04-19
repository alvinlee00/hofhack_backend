# src/agent/webapp.py
from fastapi import FastAPI, UploadFile, File, HTTPException
import os

UPLOAD_DIR = "uploads"
app = FastAPI()
       # mounts all of LG’s /runs, /assistants, etc.
@app.get("/hello")
def hello():
    return {"msg": "world"}

@app.get("/")
def read_root():
    return {"message": "Hello World"}


# @app.post("/upload-pdf")
# async def upload_pdf(pdf: UploadFile = File(...)):
#     # 1. Validate content type
#     if pdf.content_type != "application/pdf":
#         raise HTTPException(status_code=400, detail="Only PDF files allowed")

#     # 2. Stream the file to disk in chunks (avoid loading whole file in memory)
#     dest = os.path.join(UPLOAD_DIR, pdf.filename)
#     try:
#         with open(dest, "wb") as buffer:
#             while chunk := await pdf.read(1024 * 1024):  # 1MB chunks
#                 buffer.write(chunk)
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Failed to save file: {e}")

#     # 3. Return whatever you like back to the client
#     return {"filename": pdf.filename, "size_bytes": os.path.getsize(dest)}


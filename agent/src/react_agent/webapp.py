# src/agent/webapp.py
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os

UPLOAD_DIR = "uploads"
app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins=["https://localhost:3000"],
  allow_methods=["POST", "GET", "OPTIONS"],
  allow_headers=["*"],
  allow_credentials=True,
)
       # mounts all of LG’s /runs, /assistants, etc.
@app.get("/hello")
def hello():
    return {"msg": "world"}

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.post("/upload-pdf")
async def upload_pdf(pdf: UploadFile = File(...)):
    print("uploading pdf now")
    try:
        contents = await pdf.read()
        save_path = os.path.join(UPLOAD_DIR, pdf.filename)
        with open(save_path, "wb") as f:
            f.write(contents)
        return {"filename": pdf.filename, "size": len(contents)}
    except Exception as e:
        # print the real exception to your console
        import traceback; traceback.print_exc()
        # return a controlled 500 with detail
        raise HTTPException(status_code=500, detail=str(e))


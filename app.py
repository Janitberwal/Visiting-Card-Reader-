from fastapi import FastAPI, UploadFile, File, Body # Added Body here
from fastapi.responses import FileResponse          # Added FileResponse here
from ocr.reader import extract_raw_text
import os
import shutil
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# cross-origin resource sharing 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Card reader API is running"}

@app.post("/extract")
async def upload_card(file: UploadFile = File(...)):
    # ensure directory exists
    os.makedirs("data/samples", exist_ok=True)
    
    # save the file first 
    temp_path = f"data/samples/{file.filename}"
    with open(temp_path , "wb") as buffer:
        shutil.copyfileobj(file.file , buffer)
        
    # extract text from image 
    data = extract_raw_text(temp_path)

    # return json results for frontend to review/edit
    return {
        "filename": file.filename,
        "status": "success",
        "data": data
    }

# save to excel endpoint 
@app.post("/save")
async def save_data(payload: dict = Body(...)):
    """
    Receives edited data from React and saves to Excel.
    """
    try:
        from database_manager import save_to_excel
        # The payload contains the edited data from your React form
        success = save_to_excel(payload)
        
        if success:
            return {"status": "success", "message": "Data saved to Excel"}
        else:
            return {"status": "error", "message": "Failed to write to Excel"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

# FEATURE 3: Download Excel
@app.get("/download-excel")
async def download_excel():
    excel_path = "data/extracted/business_cards.xlsx"
    if os.path.exists(excel_path):
        return FileResponse(path=excel_path, filename="business_cards.xlsx")
    return {"error": "File not found"}
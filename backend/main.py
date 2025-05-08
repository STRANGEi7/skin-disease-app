from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
from predict import predict_disease
from suggestions import get_suggestions
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Security ke liye baad me isse specific domain karna
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# # Serve uploaded images
# app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

# # Serve static files (like favicon)
# app.mount("/static", StaticFiles(directory="static"), name="static")

# @app.get("/")
# async def root():
#     return {"message": "Welcome to the Skin Disease Recognition API!"}

# @app.get("/favicon.ico")
# async def favicon():
#     # Adjust path to your favicon file
#     favicon_path = os.path.join("static", "favicon.ico")
#     return FileResponse(favicon_path)

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # Save the uploaded file
    with open(f"uploads/{file.filename}", "wb") as f:
        f.write(await file.read())
    
    # Get prediction result
    disease_name = predict_disease(f"uploads/{file.filename}")
    
    # Get suggestions if needed
    suggestion = get_suggestions(disease_name)
    
    return JSONResponse(content={"disease": disease_name, "suggestion": suggestion})

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)



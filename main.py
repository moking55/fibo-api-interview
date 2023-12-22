from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Fibonacci API",
    version="1.0.0",
    summary="API to calculate fibonacci sequence",
    docs_url="/docs",
    redoc_url="/redoc"
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/v1/fibo/{number}", response_model=dict,description="Calculate fibonacci sequence")
async def fibo(number: int):
    if number < 0:
        raise HTTPException(status_code=400, detail="Number must be positive")
    if number > 100 or number == 0:
        raise HTTPException(status_code=400, detail="Number must be between 1 and 100")
    
    fibo_list = [0, 1]
    for i in range(2, number):
        fibo_list.append(fibo_list[i - 1] + fibo_list[i - 2])
    
    return JSONResponse(status_code=200, content={
        "member-count": len(fibo_list),
        "sequence": fibo_list,
        "total": sum(fibo_list),
    })

from fastapi import FastAPI, HTTPException
from fastembed.embedding import FlagEmbedding as Embedding
from pydantic import BaseModel
from typing import List

app = FastAPI()
embedding_model = Embedding(model_name="BAAI/bge-small-en-v1.5", max_length=512)


class InputModel(BaseModel):
    inputs: str

class InputModelBatch(BaseModel):
    inputs: List[str]

@app.post("/embed")
def read_item(request: InputModel):
    try:
        input = request.inputs
        if(len(input) > 512):
            raise HTTPException(status_code=400, detail="Max chunk length is 512")
        embeddings = list(embedding_model.embed(request.inputs))
        return {
            "embeddings": embeddings[0].tolist()
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@app.post("/embed-batch")
def read_item(request: InputModelBatch):
    try:
        inputs = request.inputs
        
        if len(inputs) > 500:
            raise HTTPException(status_code=400, detail="Max batch size is 100")
        
        for i in inputs:
            if(len(i)) > 512:
                raise HTTPException(status_code=400, detail="Max chunk length is 512")
        
        embeddings = list(embedding_model.embed(request.inputs))
        print(len(embeddings))
        
        return {
            "embeddings": [e.tolist() for e in embeddings]
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080)

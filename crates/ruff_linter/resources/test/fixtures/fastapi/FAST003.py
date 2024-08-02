from fastapi import FastAPI

app = FastAPI()


# Errors

@app.get("/things/{thing_id}")
async def read_thing(query: str):
    return {"query": query}

@app.get("/books/isbn-{isbn}")
async def read_thing():
    ...



# OK


@app.get("/things/{thing_id}")
async def read_thing(thing_id: int, query: str):
    return {"thing_id": thing_id, "query": query}

@app.get("/books/isbn-{isbn}")
async def read_thing(isbn: str):
    return {"isbn": isbn}


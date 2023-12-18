"""
This is the main script where Fast API application is initialized and routes are registered.
"""
import gc

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from scripts.services.mongodb_structure_services import setUp

gc.collect()

tags_meta = [{"name": "FastAPI Structure Service", "description": "API to Update DATA"}]
app = FastAPI(
    title="FastAPI Service",
    version="v1.0",
    description="Service",
    openapi_tags=tags_meta
)

app.include_router(setUp)

# allow_origins * indicates to access the code for all the domain

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

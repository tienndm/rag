"""
Extensions for Entrypoint Layer.

This module provides utility functions to integrate FastAPI exception handlers with the application's
domain-specific exceptions. It ensures that custom errors in the domain layer are transformed into appropriate
HTTP responses when they propagate to the HTTP layer.

Note:
    For simpler requirements, use extension.py. For more complex needs, consider extensions/$package.py for better clarity and scalability.
"""

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from models.exception import RagError, RagUnknownError, RagNotFound


def addExceptionHandler(app: FastAPI):
    @app.exception_handler(RagUnknownError)
    @app.exception_handler(RagError)
    async def handleGeneralRagError(_, exc):
        return JSONResponse(
            content={
                "code": 400,
                "description": "error",
                "data": {},
            },
            status_code=400,
        )

    @app.exception_handler(RagNotFound)
    async def handleRagNotFoundError(_, exc):
        return JSONResponse(
            content={
                "code": 404,
                "description": "not found",
                "data": {},
            },
            status_code=404,
        )

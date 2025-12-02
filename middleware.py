from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def setup_middleware(app: FastAPI) -> None:
    """
    Configure all middleware for the FastAPI application.
    
    Args:
        app: FastAPI application instance
    """
    # CORS Middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Update this in production with specific origins
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # Add other middleware here as needed
    # Example: Trusted host middleware, GZip middleware, etc.

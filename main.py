import os
from fastapi import FastAPI
from config import settings
from middleware import setup_middleware

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def create_app() -> FastAPI:
    """
    Application factory function that creates and configures the FastAPI application.
    
    Returns:
        FastAPI: Configured FastAPI application instance
    """
    # Initialize FastAPI app
    app = FastAPI(
        title=settings.app_name,
        description=settings.app_description,
        version=settings.app_version
    )
    
    # Setup middleware
    setup_middleware(app)
    
    # Register routes
    register_routes(app)
    
    return app


def register_routes(app: FastAPI) -> None:
    """
    Register all application routes.
    
    Args:
        app: FastAPI application instance
    """
    @app.get("/", tags=["General"])
    async def root():
        """Root endpoint - API welcome message"""
        return {
            "message": f"Welcome to {settings.app_name}",
            "version": settings.app_version,
            "docs": "/docs",
            "health": "/health"
        }

    @app.get("/.well-known/jwks.json", tags=["General"])
    async def get_jwks():
        jwks_path = os.path.join(BASE_DIR, "jwks.json")
        return FileResponse(jwks_path, media_type="application/json")

    
    @app.get("/health", tags=["General"])
    async def health_check():
        """Health check endpoint - Returns API health status"""
        return {
            "status": "healthy",
            "version": settings.app_version,
            "service": settings.app_name
        }
    
    @app.get("/info")
    async def system_info():
        """System information endpoint"""
        import platform
        import sys
        return {
            "app_name": settings.app_name,
            "app_version": settings.app_version,
            "python_version": sys.version,
            "platform": platform.platform(),
            "host": settings.host,
            "port": settings.port
        }
    

    # Import and include routers here
    # Example: app.include_router(patient_router, prefix="/api/v1/patients", tags=["patients"])


# Create the app instance
app = create_app()

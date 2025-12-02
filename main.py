from fastapi import FastAPI
from config import settings
from middleware import setup_middleware


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
    
    @app.get("/health", tags=["General"])
    async def health_check():
        """Health check endpoint - Returns API health status"""
        return {
            "status": "healthy",
            "version": settings.app_version,
            "service": settings.app_name
        }
    
    @app.get("/info", tags=["General"])
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
    
    # Patient endpoints
    @app.get("/api/v1/patients", tags=["Patients"])
    async def get_patients(skip: int = 0, limit: int = 10):
        """Get list of patients with pagination"""
        # TODO: Replace with actual database query
        sample_patients = [
            {"id": 1, "name": "John Doe", "age": 30, "email": "john@example.com"},
            {"id": 2, "name": "Jane Smith", "age": 25, "email": "jane@example.com"},
        ]
        return {
            "total": len(sample_patients),
            "skip": skip,
            "limit": limit,
            "patients": sample_patients[skip:skip+limit]
        }
    
    @app.get("/api/v1/patients/{patient_id}", tags=["Patients"])
    async def get_patient(patient_id: int):
        """Get a specific patient by ID"""
        # TODO: Replace with actual database query
        sample_patient = {
            "id": patient_id,
            "name": "John Doe",
            "age": 30,
            "email": "john@example.com",
            "phone": "+1234567890",
            "address": "123 Main St, City, State"
        }
        return sample_patient
    
    @app.post("/api/v1/patients", tags=["Patients"], status_code=201)
    async def create_patient(patient_data: dict):
        """Create a new patient record"""
        # TODO: Validate and save to database
        return {
            "message": "Patient created successfully",
            "patient": {
                "id": 123,  # This would be auto-generated
                **patient_data
            }
        }
    
    @app.put("/api/v1/patients/{patient_id}", tags=["Patients"])
    async def update_patient(patient_id: int, patient_data: dict):
        """Update an existing patient record"""
        # TODO: Update in database
        return {
            "message": f"Patient {patient_id} updated successfully",
            "patient": {
                "id": patient_id,
                **patient_data
            }
        }
    
    @app.delete("/api/v1/patients/{patient_id}", tags=["Patients"])
    async def delete_patient(patient_id: int):
        """Delete a patient record"""
        # TODO: Delete from database
        return {
            "message": f"Patient {patient_id} deleted successfully"
        }
    
    # Import and include routers here
    # Example: app.include_router(patient_router, prefix="/api/v1/patients", tags=["patients"])


# Create the app instance
app = create_app()

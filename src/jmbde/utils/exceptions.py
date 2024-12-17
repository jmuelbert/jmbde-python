"""Custom exceptions for the JMBDE application."""

class ApplicationError(Exception):
    """Base exception for application-specific errors."""
    pass

class ConfigurationError(ApplicationError):
    """Raised when there's a configuration error."""
    pass

class DatabaseError(ApplicationError):
    """Raised when there's a database-related error."""
    pass
    
class ModelError(ApplicationError):
    """Raised when there's a model-related error."""
    pass

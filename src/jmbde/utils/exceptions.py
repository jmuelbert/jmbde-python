"""Custom exceptions for the JMBDE application."""


class ApplicationError(Exception):
    """Base exception for application-specific errors."""


class ConfigurationError(ApplicationError):
    """Raised when there's a configuration error."""


class DatabaseError(ApplicationError):
    """Raised when there's a database-related error."""


class ModelError(ApplicationError):
    """Raised when there's a model-related error."""

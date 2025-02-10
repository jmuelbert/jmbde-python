"""Custom exceptions for the JMBDE application."""


class ApplicationError(Exception):
    """
    Base exception for application-specific errors.

    class ApplicationError(Exception):

    Custom exception class for application-related errors.

    def __init__(self, message: str, *args: Exception) -> None:

        Initialize ApplicationError with a message and optional arguments.

    Args:
            message (str): Error message to be displayed.
            *args (Exception): Optional arguments for additional context.
                super().__init__(message, *args)

    """


class ConfigurationError(ApplicationError):
    """Raised when there's a configuration error."""


class DatabaseError(ApplicationError):
    """Raised when there's a database-related error."""


class ModelError(ApplicationError):
    """Raised when there's a model-related error."""

class DeenAPIError(Exception):
    """Base exception for Deen API client"""
    pass

class AuthenticationError(DeenAPIError):
    """Raised when API key is invalid or missing"""
    pass

class RateLimitError(DeenAPIError):
    """Raised when rate limit is exceeded"""
    pass

class NotFoundError(DeenAPIError):
    """Raised when resource is not found"""
    pass

class ServerError(DeenAPIError):
    """Raised when server returns 5xx error"""
    pass
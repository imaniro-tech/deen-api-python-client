import requests
from typing import List, Optional, Dict, Any
from datetime import datetime
from .models import Hadith, APIResponse
from .exceptions import *

class ImaniroDeenAPIClient:
    def __init__(self, api_key: str, base_url: str = "https://deen-api.imaniro.com/api/v1"):
        self.api_key = api_key
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json',
            'X-API-Key': self.api_key
        })
    
    def _handle_response(self, response: requests.Response) -> Dict[str, Any]:
        """Handle API response and raise appropriate exceptions"""
        if response.status_code == 401:
            raise AuthenticationError("Invalid API key")
        elif response.status_code == 402:
            raise InsufficientBalanceError("Insufficient balance to process request")
        elif response.status_code == 404:
            raise NotFoundError("Resource not found")
        elif response.status_code == 429:
            raise RateLimitError("Rate limit exceeded")
        elif response.status_code >= 500:
            raise ServerError("Server error occurred")
        elif response.status_code != 200:
            raise DeenAPIError(f"API error: {response.status_code} - {response.text}")
        
        return response.json()
    
    def _make_request(self, endpoint: str, params: Optional[Dict] = None) -> APIResponse:
        """Make API request and return parsed response"""
        url = f"{self.base_url}/{endpoint}"
        
        try:
            response = self.session.post(url, json=params or {})
            data = self._handle_response(response)
            return APIResponse.from_dict(data)
        except requests.exceptions.RequestException as e:
            raise DeenAPIError(f"Request failed: {str(e)}")  
 
    def get_hadiths(
        self, 
        book: Optional[str] = None,
        hadith_number: Optional[str] = None,
        narrator: Optional[str] = None,
        category: Optional[str] = None,
        authenticity: Optional[str] = None,
        language: str = "English",  # Default to English, still allows override
        max_limit: int = 1,
        **kwargs
    ) -> List[Hadith]:
        """
        Get hadiths based on specified criteria
        
        Args:
            book: Name of the hadith book (e.g., "Sahih al-Bukhari")
            hadith_number: Specific hadith number
            narrator: Name of the narrator
            category: Category or topic of the hadith (e.g., prayer, fasting)
            authenticity: Classification of the hadith (e.g., Sahih, Daif)
            language: Language of the hadith (default: "English")
            max_limit: Maximum number of hadiths to return (default: 1, max: 500)
            **kwargs: Additional parameters for the API
        
        Returns:
            List of Hadith objects matching the criteria
        """
        # Validate max_limit
        if max_limit > 500:
            raise ValueError("max_limit cannot exceed 500")
        if max_limit < 1:
            raise ValueError("max_limit must be at least 1")
        
        # Build params dictionary only with provided values
        params = {}
        
        # Only add optional fields if they have non-None values
        if book is not None:
            params["book"] = book
        if hadith_number is not None:
            params["hadithNumber"] = hadith_number
        if narrator is not None:
            params["narrator"] = narrator
        if category is not None:
            params["category"] = category
        if authenticity is not None:
            params["authenticity"] = authenticity
        
        # Always include language (since it has a default) and max_limit
        params["language"] = language
        params["maxLimit"] = max_limit
        
        # Add any additional kwargs
        params.update(kwargs)
        
        response = self._make_request("hadiths", params)
        return [Hadith.from_dict(item) for item in response.data]
    
    def check_status(self) -> Dict[str, Any]:
        """Check API status"""
        url = f"{self.base_url}/status"
        
        try:
            response = self.session.get(url)
            if response.status_code == 200:
                return response.json()
            else:
                raise DeenAPIError(f"Status check failed: {response.status_code}")
        except requests.exceptions.RequestException as e:
            raise DeenAPIError(f"Status check request failed: {str(e)}")
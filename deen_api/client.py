import requests
from typing import List, Optional, Dict, Any
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
 
    def get_hadiths(self, book: str = '', 
                    max_limits: int = 1, 
                    number:str = '', 
                    language:str = 'en', 
                    authenticity:str = '', 
                    keywords: List[str] = [],
                    topics: List[str] = [],
                    narrator:str = '',
                    **kwargs) -> List[Hadith]:
        """
        Get hadiths from specified book
        
        Args:
            book: Name of the hadith book (e.g., "Sahih al-Bukhari")
            max_limits: Maximum number of hadiths to return
            **kwargs: Additional parameters for the API
        
        Returns:
            List of Hadith objects
        """
        params = {
            "book": book,
            "number" : number,
            "narrator": narrator,
            "language": language,
            "authenticity": authenticity,
            "keywords": keywords,
            "topics": topics,
            "maxLimits": max_limits,
            **kwargs
        }
        
        response = self._make_request("hadiths", params)
        return [Hadith.from_dict(item) for item in response.data]
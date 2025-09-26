import pytest
import requests_mock
from deen_api import ImaniroDeenAPIClient, Hadith
from deen_api.exceptions import AuthenticationError, NotFoundError

class TestDeenAPIClient:
    def setup_method(self):
        self.api_key = "test_key"
        self.client = ImaniroDeenAPIClient(api_key=self.api_key)
        self.base_url = "https://deen-api.imaniro.com/api/v1"
    
    def test_authentication_error(self):
        with requests_mock.Mocker() as m:
            m.post(f"{self.base_url}/hadiths", status_code=401)
            
            with pytest.raises(AuthenticationError):
                self.client.get_hadiths(book="Sahih al-Bukhari")
    
    def test_get_hadiths_success(self):
        mock_response = {
            "success": True,
            "data": [
                {
                    "book": "Sahih al-Bukhari",
                    "number": "1",
                    "narratedBy": "Abu Huraira",
                    "translation": "Hadith translation...",
                    "attribution": "Marfu",
                    "authenticity": "sahih",
                    "category": "Prayer",
                    "context": "Hadith Context...",
                    "explanation": "hadith Explanation...",
                    "hadith": "الكَعْبَةَ وَأُسَامَةُ"
                }
            ],
            "message": "Success",
            "count": 1
        }
        
        with requests_mock.Mocker() as m:
            m.post(f"{self.base_url}/hadiths", json=mock_response)
            
            hadiths = self.client.get_hadiths(book="Sahih al-Bukhari")
            
            assert len(hadiths) == 1
            assert isinstance(hadiths[0], Hadith)
            assert hadiths[0].book == "Sahih al-Bukhari"
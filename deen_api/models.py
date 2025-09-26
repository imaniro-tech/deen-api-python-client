from typing import List, Optional, Dict, Any
from dataclasses import dataclass

@dataclass
class Hadith:
    attribution: str
    authenticity: str
    category: str
    context: str
    explanation: str
    hadith: str
    narratedBy: str
    book: str
    number: str
    translation: str

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Hadith':
        return cls(
                attribution = data.get('attribution', ''),
                authenticity = data.get('authenticity', ''),
                category = data.get('category', ''),
                context = data.get('context', ''),
                explanation = data.get('explanation', ''),
                hadith = data.get('hadith', ''),
                narratedBy = data.get('narratedBy', ''),
                book=data.get('book', ''),
                number = data.get('number', ''),
                translation=data.get('translation', '')
        )

@dataclass
class APIResponse:
    success: bool
    data: List[Any]
    message: str
    count: int
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'APIResponse':
        return cls(
            success=data.get('success', False),
            data=data.get('data', []),
            message=data.get('message', ''),
            count=data.get('count', 0)
        )
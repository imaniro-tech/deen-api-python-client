# Deen API Python Client

A Python client for the Deen API, providing easy access to Islamic resources including Hadith, Quran verses, and Duas.

## Installation

```bash
pip install deen-api-client
```

# Quick Start

```python
from deen_api import ImaniroDeenAPIClient

# Initialize client with your API key
client = ImaniroDeenAPIClient(api_key="sk_12345")

# Get hadiths from Sahih al-Bukhari
hadiths = client.get_hadiths(book="Sahih al-Bukhari", max_limits=5)

for hadith in hadiths:
    print(f"Book: {hadith.book}")
    print(f"Chapter: {hadith.chapter}")
    print(f"Text: {hadith.text}")
    print(f"Translation: {hadith.translation}")
    print("---")

# Get Quran verses
verses = client.get_quran_verses(surah="Al-Fatiha", max_limits=3)

# Get Duas
duas = client.get_duas(category="morning", max_limits=5)
```

# Features

- Hadith Access: Retrieve hadiths from various books

- Quran Verses: Access Quranic verses with translations(under development)

- Islamic Duas: Get supplications for various occasions(under development)

- Error Handling: Comprehensive exception handling

# Error Handling

The client provides specific exception types:

```python
from deen_api import AuthenticationError, RateLimitError, NotFoundError

try:
    hadiths = client.get_hadiths(book="Sahih al-Bukhari")
except AuthenticationError:
    print("Invalid API key")
except RateLimitError:
    print("Rate limit exceeded")
except NotFoundError:
    print("Resource not found")
```

## Example Usage Files

### `examples/hadith_example.py`

```python
from deen_api import ImaniroDeenAPIClient

def hadith_example():
    client = ImaniroDeenAPIClient(api_key="sk_12345")

    try:
        # Get hadiths from Sahih al-Bukhari
        hadiths = client.get_hadiths(book="Sahih al-Bukhari", max_limits=3)

        print("Hadiths from Sahih al-Bukhari:")
        for i, hadith in enumerate(hadiths, 1):
            print(f"\n{i}. {hadith.hadith}")
            print(f"Translation: {hadith.translation}")
            print("-" * 50)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    hadith_example()
```

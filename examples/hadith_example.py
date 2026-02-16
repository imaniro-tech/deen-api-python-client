from deen_api import ImaniroDeenAPIClient

def hadith_example():
    client = ImaniroDeenAPIClient(api_key="sk_12345")
    
    try:
        # Get hadiths from Sahih al-Bukhari
        hadiths = client.get_hadiths(book="Sahih al-Bukhari", hadith_number='52', max_limit=1)
        
        print("Hadiths from Sahih al-Bukhari:")
        for i, hadith in enumerate(hadiths, 1):
            print(f"\n{i}. {hadith.hadith}")
            print(f"Translation: {hadith.translation}")
            print("-" * 50)
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    hadith_example()
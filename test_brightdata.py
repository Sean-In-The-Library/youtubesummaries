from brightdata_scrapper import trigger_scraping_channels
from dotenv import load_dotenv
import os

# Force reload of environment variables
load_dotenv(override=True)

def test_bright_data_api():
    api_key = os.getenv("BRIGHT_DATA_API_KEY")
    print(f"Testing Bright Data API with key: {api_key}")
    
    # Test with a single YouTube channel
    test_channel = ["https://www.youtube.com/@OpenAI"]
    
    try:
        result = trigger_scraping_channels(
            api_key=api_key,
            channel_urls=test_channel,
            num_of_posts=1,  # Just get 1 post for testing
            start_date="2024-01-01",
            end_date="2024-12-31",
            order_by="Latest",
            country=""
        )
        
        if result is None:
            print("Error: API call failed. Check your API key and network connection.")
            return
            
        print("\nAPI Response:")
        print(result)
        print("\nTest completed successfully!")
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")

if __name__ == "__main__":
    test_bright_data_api()

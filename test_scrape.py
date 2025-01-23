import os
import time
from datetime import datetime, timedelta
from brightdata_scrapper import trigger_scraping_channels, get_output
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key from environment
api_key = os.getenv('BRIGHT_DATA_API_KEY')

# Test channel URL (using full URL format)
channel_urls = ["https://www.youtube.com/channel/UCBa659QWEk1AI4Tg--mrJ2A"]  # Tom Scott's channel ID

# Set up minimal parameters
num_of_posts = 5

print("Starting scraping test...")

# Trigger scraping with minimal parameters
response = trigger_scraping_channels(
    api_key=api_key,
    channel_urls=channel_urls,
    num_of_posts=num_of_posts,
    start_date=None,
    end_date=None,
    order_by=None,
    country=None
)

if response and 'snapshot_id' in response:
    snapshot_id = response['snapshot_id']
    print(f"\nGot snapshot ID: {snapshot_id}")
    
    # Try up to 30 times (5 minutes total)
    max_attempts = 30
    for attempt in range(max_attempts):
        print(f"\nAttempt {attempt + 1}/{max_attempts} to get data...")
        
        # Get the output
        output = get_output(api_key, snapshot_id)
        
        if output and len(output) > 0:
            print(f"\nReceived {len(output)} items:")
            for item in output:
                title = item.get('title', 'No title')
                url = item.get('url', 'No URL')
                views = item.get('views', 'No views')
                date = item.get('date_posted', 'No date')
                print(f"- {title}")
                print(f"  URL: {url}")
                print(f"  Views: {views}")
                print(f"  Posted: {date}")
            break
        else:
            if attempt < max_attempts - 1:
                print("No data yet, waiting 10 seconds...")
                time.sleep(10)
            else:
                print("No data received after all attempts")

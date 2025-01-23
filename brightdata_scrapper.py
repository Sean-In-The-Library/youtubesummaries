import subprocess
import json
import time
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("BRIGHT_DATA_API_KEY")

def trigger_scraping_niche(api_key, keyword, num_of_posts, start_date, end_date, country, endpoint):

    payload = [{"keyword": keyword, 
                "num_of_posts": num_of_posts, 
                "start_date": start_date, 
                "end_date": end_date, 
                "country": country}]

    # Define the curl command
    command = [
        "curl",
        "-H", f"Authorization: Bearer {api_key}",
        "-H", "Content-Type: application/json",
        "-d", json.dumps(payload),  # Convert payload to a JSON string
        endpoint
    ]

    # Execute the command and capture the output
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    # Check if the command was successful
    if result.returncode == 0:
        try:
            # Parse the JSON response
            return json.loads(result.stdout.strip())
        except json.JSONDecodeError:
            print("Failed to parse JSON response.")
            return None
    else:
        # Print the error if the command fails
        print(f"Error: {result.stderr}")
        return None

def trigger_scraping_channels(api_key, channel_urls, num_of_posts, start_date, end_date, order_by, country):
    print(f"Triggering scraping for channels: {channel_urls}")
    
    dataset_id = "gd_lk56epmy2i5g7lzu0k"
    endpoint = f"https://api.brightdata.com/datasets/v3/trigger?dataset_id={dataset_id}&include_errors=true&type=discover_new&discover_by=url"

    # Create payload with only required parameters
    payload = []
    for url in channel_urls:
        item = {
            "url": url,
            "num_of_posts": num_of_posts
        }
        payload.append(item)

    print(f"Using endpoint: {endpoint}")
    print(f"Payload: {json.dumps(payload, indent=2)}")

    # Define the curl command
    command = [
        "curl",
        "-H", f"Authorization: Bearer {api_key}",
        "-H", "Content-Type: application/json",
        "-d", json.dumps(payload),
        endpoint
    ]

    print(f"Executing command: {' '.join(command)}")
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    print(f"Command return code: {result.returncode}")
    print(f"Stderr output: {result.stderr}")
    print(f"Raw stdout: {result.stdout}")

    if result.returncode == 0:
        try:
            response = json.loads(result.stdout.strip())
            print(f"Parsed response: {json.dumps(response, indent=2)}")
            return response
        except json.JSONDecodeError as e:
            print(f"Failed to parse JSON response: {str(e)}")
            return None
    else:
        print(f"Error: {result.stderr}")
        return None

def get_progress(api_key, snapshot_id):
    command = [
        "curl",
        "-H", f"Authorization: Bearer {api_key}",
        f"https://api.brightdata.com/datasets/v3/progress/{snapshot_id}"
    ]

    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    if result.returncode == 0:
        return json.loads(result.stdout.strip())
    else:
        print(f"Error: {result.stderr}")
        return None

def get_output(api_key, snapshot_id, format="json"):
    print(f"Fetching output for snapshot: {snapshot_id}")
    
    # Define the curl command as a list
    command = [
        "curl",
        "-H", f"Authorization: Bearer {api_key}",
        f"https://api.brightdata.com/datasets/v3/snapshot/{snapshot_id}?format={format}"
    ]

    print(f"Executing command: {' '.join(command)}")
    
    # Use universal_newlines=False to get bytes output
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=False)

    print(f"Command return code: {result.returncode}")
    if result.stderr:
        print(f"Stderr output: {result.stderr.decode('utf-8', errors='ignore')}")
    
    if result.returncode == 0 and result.stdout:
        try:
            # Decode stdout with utf-8 and handle errors
            stdout_str = result.stdout.decode('utf-8', errors='ignore')
            
            # Try to parse the response
            response = json.loads(stdout_str.strip())
            
            # Check if it's a status message
            if isinstance(response, dict) and 'status' in response:
                if response['status'] == 'running':
                    print(f"Status: {response['status']} - {response.get('message', '')}")
                    return None
            
            # If we got here, we should have actual data
            if isinstance(response, list):
                print(f"Received {len(response)} items")
                return response
            elif isinstance(response, dict):
                print("Received single item response")
                return [response]
            else:
                print(f"Unexpected response format: {type(response)}")
                return None
                
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON: {str(e)}")
            print(f"Raw output was: {stdout_str[:500]}...")  # Show first 500 chars
            return None
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
            return None
    else:
        print(f"Request failed or empty response")
        return None

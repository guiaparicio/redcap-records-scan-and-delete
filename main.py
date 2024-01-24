from dotenv import load_dotenv
import requests
import os

load_dotenv()

redcap_api_url = os.environ.get("REDCAP_API_URL")
api_key        = os.environ.get("API_KEY")

print(redcap_api_url)

# SEARCH RECORDS
payload = {
    'token': api_key,
    'content': 'record',
    'format': 'json',
    'type': 'flat',
    'filterLogic': '[email] = "email@test.net"' # ALTER FILTER LOGIC
}

response = requests.post(redcap_api_url, data=payload)

if response.status_code == 200:
    
    data = response.json()

    if isinstance(data, list) and len(data) > 0:

        records = data

        for record in records:
            record_id = record.get('record_id')
            print(f"Record ID: {record_id}")

            # DELETE RECORD
            delete_payload = {
                'token': api_key,
                'content': 'record',
                'action': 'delete',
                'records[0]': record_id, 
            }

            delete_response = requests.post(redcap_api_url, data=delete_payload)

            if delete_response.status_code == 200:
                print(f"Record {record_id} deleted.")
            else:
                print(f"Error deleted: {record_id}. Status Code: {delete_response.status_code}")
                print(delete_response.text)
        
        total_records = len(records)
        print(f"\nRegisters: {total_records}")
    else:
        print("No register found.")
else:
    print(f"Request Error. Status Code: {response.status_code}")
    print(response.text)
# About
This project aims to search for records in a REDCap project based on certain filtering criteria and delete the record.

# .env

Alter .env file with your REDCAP configs.

```env

[REDCAP]
REDCAP_API_URL = 
API_KEY        = 

```

# FilterLogic
Alter the filterLogic, ex:

```python

'filterLogic': '[email] = "email@test.net"'

```
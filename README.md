# Nui Federation Python SDK

This SDK connects to the NUI Federation API for getting or creating, revoke, generating batch for NUI from the API.

## Installation

### Package Manager

```sh
pip install nui_federation_py_sdk
```

# Example

```py
from nui_federation_py_sdk import NUIFederation

# Initialize UINService with baseUrl and apiKey
base_url = "https://example.com/api"
api_key = "your-api-key"

nui_federation = NUIFederation(base_url=base_url, api_key=api_key)

# Example 1: Get or Create UIN
citizen_datas = [{
    "externalId": "123",
    "firstname": "John",
    "lastname": "Doe",
    "dateOfBirth": "2000-01-01",
    "birthCertificateId": "BC123",
    "motherName": "Jane Doe",
}]

try:
    response = nui_federation.uin.get_or_create_uin(citizen_datas)
    print("UIN Response:", response)
except Exception as e:
    print("Error creating or fetching UIN:", str(e))

# Example 2: Revoke a UIN
uin = "123456789"
try:
    revoke_response = nui_federation.uin.revoke_uin(uin)
    print("Revoke Response:", revoke_response)
except Exception as e:
    print("Error revoking UIN:", str(e))

# Example 3: Generate UIN Batch
count = 5
try:
    batch_response = nui_federation.uin.generate_uin_batch(count)
    print("Batch Response:", batch_response)
except Exception as e:
    print("Error generating UIN batch:", str(e))

```

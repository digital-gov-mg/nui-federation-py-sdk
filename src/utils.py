def validate_citizen_data(citizen_data):
    required_keys = [
        "externalId",
        "firstname",
        "lastname",
        "dateOfBirth",
        "birthCertificateId",
    ]
    for key in required_keys:
        if key not in citizen_data:
            raise ValueError(f"Missing required field: {key}")

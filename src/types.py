from typing import TypedDict, Optional


class CitizenData(TypedDict):
    externalId: str
    firstname: str
    lastname: str
    dateOfBirth: str
    birthCertificateId: str
    motherName: Optional[str]

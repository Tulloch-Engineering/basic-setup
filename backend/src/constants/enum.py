from enum import Enum


class ErrorResponse(Enum):
    ATTRIBUTE = "Attribute Error."
    CREDENTIALS = "Credential Error."
    CONNECTION = "Connection Error."
    DATA = "Data Error."
    DATABASE = "Database Error."
    DATABASE_KEY = "Error Database Key Invalid."
    FILE = "File Error"
    INVALID_CONTENTS = "Contents Invalid."
    INVALID_FILE = "Invalid File Parsing Error. Please check file type."
    PERMISSION = "Permission Error"
    PROVIDER = "Provider List Error."
    REQUEST = "Request Error."
    TENDERS = "Tender List Error."
    TIMEOUT = "Timeout Error."
    TYPE = "Type Error."
    UNKNOWN = "Unknown Error."
    VALIDATION = "Validation Error."
    VALUE = "Value Error"

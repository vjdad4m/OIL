# This file contains the custom defined errors

class OILFormatError(Exception):
    def __init__(self, data = "") -> None:
        message = f"The OIL file contains invalid data | {data}"
        super().__init__(message)

class OILFileLoadError(Exception):
    def __init__(self) -> None:
        message = "File Error"
        super().__init__(message)

class OILParseError(Exception):
    def __init__(self) -> None:
        message = "Parsing Error"
        super().__init__(message)

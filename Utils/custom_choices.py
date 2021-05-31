# Python's Libraries
import enum

# Django/Third-party Libraries

# Stx Libraries


class SecurityType(enum.Enum):
    # Sets security types for Postman class' parameters
    SSL = 465
    TLS = 587


class DateRangeType(enum.Enum):
    # Sets security types for Postman class' parameters
    Start = "Start"
    End = "End"

from pydantic import BaseModel, Field, constr
from typing import List, Dict, Any
import re
from datetime import datetime
import json

class IdentityData(BaseModel):
    name: str
    telephone: constr(pattern=r'^\+?[1-9]\d{1,14}$')
    license_number: constr(pattern=r'^\d{14}$')

class IdentityModel(BaseModel):
    date: str = Field(..., pattern=r'^\d{8}$')
    identity_data: IdentityData
    codes: List[constr(min_length=5, max_length=6)] = Field(..., min_items=1)

    @property
    def parsed_date(self) -> datetime:
        return datetime.strptime(self.date, '%Y%m%d')

    @classmethod
    def validate_date(cls, v):
        if not re.match(r'^\d{8}$', v):
            raise ValueError('Date must be in YYYYMMDD format')
        try:
            datetime.strptime(v, '%Y%m%d')
        except ValueError:
            raise ValueError('Invalid date')
        return v

    @classmethod
    def get_json_schema(cls) -> Dict[str, Any]:
        """
        Export the Pydantic model as a JSON schema.
        """
        return json.loads(cls.schema_json())

    @classmethod
    def from_json(cls, json_data: str) -> 'IdentityModel':
        """
        Load JSON data into the model.
        """
        data = json.loads(json_data)
        return cls(**data)

    def to_json(self) -> str:
        """
        Export an existing model instance to JSON.
        """
        return self.json()


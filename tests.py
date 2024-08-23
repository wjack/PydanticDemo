from models import IdentityModel, IdentityData
import json

if __name__ == "__main__":
    # Get JSON schema
    schema = IdentityModel.get_json_schema()
    print("JSON Schema:", json.dumps(schema, indent=2))

    # Create a sample model instance
    sample_data = {
        "date": "20240823",
        "identity_data": {
            "name": "John Doe",
            "telephone": "+1234567890",
            "license_number": "12345678901234"
        },
        "codes": ["ABC12", "DEF345", "GHI45"]
    }
    model_instance = IdentityModel(**sample_data)

    # Export model to JSON
    json_output = model_instance.to_json()
    print("\nExported JSON:", json_output)

    # Load JSON into model
    loaded_model = IdentityModel.from_json(json_output)
    print("\nLoaded Model:", loaded_model)
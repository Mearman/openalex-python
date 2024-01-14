# InstitutionsResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_by** | **object** |  | 
**meta** | [**Meta**](Meta.md) |  | 
**results** | **object** |  | [optional] 

## Example

```python
from openalex_api.models.institutions_response_schema import InstitutionsResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of InstitutionsResponseSchema from a JSON string
institutions_response_schema_instance = InstitutionsResponseSchema.from_json(json)
# print the JSON string representation of the object
print InstitutionsResponseSchema.to_json()

# convert the object into a dict
institutions_response_schema_dict = institutions_response_schema_instance.to_dict()
# create an instance of InstitutionsResponseSchema from a dict
institutions_response_schema_form_dict = institutions_response_schema.from_dict(institutions_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



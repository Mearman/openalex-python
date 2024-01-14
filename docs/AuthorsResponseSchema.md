# AuthorsResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_by** | **object** |  | 
**meta** | [**Meta**](Meta.md) |  | 
**results** | **object** |  | [optional] 

## Example

```python
from openalex_api.models.authors_response_schema import AuthorsResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorsResponseSchema from a JSON string
authors_response_schema_instance = AuthorsResponseSchema.from_json(json)
# print the JSON string representation of the object
print AuthorsResponseSchema.to_json()

# convert the object into a dict
authors_response_schema_dict = authors_response_schema_instance.to_dict()
# create an instance of AuthorsResponseSchema from a dict
authors_response_schema_form_dict = authors_response_schema.from_dict(authors_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



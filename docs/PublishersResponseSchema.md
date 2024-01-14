# PublishersResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_by** | **object** |  | 
**meta** | [**Meta**](Meta.md) |  | 
**results** | **object** |  | 

## Example

```python
from openalex_api.models.publishers_response_schema import PublishersResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PublishersResponseSchema from a JSON string
publishers_response_schema_instance = PublishersResponseSchema.from_json(json)
# print the JSON string representation of the object
print PublishersResponseSchema.to_json()

# convert the object into a dict
publishers_response_schema_dict = publishers_response_schema_instance.to_dict()
# create an instance of PublishersResponseSchema from a dict
publishers_response_schema_form_dict = publishers_response_schema.from_dict(publishers_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



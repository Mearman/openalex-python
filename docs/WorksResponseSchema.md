# WorksResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_by** | **object** |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | 
**results** | **object** |  | 

## Example

```python
from openalex_api.models.works_response_schema import WorksResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of WorksResponseSchema from a JSON string
works_response_schema_instance = WorksResponseSchema.from_json(json)
# print the JSON string representation of the object
print WorksResponseSchema.to_json()

# convert the object into a dict
works_response_schema_dict = works_response_schema_instance.to_dict()
# create an instance of WorksResponseSchema from a dict
works_response_schema_form_dict = works_response_schema.from_dict(works_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



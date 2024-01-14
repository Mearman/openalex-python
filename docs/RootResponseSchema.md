# RootResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**documentation_url** | **object** |  | 
**msg** | **object** |  | 
**version** | **object** |  | 

## Example

```python
from mearman_openalex_api.models.root_response_schema import RootResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of RootResponseSchema from a JSON string
root_response_schema_instance = RootResponseSchema.from_json(json)
# print the JSON string representation of the object
print RootResponseSchema.to_json()

# convert the object into a dict
root_response_schema_dict = root_response_schema_instance.to_dict()
# create an instance of RootResponseSchema from a dict
root_response_schema_form_dict = root_response_schema.from_dict(root_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



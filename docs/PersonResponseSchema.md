# PersonResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **object** |  | 
**id** | **object** |  | 
**orcid** | **object** |  | 

## Example

```python
from mearman_openalex_api.models.person_response_schema import PersonResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PersonResponseSchema from a JSON string
person_response_schema_instance = PersonResponseSchema.from_json(json)
# print the JSON string representation of the object
print PersonResponseSchema.to_json()

# convert the object into a dict
person_response_schema_dict = person_response_schema_instance.to_dict()
# create an instance of PersonResponseSchema from a dict
person_response_schema_form_dict = person_response_schema.from_dict(person_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



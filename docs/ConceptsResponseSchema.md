# ConceptsResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_by** | **object** |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 
**results** | **object** |  | [optional] 

## Example

```python
from openalex_api.models.concepts_response_schema import ConceptsResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ConceptsResponseSchema from a JSON string
concepts_response_schema_instance = ConceptsResponseSchema.from_json(json)
# print the JSON string representation of the object
print ConceptsResponseSchema.to_json()

# convert the object into a dict
concepts_response_schema_dict = concepts_response_schema_instance.to_dict()
# create an instance of ConceptsResponseSchema from a dict
concepts_response_schema_form_dict = concepts_response_schema.from_dict(concepts_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



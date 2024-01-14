# AutoCompleteResultSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Meta**](Meta.md) |  | 
**results** | **object** |  | 

## Example

```python
from openalex_api.models.auto_complete_result_schema import AutoCompleteResultSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AutoCompleteResultSchema from a JSON string
auto_complete_result_schema_instance = AutoCompleteResultSchema.from_json(json)
# print the JSON string representation of the object
print AutoCompleteResultSchema.to_json()

# convert the object into a dict
auto_complete_result_schema_dict = auto_complete_result_schema_instance.to_dict()
# create an instance of AutoCompleteResultSchema from a dict
auto_complete_result_schema_form_dict = auto_complete_result_schema.from_dict(auto_complete_result_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# Sources


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_by** | **object** |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 
**results** | **object** |  | [optional] 

## Example

```python
from openalex_api.models.sources import Sources

# TODO update the JSON string below
json = "{}"
# create an instance of Sources from a JSON string
sources_instance = Sources.from_json(json)
# print the JSON string representation of the object
print Sources.to_json()

# convert the object into a dict
sources_dict = sources_instance.to_dict()
# create an instance of Sources from a dict
sources_form_dict = sources.from_dict(sources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# SourcesArray


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_by** | **object** |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 
**results** | **object** |  | [optional] 

## Example

```python
from openalex_api.models.sources_array import SourcesArray

# TODO update the JSON string below
json = "{}"
# create an instance of SourcesArray from a JSON string
sources_array_instance = SourcesArray.from_json(json)
# print the JSON string representation of the object
print SourcesArray.to_json()

# convert the object into a dict
sources_array_dict = sources_array_instance.to_dict()
# create an instance of SourcesArray from a dict
sources_array_form_dict = sources_array.from_dict(sources_array_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



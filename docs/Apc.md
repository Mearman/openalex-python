# Apc


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** |  | 
**provenance** | **str** |  | 
**value** | **int** |  | 
**value_usd** | **int** |  | 

## Example

```python
from mearman_openalex_api.models.apc import Apc

# TODO update the JSON string below
json = "{}"
# create an instance of Apc from a JSON string
apc_instance = Apc.from_json(json)
# print the JSON string representation of the object
print Apc.to_json()

# convert the object into a dict
apc_dict = apc_instance.to_dict()
# create an instance of Apc from a dict
apc_form_dict = apc.from_dict(apc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



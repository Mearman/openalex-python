# SourceSocietiesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from openalex_api.models.source_societies_inner import SourceSocietiesInner

# TODO update the JSON string below
json = "{}"
# create an instance of SourceSocietiesInner from a JSON string
source_societies_inner_instance = SourceSocietiesInner.from_json(json)
# print the JSON string representation of the object
print(SourceSocietiesInner.to_json())

# convert the object into a dict
source_societies_inner_dict = source_societies_inner_instance.to_dict()
# create an instance of SourceSocietiesInner from a dict
source_societies_inner_from_dict = SourceSocietiesInner.from_dict(source_societies_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



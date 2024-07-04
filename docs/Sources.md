# Sources


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_by** | [**List[GroupByResultInner]**](GroupByResultInner.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 
**results** | [**List[SourceSchema]**](SourceSchema.md) |  | [optional] 

## Example

```python
from openalex_api.models.sources import Sources

# TODO update the JSON string below
json = "{}"
# create an instance of Sources from a JSON string
sources_instance = Sources.from_json(json)
# print the JSON string representation of the object
print(Sources.to_json())

# convert the object into a dict
sources_dict = sources_instance.to_dict()
# create an instance of Sources from a dict
sources_from_dict = Sources.from_dict(sources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



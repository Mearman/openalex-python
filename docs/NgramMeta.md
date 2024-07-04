# NgramMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**doi** | **str** |  | [optional] 
**openalex_id** | **str** |  | 

## Example

```python
from openalex_api.models.ngram_meta import NgramMeta

# TODO update the JSON string below
json = "{}"
# create an instance of NgramMeta from a JSON string
ngram_meta_instance = NgramMeta.from_json(json)
# print the JSON string representation of the object
print(NgramMeta.to_json())

# convert the object into a dict
ngram_meta_dict = ngram_meta_instance.to_dict()
# create an instance of NgramMeta from a dict
ngram_meta_from_dict = NgramMeta.from_dict(ngram_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



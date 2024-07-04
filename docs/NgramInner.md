# NgramInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ngram** | **str** |  | 
**ngram_count** | **int** |  | 
**ngram_tokens** | **int** |  | 
**term_frequency** | **float** |  | 

## Example

```python
from openalex_api.models.ngram_inner import NgramInner

# TODO update the JSON string below
json = "{}"
# create an instance of NgramInner from a JSON string
ngram_inner_instance = NgramInner.from_json(json)
# print the JSON string representation of the object
print(NgramInner.to_json())

# convert the object into a dict
ngram_inner_dict = ngram_inner_instance.to_dict()
# create an instance of NgramInner from a dict
ngram_inner_from_dict = NgramInner.from_dict(ngram_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



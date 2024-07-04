# Ngrams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**NgramMeta**](NgramMeta.md) |  | [optional] 
**ngrams** | [**List[NgramInner]**](NgramInner.md) |  | [optional] 

## Example

```python
from openalex_api.models.ngrams import Ngrams

# TODO update the JSON string below
json = "{}"
# create an instance of Ngrams from a JSON string
ngrams_instance = Ngrams.from_json(json)
# print the JSON string representation of the object
print(Ngrams.to_json())

# convert the object into a dict
ngrams_dict = ngrams_instance.to_dict()
# create an instance of Ngrams from a dict
ngrams_from_dict = Ngrams.from_dict(ngrams_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



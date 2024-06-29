# GetTopics200ResponseMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **object** |  | 
**db_response_time_ms** | **object** |  | 
**groups_count** | **object** |  | 
**page** | **object** |  | 
**per_page** | **object** |  | 

## Example

```python
from openalex_api.models.get_topics200_response_meta import GetTopics200ResponseMeta

# TODO update the JSON string below
json = "{}"
# create an instance of GetTopics200ResponseMeta from a JSON string
get_topics200_response_meta_instance = GetTopics200ResponseMeta.from_json(json)
# print the JSON string representation of the object
print GetTopics200ResponseMeta.to_json()

# convert the object into a dict
get_topics200_response_meta_dict = get_topics200_response_meta_instance.to_dict()
# create an instance of GetTopics200ResponseMeta from a dict
get_topics200_response_meta_form_dict = get_topics200_response_meta.from_dict(get_topics200_response_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# TopicsMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**db_response_time_ms** | **int** |  | 
**groups_count** | **int** |  | 
**page** | **int** |  | 
**per_page** | **int** |  | 

## Example

```python
from openalex_api.models.topics_meta import TopicsMeta

# TODO update the JSON string below
json = "{}"
# create an instance of TopicsMeta from a JSON string
topics_meta_instance = TopicsMeta.from_json(json)
# print the JSON string representation of the object
print(TopicsMeta.to_json())

# convert the object into a dict
topics_meta_dict = topics_meta_instance.to_dict()
# create an instance of TopicsMeta from a dict
topics_meta_from_dict = TopicsMeta.from_dict(topics_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



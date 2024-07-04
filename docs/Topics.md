# Topics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_by** | [**List[GroupByResultInner]**](GroupByResultInner.md) |  | 
**meta** | [**TopicsMeta**](TopicsMeta.md) |  | 
**results** | [**List[TopicsResultsInner]**](TopicsResultsInner.md) |  | [optional] 

## Example

```python
from openalex_api.models.topics import Topics

# TODO update the JSON string below
json = "{}"
# create an instance of Topics from a JSON string
topics_instance = Topics.from_json(json)
# print the JSON string representation of the object
print(Topics.to_json())

# convert the object into a dict
topics_dict = topics_instance.to_dict()
# create an instance of Topics from a dict
topics_from_dict = Topics.from_dict(topics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



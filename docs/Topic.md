# Topic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cited_by_count** | **object** |  | 
**created_date** | **object** |  | 
**description** | **object** |  | 
**display_name** | **object** |  | 
**domain** | [**TopicLevelArraySchema**](TopicLevelArraySchema.md) |  | 
**field** | [**TopicLevelArraySchema**](TopicLevelArraySchema.md) |  | 
**id** | **object** |  | 
**ids** | [**Ids**](Ids.md) |  | 
**keywords** | **object** |  | 
**siblings** | [**TopicLevelSchema**](TopicLevelSchema.md) |  | 
**subfield** | [**TopicLevelArraySchema**](TopicLevelArraySchema.md) |  | 
**updated_date** | **object** |  | 
**works_count** | **object** |  | 

## Example

```python
from openalex_api.models.topic import Topic

# TODO update the JSON string below
json = "{}"
# create an instance of Topic from a JSON string
topic_instance = Topic.from_json(json)
# print the JSON string representation of the object
print Topic.to_json()

# convert the object into a dict
topic_dict = topic_instance.to_dict()
# create an instance of Topic from a dict
topic_form_dict = topic.from_dict(topic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



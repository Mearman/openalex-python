# Topic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cited_by_count** | **int** |  | 
**created_date** | **str** |  | 
**description** | **str** |  | 
**display_name** | **str** |  | 
**domain** | [**TopicLevelArraySchema**](TopicLevelArraySchema.md) |  | 
**var_field** | [**TopicLevelArraySchema**](TopicLevelArraySchema.md) |  | 
**id** | **str** |  | 
**ids** | [**Ids**](Ids.md) |  | 
**keywords** | **List[str]** |  | 
**siblings** | [**TopicLevelSchema**](TopicLevelSchema.md) |  | 
**subfield** | [**TopicLevelArraySchema**](TopicLevelArraySchema.md) |  | 
**updated_date** | **str** |  | 
**works_count** | **int** |  | 

## Example

```python
from openalex_api.models.topic import Topic

# TODO update the JSON string below
json = "{}"
# create an instance of Topic from a JSON string
topic_instance = Topic.from_json(json)
# print the JSON string representation of the object
print(Topic.to_json())

# convert the object into a dict
topic_dict = topic_instance.to_dict()
# create an instance of Topic from a dict
topic_from_dict = Topic.from_dict(topic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



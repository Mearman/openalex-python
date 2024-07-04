# TopicLevelSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** |  | 
**id** | [**TopicLevelSchemaId**](TopicLevelSchemaId.md) |  | 

## Example

```python
from openalex_api.models.topic_level_schema import TopicLevelSchema

# TODO update the JSON string below
json = "{}"
# create an instance of TopicLevelSchema from a JSON string
topic_level_schema_instance = TopicLevelSchema.from_json(json)
# print the JSON string representation of the object
print(TopicLevelSchema.to_json())

# convert the object into a dict
topic_level_schema_dict = topic_level_schema_instance.to_dict()
# create an instance of TopicLevelSchema from a dict
topic_level_schema_from_dict = TopicLevelSchema.from_dict(topic_level_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



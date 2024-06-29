# TopicLevelArraySchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**siblings** | **object** |  | [optional] 

## Example

```python
from openalex_api.models.topic_level_array_schema import TopicLevelArraySchema

# TODO update the JSON string below
json = "{}"
# create an instance of TopicLevelArraySchema from a JSON string
topic_level_array_schema_instance = TopicLevelArraySchema.from_json(json)
# print the JSON string representation of the object
print TopicLevelArraySchema.to_json()

# convert the object into a dict
topic_level_array_schema_dict = topic_level_array_schema_instance.to_dict()
# create an instance of TopicLevelArraySchema from a dict
topic_level_array_schema_form_dict = topic_level_array_schema.from_dict(topic_level_array_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



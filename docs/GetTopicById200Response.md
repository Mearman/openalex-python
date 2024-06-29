# GetTopicById200Response


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
from openalex_api.models.get_topic_by_id200_response import GetTopicById200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetTopicById200Response from a JSON string
get_topic_by_id200_response_instance = GetTopicById200Response.from_json(json)
# print the JSON string representation of the object
print GetTopicById200Response.to_json()

# convert the object into a dict
get_topic_by_id200_response_dict = get_topic_by_id200_response_instance.to_dict()
# create an instance of GetTopicById200Response from a dict
get_topic_by_id200_response_form_dict = get_topic_by_id200_response.from_dict(get_topic_by_id200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



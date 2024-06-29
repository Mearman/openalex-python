# GetTopics200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_by** | **object** |  | 
**meta** | [**GetTopics200ResponseMeta**](GetTopics200ResponseMeta.md) |  | 
**results** | **object** |  | [optional] 

## Example

```python
from openalex_api.models.get_topics200_response import GetTopics200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetTopics200Response from a JSON string
get_topics200_response_instance = GetTopics200Response.from_json(json)
# print the JSON string representation of the object
print GetTopics200Response.to_json()

# convert the object into a dict
get_topics200_response_dict = get_topics200_response_instance.to_dict()
# create an instance of GetTopics200Response from a dict
get_topics200_response_form_dict = get_topics200_response.from_dict(get_topics200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



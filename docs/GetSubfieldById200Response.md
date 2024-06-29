# GetSubfieldById200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cited_by_count** | **object** |  | 
**created_date** | **object** |  | 
**description** | **object** |  | 
**display_name** | **object** |  | 
**display_name_alternatives** | **object** |  | 
**domain** | [**TopicLevelSchema**](TopicLevelSchema.md) |  | 
**field** | [**TopicLevelSchema**](TopicLevelSchema.md) |  | 
**id** | **object** |  | 
**ids** | [**Ids**](Ids.md) |  | 
**siblings** | [**TopicLevelArraySchema**](TopicLevelArraySchema.md) |  | 
**topics** | **object** |  | 
**updated_date** | **object** |  | 
**works_api_url** | **object** |  | 
**works_count** | **object** |  | 

## Example

```python
from openalex_api.models.get_subfield_by_id200_response import GetSubfieldById200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetSubfieldById200Response from a JSON string
get_subfield_by_id200_response_instance = GetSubfieldById200Response.from_json(json)
# print the JSON string representation of the object
print GetSubfieldById200Response.to_json()

# convert the object into a dict
get_subfield_by_id200_response_dict = get_subfield_by_id200_response_instance.to_dict()
# create an instance of GetSubfieldById200Response from a dict
get_subfield_by_id200_response_form_dict = get_subfield_by_id200_response.from_dict(get_subfield_by_id200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



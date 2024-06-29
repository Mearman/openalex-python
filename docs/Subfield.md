# Subfield


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
from openalex_api.models.subfield import Subfield

# TODO update the JSON string below
json = "{}"
# create an instance of Subfield from a JSON string
subfield_instance = Subfield.from_json(json)
# print the JSON string representation of the object
print Subfield.to_json()

# convert the object into a dict
subfield_dict = subfield_instance.to_dict()
# create an instance of Subfield from a dict
subfield_form_dict = subfield.from_dict(subfield_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



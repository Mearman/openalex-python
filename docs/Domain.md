# Domain


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cited_by_count** | **object** |  | 
**created_date** | **object** |  | 
**description** | **object** |  | 
**display_name** | **object** |  | 
**display_name_alternatives** | **object** |  | 
**fields** | [**TopicLevelArraySchema**](TopicLevelArraySchema.md) |  | 
**id** | **object** |  | 
**ids** | [**Ids**](Ids.md) |  | 
**siblings** | [**TopicLevelArraySchema**](TopicLevelArraySchema.md) |  | 
**updated_date** | **object** |  | 
**works_api_url** | **object** |  | 
**works_count** | **object** |  | 

## Example

```python
from openalex_api.models.domain import Domain

# TODO update the JSON string below
json = "{}"
# create an instance of Domain from a JSON string
domain_instance = Domain.from_json(json)
# print the JSON string representation of the object
print Domain.to_json()

# convert the object into a dict
domain_dict = domain_instance.to_dict()
# create an instance of Domain from a dict
domain_form_dict = domain.from_dict(domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# Domain


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cited_by_count** | **int** |  | 
**created_date** | **str** |  | 
**description** | **str** |  | 
**display_name** | **str** |  | 
**display_name_alternatives** | **List[str]** |  | 
**fields** | [**TopicLevelArraySchema**](TopicLevelArraySchema.md) |  | 
**id** | **str** |  | 
**ids** | [**Ids**](Ids.md) |  | 
**siblings** | [**TopicLevelArraySchema**](TopicLevelArraySchema.md) |  | 
**updated_date** | **str** |  | 
**works_api_url** | **str** |  | 
**works_count** | **int** |  | 

## Example

```python
from openalex_api.models.domain import Domain

# TODO update the JSON string below
json = "{}"
# create an instance of Domain from a JSON string
domain_instance = Domain.from_json(json)
# print the JSON string representation of the object
print(Domain.to_json())

# convert the object into a dict
domain_dict = domain_instance.to_dict()
# create an instance of Domain from a dict
domain_from_dict = Domain.from_dict(domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



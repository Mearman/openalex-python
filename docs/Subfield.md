# Subfield


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cited_by_count** | **int** |  | 
**created_date** | **str** |  | 
**description** | **str** |  | 
**display_name** | **str** |  | 
**display_name_alternatives** | **List[str]** |  | 
**domain** | [**TopicLevelSchema**](TopicLevelSchema.md) |  | 
**var_field** | [**TopicLevelSchema**](TopicLevelSchema.md) |  | 
**id** | **str** |  | 
**ids** | [**Ids**](Ids.md) |  | 
**siblings** | [**TopicLevelArraySchema**](TopicLevelArraySchema.md) |  | 
**topics** | [**List[SubfieldTopicsInner]**](SubfieldTopicsInner.md) |  | 
**updated_date** | **str** |  | 
**works_api_url** | **str** |  | 
**works_count** | **int** |  | 

## Example

```python
from openalex_api.models.subfield import Subfield

# TODO update the JSON string below
json = "{}"
# create an instance of Subfield from a JSON string
subfield_instance = Subfield.from_json(json)
# print the JSON string representation of the object
print(Subfield.to_json())

# convert the object into a dict
subfield_dict = subfield_instance.to_dict()
# create an instance of Subfield from a dict
subfield_from_dict = Subfield.from_dict(subfield_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



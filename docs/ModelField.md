# ModelField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cited_by_count** | **int** |  | 
**created_date** | **str** |  | 
**description** | **str** |  | 
**display_name** | **str** |  | 
**display_name_alternatives** | **List[str]** |  | 
**domain** | [**TopicLevelSchema**](TopicLevelSchema.md) |  | 
**id** | **str** |  | 
**ids** | [**Ids**](Ids.md) |  | 
**siblings** | [**TopicLevelArraySchema**](TopicLevelArraySchema.md) |  | 
**subfields** | [**TopicLevelArraySchema**](TopicLevelArraySchema.md) |  | 
**updated_date** | **str** |  | 
**works_api_url** | **str** |  | 
**works_count** | **int** |  | 

## Example

```python
from openalex_api.models.model_field import ModelField

# TODO update the JSON string below
json = "{}"
# create an instance of ModelField from a JSON string
model_field_instance = ModelField.from_json(json)
# print the JSON string representation of the object
print(ModelField.to_json())

# convert the object into a dict
model_field_dict = model_field_instance.to_dict()
# create an instance of ModelField from a dict
model_field_from_dict = ModelField.from_dict(model_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



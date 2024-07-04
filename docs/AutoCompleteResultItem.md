# AutoCompleteResultItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cited_by_count** | **int** |  | 
**display_name** | **str** |  | 
**entity_type** | **str** |  | 
**external_id** | **str** |  | 
**filter_key** | **str** |  | 
**hint** | **str** |  | 
**id** | **str** |  | 
**works_count** | **int** |  | 

## Example

```python
from openalex_api.models.auto_complete_result_item import AutoCompleteResultItem

# TODO update the JSON string below
json = "{}"
# create an instance of AutoCompleteResultItem from a JSON string
auto_complete_result_item_instance = AutoCompleteResultItem.from_json(json)
# print the JSON string representation of the object
print(AutoCompleteResultItem.to_json())

# convert the object into a dict
auto_complete_result_item_dict = auto_complete_result_item_instance.to_dict()
# create an instance of AutoCompleteResultItem from a dict
auto_complete_result_item_from_dict = AutoCompleteResultItem.from_dict(auto_complete_result_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# AutoCompleteResultItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cited_by_count** | **object** |  | 
**display_name** | **object** |  | 
**entity_type** | **object** |  | 
**external_id** | **object** |  | 
**filter_key** | **object** |  | 
**hint** | **object** |  | 
**id** | **object** |  | 
**works_count** | **object** |  | 

## Example

```python
from openalex_api.models.auto_complete_result_item import AutoCompleteResultItem

# TODO update the JSON string below
json = "{}"
# create an instance of AutoCompleteResultItem from a JSON string
auto_complete_result_item_instance = AutoCompleteResultItem.from_json(json)
# print the JSON string representation of the object
print AutoCompleteResultItem.to_json()

# convert the object into a dict
auto_complete_result_item_dict = auto_complete_result_item_instance.to_dict()
# create an instance of AutoCompleteResultItem from a dict
auto_complete_result_item_form_dict = auto_complete_result_item.from_dict(auto_complete_result_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



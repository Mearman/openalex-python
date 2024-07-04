# GroupByResultInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**key** | **str** |  | 
**key_display_name** | **str** |  | 

## Example

```python
from openalex_api.models.group_by_result_inner import GroupByResultInner

# TODO update the JSON string below
json = "{}"
# create an instance of GroupByResultInner from a JSON string
group_by_result_inner_instance = GroupByResultInner.from_json(json)
# print the JSON string representation of the object
print(GroupByResultInner.to_json())

# convert the object into a dict
group_by_result_inner_dict = group_by_result_inner_instance.to_dict()
# create an instance of GroupByResultInner from a dict
group_by_result_inner_from_dict = GroupByResultInner.from_dict(group_by_result_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



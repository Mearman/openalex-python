# WorkGrantsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**award_id** | **str** |  | 
**funder** | **str** |  | 
**funder_display_name** | **str** |  | 

## Example

```python
from openalex_api.models.work_grants_inner import WorkGrantsInner

# TODO update the JSON string below
json = "{}"
# create an instance of WorkGrantsInner from a JSON string
work_grants_inner_instance = WorkGrantsInner.from_json(json)
# print the JSON string representation of the object
print(WorkGrantsInner.to_json())

# convert the object into a dict
work_grants_inner_dict = work_grants_inner_instance.to_dict()
# create an instance of WorkGrantsInner from a dict
work_grants_inner_from_dict = WorkGrantsInner.from_dict(work_grants_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



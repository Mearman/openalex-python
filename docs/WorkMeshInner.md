# WorkMeshInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**descriptor_name** | **str** |  | 
**descriptor_ui** | **str** |  | 
**is_major_topic** | **bool** |  | 
**qualifier_name** | **str** |  | 
**qualifier_ui** | **str** |  | 

## Example

```python
from openalex_api.models.work_mesh_inner import WorkMeshInner

# TODO update the JSON string below
json = "{}"
# create an instance of WorkMeshInner from a JSON string
work_mesh_inner_instance = WorkMeshInner.from_json(json)
# print the JSON string representation of the object
print(WorkMeshInner.to_json())

# convert the object into a dict
work_mesh_inner_dict = work_mesh_inner_instance.to_dict()
# create an instance of WorkMeshInner from a dict
work_mesh_inner_from_dict = WorkMeshInner.from_dict(work_mesh_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



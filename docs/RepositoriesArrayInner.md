# RepositoriesArrayInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** |  | 
**host_organization** | **str** |  | 
**host_organization_lineage** | **List[str]** |  | 
**host_organization_name** | **str** |  | 
**id** | **str** |  | 

## Example

```python
from openalex_api.models.repositories_array_inner import RepositoriesArrayInner

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoriesArrayInner from a JSON string
repositories_array_inner_instance = RepositoriesArrayInner.from_json(json)
# print the JSON string representation of the object
print(RepositoriesArrayInner.to_json())

# convert the object into a dict
repositories_array_inner_dict = repositories_array_inner_instance.to_dict()
# create an instance of RepositoriesArrayInner from a dict
repositories_array_inner_from_dict = RepositoriesArrayInner.from_dict(repositories_array_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



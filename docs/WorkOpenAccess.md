# WorkOpenAccess


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**any_repository_has_fulltext** | **object** |  | 
**is_oa** | **object** |  | 
**oa_status** | **object** |  | 
**oa_url** | **object** |  | 

## Example

```python
from openalex_api.models.work_open_access import WorkOpenAccess

# TODO update the JSON string below
json = "{}"
# create an instance of WorkOpenAccess from a JSON string
work_open_access_instance = WorkOpenAccess.from_json(json)
# print the JSON string representation of the object
print WorkOpenAccess.to_json()

# convert the object into a dict
work_open_access_dict = work_open_access_instance.to_dict()
# create an instance of WorkOpenAccess from a dict
work_open_access_form_dict = work_open_access.from_dict(work_open_access_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



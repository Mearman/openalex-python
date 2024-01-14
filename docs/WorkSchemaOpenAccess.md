# WorkSchemaOpenAccess


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**any_repository_has_fulltext** | **object** |  | 
**is_oa** | **object** |  | 
**oa_status** | **object** |  | 
**oa_url** | **object** |  | 

## Example

```python
from openalex_api.models.work_schema_open_access import WorkSchemaOpenAccess

# TODO update the JSON string below
json = "{}"
# create an instance of WorkSchemaOpenAccess from a JSON string
work_schema_open_access_instance = WorkSchemaOpenAccess.from_json(json)
# print the JSON string representation of the object
print WorkSchemaOpenAccess.to_json()

# convert the object into a dict
work_schema_open_access_dict = work_schema_open_access_instance.to_dict()
# create an instance of WorkSchemaOpenAccess from a dict
work_schema_open_access_form_dict = work_schema_open_access.from_dict(work_schema_open_access_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



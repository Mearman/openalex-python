# LocationSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** |  | [optional] 
**host_organization** | **str** |  | [optional] 
**host_organization_lineage** | **List[str]** |  | [optional] 
**host_organization_lineage_names** | **List[str]** |  | [optional] 
**host_organization_name** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**is_in_doaj** | **bool** |  | [optional] 
**is_oa** | **bool** |  | [optional] 
**issn** | **List[str]** |  | [optional] 
**issn_l** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from openalex_api.models.location_source import LocationSource

# TODO update the JSON string below
json = "{}"
# create an instance of LocationSource from a JSON string
location_source_instance = LocationSource.from_json(json)
# print the JSON string representation of the object
print(LocationSource.to_json())

# convert the object into a dict
location_source_dict = location_source_instance.to_dict()
# create an instance of LocationSource from a dict
location_source_from_dict = LocationSource.from_dict(location_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



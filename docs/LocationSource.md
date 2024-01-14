# LocationSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **object** |  | [optional] 
**host_organization** | **object** |  | [optional] 
**host_organization_lineage** | **object** |  | [optional] 
**host_organization_lineage_names** | **object** |  | [optional] 
**host_organization_name** | **object** |  | [optional] 
**id** | **object** |  | [optional] 
**is_in_doaj** | **object** |  | [optional] 
**is_oa** | **object** |  | [optional] 
**issn** | **object** |  | [optional] 
**issn_l** | **object** |  | [optional] 
**type** | **object** |  | [optional] 

## Example

```python
from openalex_api.models.location_source import LocationSource

# TODO update the JSON string below
json = "{}"
# create an instance of LocationSource from a JSON string
location_source_instance = LocationSource.from_json(json)
# print the JSON string representation of the object
print LocationSource.to_json()

# convert the object into a dict
location_source_dict = location_source_instance.to_dict()
# create an instance of LocationSource from a dict
location_source_form_dict = location_source.from_dict(location_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



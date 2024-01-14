# Location


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_accepted** | **object** |  | 
**is_oa** | **object** |  | 
**is_published** | **object** |  | 
**landing_page_url** | **object** |  | 
**license** | **object** |  | [optional] 
**pdf_url** | **object** |  | [optional] 
**source** | [**LocationSource**](LocationSource.md) |  | 
**version** | **object** |  | 

## Example

```python
from mearman_openalex_api.models.location import Location

# TODO update the JSON string below
json = "{}"
# create an instance of Location from a JSON string
location_instance = Location.from_json(json)
# print the JSON string representation of the object
print Location.to_json()

# convert the object into a dict
location_dict = location_instance.to_dict()
# create an instance of Location from a dict
location_form_dict = location.from_dict(location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


# GetWorks200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**foo** | **object** |  | [optional] 
**group_by** | **object** |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | 
**results** | **object** |  | 

## Example

```python
from openalex_api.models.get_works200_response import GetWorks200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetWorks200Response from a JSON string
get_works200_response_instance = GetWorks200Response.from_json(json)
# print the JSON string representation of the object
print GetWorks200Response.to_json()

# convert the object into a dict
get_works200_response_dict = get_works200_response_instance.to_dict()
# create an instance of GetWorks200Response from a dict
get_works200_response_form_dict = get_works200_response.from_dict(get_works200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



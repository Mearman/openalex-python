# Institutions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_by** | **object** |  | 
**meta** | [**Meta**](Meta.md) |  | 
**results** | **object** |  | [optional] 

## Example

```python
from openalex_api.models.institutions import Institutions

# TODO update the JSON string below
json = "{}"
# create an instance of Institutions from a JSON string
institutions_instance = Institutions.from_json(json)
# print the JSON string representation of the object
print Institutions.to_json()

# convert the object into a dict
institutions_dict = institutions_instance.to_dict()
# create an instance of Institutions from a dict
institutions_form_dict = institutions.from_dict(institutions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



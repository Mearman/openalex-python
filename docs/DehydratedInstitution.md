# DehydratedInstitution


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_code** | **object** |  | [optional] 
**display_name** | **object** |  | [optional] 
**id** | **object** |  | [optional] 
**lineage** | **object** |  | [optional] 
**ror** | **object** |  | [optional] 
**type** | **object** |  | [optional] 

## Example

```python
from mearman_openalex_api.models.dehydrated_institution import DehydratedInstitution

# TODO update the JSON string below
json = "{}"
# create an instance of DehydratedInstitution from a JSON string
dehydrated_institution_instance = DehydratedInstitution.from_json(json)
# print the JSON string representation of the object
print DehydratedInstitution.to_json()

# convert the object into a dict
dehydrated_institution_dict = dehydrated_institution_instance.to_dict()
# create an instance of DehydratedInstitution from a dict
dehydrated_institution_form_dict = dehydrated_institution.from_dict(dehydrated_institution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# InternationalDisplayNameAndDescription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | [**InternationalDescription**](InternationalDescription.md) |  | [optional] 
**display_name** | [**InternationalDisplayName**](InternationalDisplayName.md) |  | [optional] 

## Example

```python
from openalex_api.models.international_display_name_and_description import InternationalDisplayNameAndDescription

# TODO update the JSON string below
json = "{}"
# create an instance of InternationalDisplayNameAndDescription from a JSON string
international_display_name_and_description_instance = InternationalDisplayNameAndDescription.from_json(json)
# print the JSON string representation of the object
print InternationalDisplayNameAndDescription.to_json()

# convert the object into a dict
international_display_name_and_description_dict = international_display_name_and_description_instance.to_dict()
# create an instance of InternationalDisplayNameAndDescription from a dict
international_display_name_and_description_form_dict = international_display_name_and_description.from_dict(international_display_name_and_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# InternationalDisplayName


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | [**Internationalisation**](Internationalisation.md) |  | [optional] 

## Example

```python
from openalex_api.models.international_display_name import InternationalDisplayName

# TODO update the JSON string below
json = "{}"
# create an instance of InternationalDisplayName from a JSON string
international_display_name_instance = InternationalDisplayName.from_json(json)
# print the JSON string representation of the object
print(InternationalDisplayName.to_json())

# convert the object into a dict
international_display_name_dict = international_display_name_instance.to_dict()
# create an instance of InternationalDisplayName from a dict
international_display_name_from_dict = InternationalDisplayName.from_dict(international_display_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



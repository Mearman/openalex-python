# InternationalDescription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | [**Internationalisation**](Internationalisation.md) |  | [optional] 

## Example

```python
from openalex_api.models.international_description import InternationalDescription

# TODO update the JSON string below
json = "{}"
# create an instance of InternationalDescription from a JSON string
international_description_instance = InternationalDescription.from_json(json)
# print the JSON string representation of the object
print InternationalDescription.to_json()

# convert the object into a dict
international_description_dict = international_description_instance.to_dict()
# create an instance of InternationalDescription from a dict
international_description_form_dict = international_description.from_dict(international_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# Works


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_by** | **object** |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | 
**results** | **object** |  | 

## Example

```python
from openalex_api.models.works import Works

# TODO update the JSON string below
json = "{}"
# create an instance of Works from a JSON string
works_instance = Works.from_json(json)
# print the JSON string representation of the object
print Works.to_json()

# convert the object into a dict
works_dict = works_instance.to_dict()
# create an instance of Works from a dict
works_form_dict = works.from_dict(works_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



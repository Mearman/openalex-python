# WorksResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_by** | **object** |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | 
**results** | **object** |  | 

## Example

```python
from openalex_api.models.works_response import WorksResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WorksResponse from a JSON string
works_response_instance = WorksResponse.from_json(json)
# print the JSON string representation of the object
print WorksResponse.to_json()

# convert the object into a dict
works_response_dict = works_response_instance.to_dict()
# create an instance of WorksResponse from a dict
works_response_form_dict = works_response.from_dict(works_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



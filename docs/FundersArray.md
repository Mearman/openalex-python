# FundersArray


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_by** | **object** |  | 
**meta** | [**Meta**](Meta.md) |  | 
**results** | **object** |  | [optional] 

## Example

```python
from mearman_openalex_api.models.funders_array import FundersArray

# TODO update the JSON string below
json = "{}"
# create an instance of FundersArray from a JSON string
funders_array_instance = FundersArray.from_json(json)
# print the JSON string representation of the object
print FundersArray.to_json()

# convert the object into a dict
funders_array_dict = funders_array_instance.to_dict()
# create an instance of FundersArray from a dict
funders_array_form_dict = funders_array.from_dict(funders_array_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



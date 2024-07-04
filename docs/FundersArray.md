# FundersArray


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_by** | [**List[GroupByResultInner]**](GroupByResultInner.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 
**results** | [**List[FunderSchema]**](FunderSchema.md) |  | [optional] 

## Example

```python
from openalex_api.models.funders_array import FundersArray

# TODO update the JSON string below
json = "{}"
# create an instance of FundersArray from a JSON string
funders_array_instance = FundersArray.from_json(json)
# print the JSON string representation of the object
print(FundersArray.to_json())

# convert the object into a dict
funders_array_dict = funders_array_instance.to_dict()
# create an instance of FundersArray from a dict
funders_array_from_dict = FundersArray.from_dict(funders_array_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



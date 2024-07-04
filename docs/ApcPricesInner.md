# ApcPricesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** |  | 
**price** | **float** |  | 

## Example

```python
from openalex_api.models.apc_prices_inner import ApcPricesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApcPricesInner from a JSON string
apc_prices_inner_instance = ApcPricesInner.from_json(json)
# print the JSON string representation of the object
print(ApcPricesInner.to_json())

# convert the object into a dict
apc_prices_inner_dict = apc_prices_inner_instance.to_dict()
# create an instance of ApcPricesInner from a dict
apc_prices_inner_from_dict = ApcPricesInner.from_dict(apc_prices_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



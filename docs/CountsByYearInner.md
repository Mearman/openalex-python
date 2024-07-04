# CountsByYearInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cited_by_count** | **int** |  | 
**works_count** | **int** |  | [optional] 
**year** | **int** |  | 

## Example

```python
from openalex_api.models.counts_by_year_inner import CountsByYearInner

# TODO update the JSON string below
json = "{}"
# create an instance of CountsByYearInner from a JSON string
counts_by_year_inner_instance = CountsByYearInner.from_json(json)
# print the JSON string representation of the object
print(CountsByYearInner.to_json())

# convert the object into a dict
counts_by_year_inner_dict = counts_by_year_inner_instance.to_dict()
# create an instance of CountsByYearInner from a dict
counts_by_year_inner_from_dict = CountsByYearInner.from_dict(counts_by_year_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# SummaryStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_2yr_mean_citedness** | **object** |  | 
**h_index** | **object** |  | 
**i10_index** | **object** |  | 

## Example

```python
from mearman_openalex_api.models.summary_stats import SummaryStats

# TODO update the JSON string below
json = "{}"
# create an instance of SummaryStats from a JSON string
summary_stats_instance = SummaryStats.from_json(json)
# print the JSON string representation of the object
print SummaryStats.to_json()

# convert the object into a dict
summary_stats_dict = summary_stats_instance.to_dict()
# create an instance of SummaryStats from a dict
summary_stats_form_dict = summary_stats.from_dict(summary_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



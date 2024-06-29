# Funder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alternate_titles** | **object** |  | 
**cited_by_count** | **object** |  | [optional] 
**country_code** | **object** |  | [optional] 
**counts_by_year** | **object** |  | [optional] 
**created_date** | **object** |  | [optional] 
**description** | **object** |  | [optional] 
**display_name** | **object** |  | 
**grants_count** | **object** |  | [optional] 
**homepage_url** | **object** |  | [optional] 
**id** | **object** |  | 
**ids** | [**Ids**](Ids.md) |  | [optional] 
**image_thumbnail_url** | **object** |  | [optional] 
**image_url** | **object** |  | [optional] 
**relevance_score** | **object** |  | [optional] 
**roles** | **object** |  | [optional] 
**summary_stats** | [**SummaryStats**](SummaryStats.md) |  | [optional] 
**updated_date** | **object** |  | [optional] 
**works_count** | **object** |  | [optional] 

## Example

```python
from openalex_api.models.funder import Funder

# TODO update the JSON string below
json = "{}"
# create an instance of Funder from a JSON string
funder_instance = Funder.from_json(json)
# print the JSON string representation of the object
print Funder.to_json()

# convert the object into a dict
funder_dict = funder_instance.to_dict()
# create an instance of Funder from a dict
funder_form_dict = funder.from_dict(funder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



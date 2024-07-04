# Funder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alternate_titles** | **List[str]** |  | 
**cited_by_count** | **int** |  | [optional] 
**country_code** | **str** |  | [optional] 
**counts_by_year** | [**List[CountsByYearInner]**](CountsByYearInner.md) |  | [optional] 
**created_date** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**display_name** | **str** |  | 
**grants_count** | **int** |  | [optional] 
**homepage_url** | **str** |  | [optional] 
**id** | **str** |  | 
**ids** | [**Ids**](Ids.md) |  | [optional] 
**image_thumbnail_url** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 
**relevance_score** | **float** |  | [optional] 
**roles** | [**List[Role]**](Role.md) |  | [optional] 
**summary_stats** | [**SummaryStats**](SummaryStats.md) |  | [optional] 
**updated_date** | **str** |  | [optional] 
**works_count** | **int** |  | [optional] 

## Example

```python
from openalex_api.models.funder import Funder

# TODO update the JSON string below
json = "{}"
# create an instance of Funder from a JSON string
funder_instance = Funder.from_json(json)
# print the JSON string representation of the object
print(Funder.to_json())

# convert the object into a dict
funder_dict = funder_instance.to_dict()
# create an instance of Funder from a dict
funder_from_dict = Funder.from_dict(funder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



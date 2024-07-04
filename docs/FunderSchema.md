# FunderSchema


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
from openalex_api.models.funder_schema import FunderSchema

# TODO update the JSON string below
json = "{}"
# create an instance of FunderSchema from a JSON string
funder_schema_instance = FunderSchema.from_json(json)
# print the JSON string representation of the object
print(FunderSchema.to_json())

# convert the object into a dict
funder_schema_dict = funder_schema_instance.to_dict()
# create an instance of FunderSchema from a dict
funder_schema_from_dict = FunderSchema.from_dict(funder_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



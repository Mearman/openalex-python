# Source


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abbreviated_title** | **str** |  | [optional] 
**alternate_titles** | **List[str]** |  | [optional] 
**apc_prices** | [**List[ApcPricesInner]**](ApcPricesInner.md) |  | [optional] 
**apc_usd** | **float** |  | [optional] 
**cited_by_count** | **int** |  | [optional] 
**country_code** | **str** |  | [optional] 
**counts_by_year** | [**List[CountsByYearInner]**](CountsByYearInner.md) |  | [optional] 
**created_date** | **str** |  | [optional] 
**display_name** | **str** |  | 
**homepage_url** | **str** |  | [optional] 
**host_organization** | **str** |  | [optional] 
**host_organization_lineage** | **List[str]** |  | [optional] 
**host_organization_name** | **str** |  | [optional] 
**id** | **str** |  | 
**ids** | [**Ids**](Ids.md) |  | [optional] 
**is_in_doaj** | **bool** |  | [optional] 
**is_oa** | **bool** |  | [optional] 
**issn** | **List[str]** |  | [optional] 
**issn_l** | **str** |  | [optional] 
**societies** | [**List[SourceSocietiesInner]**](SourceSocietiesInner.md) |  | [optional] 
**summary_stats** | [**SummaryStats**](SummaryStats.md) |  | [optional] 
**type** | **str** |  | [optional] 
**updated_date** | **str** |  | [optional] 
**works_api_url** | **str** |  | [optional] 
**works_count** | **int** |  | [optional] 
**x_concepts** | [**List[DehydratedConcept]**](DehydratedConcept.md) |  | [optional] 

## Example

```python
from openalex_api.models.source import Source

# TODO update the JSON string below
json = "{}"
# create an instance of Source from a JSON string
source_instance = Source.from_json(json)
# print the JSON string representation of the object
print(Source.to_json())

# convert the object into a dict
source_dict = source_instance.to_dict()
# create an instance of Source from a dict
source_from_dict = Source.from_dict(source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



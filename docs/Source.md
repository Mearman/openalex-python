# Source


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abbreviated_title** | **object** |  | [optional] 
**alternate_titles** | **object** |  | [optional] 
**apc_prices** | **Dict[str, object]** |  | [optional] 
**apc_usd** | **object** |  | [optional] 
**cited_by_count** | **object** |  | [optional] 
**country_code** | **object** |  | [optional] 
**counts_by_year** | **object** |  | [optional] 
**created_date** | **object** |  | [optional] 
**display_name** | **object** |  | 
**homepage_url** | **object** |  | [optional] 
**host_organization** | **object** |  | [optional] 
**host_organization_lineage** | **object** |  | [optional] 
**host_organization_name** | **object** |  | [optional] 
**id** | **object** |  | 
**ids** | [**Ids**](Ids.md) |  | [optional] 
**is_in_doaj** | **object** |  | [optional] 
**is_oa** | **object** |  | [optional] 
**issn** | **object** |  | [optional] 
**issn_l** | **object** |  | [optional] 
**societies** | **object** |  | [optional] 
**summary_stats** | [**SummaryStats**](SummaryStats.md) |  | [optional] 
**type** | **object** |  | [optional] 
**updated_date** | **object** |  | [optional] 
**works_api_url** | **object** |  | [optional] 
**works_count** | **object** |  | [optional] 
**x_concepts** | **object** |  | [optional] 

## Example

```python
from openalex_api.models.source import Source

# TODO update the JSON string below
json = "{}"
# create an instance of Source from a JSON string
source_instance = Source.from_json(json)
# print the JSON string representation of the object
print Source.to_json()

# convert the object into a dict
source_dict = source_instance.to_dict()
# create an instance of Source from a dict
source_form_dict = source.from_dict(source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# FunderSchema


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
from openalex_api.models.funder_schema import FunderSchema

# TODO update the JSON string below
json = "{}"
# create an instance of FunderSchema from a JSON string
funder_schema_instance = FunderSchema.from_json(json)
# print the JSON string representation of the object
print FunderSchema.to_json()

# convert the object into a dict
funder_schema_dict = funder_schema_instance.to_dict()
# create an instance of FunderSchema from a dict
funder_schema_form_dict = funder_schema.from_dict(funder_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



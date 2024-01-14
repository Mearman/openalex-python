# InstitutionSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_institutions** | **object** |  | [optional] 
**cited_by_count** | **object** |  | [optional] 
**country_code** | **object** |  | [optional] 
**counts_by_year** | **object** |  | [optional] 
**created_date** | **object** |  | [optional] 
**display_name** | **object** |  | 
**display_name_acronyms** | **object** |  | [optional] 
**display_name_alternatives** | **object** |  | [optional] 
**geo** | [**Geo**](Geo.md) |  | [optional] 
**homepage_url** | **object** |  | [optional] 
**id** | **object** |  | 
**ids** | [**Ids**](Ids.md) |  | [optional] 
**image_thumbnail_url** | **object** |  | [optional] 
**image_url** | **object** |  | [optional] 
**international** | [**InternationalDisplayName**](InternationalDisplayName.md) |  | [optional] 
**lineage** | **object** |  | [optional] 
**repositories** | **object** |  | [optional] 
**roles** | **object** |  | [optional] 
**ror** | **object** |  | [optional] 
**summary_stats** | [**SummaryStats**](SummaryStats.md) |  | [optional] 
**type** | **object** |  | [optional] 
**updated_date** | **object** |  | [optional] 
**works_api_url** | **object** |  | [optional] 
**works_count** | **object** |  | [optional] 
**x_concepts** | **object** |  | [optional] 

## Example

```python
from mearman_openalex_api.models.institution_schema import InstitutionSchema

# TODO update the JSON string below
json = "{}"
# create an instance of InstitutionSchema from a JSON string
institution_schema_instance = InstitutionSchema.from_json(json)
# print the JSON string representation of the object
print InstitutionSchema.to_json()

# convert the object into a dict
institution_schema_dict = institution_schema_instance.to_dict()
# create an instance of InstitutionSchema from a dict
institution_schema_form_dict = institution_schema.from_dict(institution_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



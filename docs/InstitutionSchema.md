# InstitutionSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_institutions** | [**List[AssociatedInstitution]**](AssociatedInstitution.md) |  | [optional] 
**cited_by_count** | **int** |  | [optional] 
**country_code** | **str** |  | [optional] 
**counts_by_year** | [**List[CountsByYearInner]**](CountsByYearInner.md) |  | [optional] 
**created_date** | **str** |  | [optional] 
**display_name** | **str** |  | 
**display_name_acronyms** | **List[str]** |  | [optional] 
**display_name_alternatives** | **List[str]** |  | [optional] 
**geo** | [**Geo**](Geo.md) |  | [optional] 
**homepage_url** | **str** |  | [optional] 
**id** | **str** |  | 
**ids** | [**Ids**](Ids.md) |  | [optional] 
**image_thumbnail_url** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 
**international** | [**InternationalDisplayName**](InternationalDisplayName.md) |  | [optional] 
**lineage** | **List[str]** |  | [optional] 
**repositories** | [**List[RepositoriesArrayInner]**](RepositoriesArrayInner.md) |  | [optional] 
**roles** | [**List[Role]**](Role.md) |  | [optional] 
**ror** | **str** |  | [optional] 
**summary_stats** | [**SummaryStats**](SummaryStats.md) |  | [optional] 
**type** | **str** |  | [optional] 
**updated_date** | **str** |  | [optional] 
**works_api_url** | **str** |  | [optional] 
**works_count** | **int** |  | [optional] 
**x_concepts** | [**List[DehydratedConcept]**](DehydratedConcept.md) |  | [optional] 

## Example

```python
from openalex_api.models.institution_schema import InstitutionSchema

# TODO update the JSON string below
json = "{}"
# create an instance of InstitutionSchema from a JSON string
institution_schema_instance = InstitutionSchema.from_json(json)
# print the JSON string representation of the object
print(InstitutionSchema.to_json())

# convert the object into a dict
institution_schema_dict = institution_schema_instance.to_dict()
# create an instance of InstitutionSchema from a dict
institution_schema_from_dict = InstitutionSchema.from_dict(institution_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



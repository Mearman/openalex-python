# ConceptSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ancestors** | **object** |  | [optional] 
**cited_by_count** | **object** |  | [optional] 
**counts_by_year** | **object** |  | [optional] 
**created_date** | **object** |  | [optional] 
**description** | **object** |  | [optional] 
**display_name** | **object** |  | 
**id** | **object** |  | 
**ids** | [**ConceptIds**](ConceptIds.md) |  | [optional] 
**image_thumbnail_url** | **object** |  | [optional] 
**image_url** | **object** |  | [optional] 
**international** | [**InternationalDisplayNameAndDescription**](InternationalDisplayNameAndDescription.md) |  | [optional] 
**level** | **object** |  | [optional] 
**related_concepts** | **object** |  | [optional] 
**summary_stats** | [**SummaryStats**](SummaryStats.md) |  | [optional] 
**updated_date** | **object** |  | [optional] 
**wikidata** | **object** |  | [optional] 
**works_api_url** | **object** |  | [optional] 
**works_count** | **object** |  | [optional] 

## Example

```python
from mearman_openalex_api.models.concept_schema import ConceptSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ConceptSchema from a JSON string
concept_schema_instance = ConceptSchema.from_json(json)
# print the JSON string representation of the object
print ConceptSchema.to_json()

# convert the object into a dict
concept_schema_dict = concept_schema_instance.to_dict()
# create an instance of ConceptSchema from a dict
concept_schema_form_dict = concept_schema.from_dict(concept_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



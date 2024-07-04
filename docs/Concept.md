# Concept


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ancestors** | [**List[DehydratedConcept]**](DehydratedConcept.md) |  | [optional] 
**cited_by_count** | **int** |  | [optional] 
**counts_by_year** | [**List[CountsByYearInner]**](CountsByYearInner.md) |  | [optional] 
**created_date** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**display_name** | **str** |  | 
**id** | **str** |  | 
**ids** | [**ConceptIds**](ConceptIds.md) |  | [optional] 
**image_thumbnail_url** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 
**international** | [**InternationalDisplayNameAndDescription**](InternationalDisplayNameAndDescription.md) |  | [optional] 
**level** | **int** |  | [optional] 
**related_concepts** | [**List[DehydratedConcept]**](DehydratedConcept.md) |  | [optional] 
**summary_stats** | [**SummaryStats**](SummaryStats.md) |  | [optional] 
**updated_date** | **str** |  | [optional] 
**wikidata** | **str** |  | [optional] 
**works_api_url** | **str** |  | [optional] 
**works_count** | **int** |  | [optional] 

## Example

```python
from openalex_api.models.concept import Concept

# TODO update the JSON string below
json = "{}"
# create an instance of Concept from a JSON string
concept_instance = Concept.from_json(json)
# print the JSON string representation of the object
print(Concept.to_json())

# convert the object into a dict
concept_dict = concept_instance.to_dict()
# create an instance of Concept from a dict
concept_from_dict = Concept.from_dict(concept_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



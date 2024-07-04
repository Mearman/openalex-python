# Work


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abstract_inverted_index** | **object** |  | [optional] 
**apc_list** | [**Apc**](Apc.md) |  | [optional] 
**apc_paid** | [**Apc**](Apc.md) |  | [optional] 
**authorships** | [**List[AuthorshipsInner]**](AuthorshipsInner.md) |  | [optional] 
**best_oa_location** | [**Location**](Location.md) |  | [optional] 
**biblio** | [**WorkBiblio**](WorkBiblio.md) |  | [optional] 
**cited_by_api_url** | **str** |  | [optional] 
**cited_by_count** | **int** |  | [optional] 
**cited_by_percentile_year** | [**WorkCitedByPercentileYear**](WorkCitedByPercentileYear.md) |  | [optional] 
**concepts** | [**List[DehydratedConcept]**](DehydratedConcept.md) |  | [optional] 
**corresponding_author_ids** | **List[str]** |  | [optional] 
**corresponding_institution_ids** | **List[str]** |  | [optional] 
**countries_distinct_count** | **int** |  | [optional] 
**counts_by_year** | [**List[CountsByYearInner]**](CountsByYearInner.md) |  | [optional] 
**created_date** | **str** |  | [optional] 
**display_name** | **str** |  | 
**doi** | **str** |  | [optional] 
**grants** | [**List[WorkGrantsInner]**](WorkGrantsInner.md) |  | [optional] 
**has_fulltext** | **bool** |  | [optional] 
**id** | **str** |  | 
**ids** | [**Ids**](Ids.md) |  | [optional] 
**institutions_distinct_count** | **int** |  | [optional] 
**is_paratext** | **bool** |  | [optional] 
**is_retracted** | **bool** |  | [optional] 
**keywords** | [**List[WorkKeywordsInner]**](WorkKeywordsInner.md) |  | [optional] 
**language** | **str** |  | [optional] 
**locations** | [**List[Location]**](Location.md) |  | [optional] 
**locations_count** | **int** |  | [optional] 
**mesh** | [**List[WorkMeshInner]**](WorkMeshInner.md) |  | [optional] 
**ngrams_url** | **str** |  | [optional] 
**open_access** | [**WorkOpenAccess**](WorkOpenAccess.md) |  | [optional] 
**primary_location** | [**Location**](Location.md) |  | [optional] 
**publication_date** | **str** |  | [optional] 
**publication_year** | **int** |  | [optional] 
**referenced_works** | **List[str]** |  | [optional] 
**referenced_works_count** | **int** |  | [optional] 
**related_works** | **List[str]** |  | [optional] 
**sustainable_development_goals** | [**List[WorkSustainableDevelopmentGoalsInner]**](WorkSustainableDevelopmentGoalsInner.md) |  | [optional] 
**title** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**type_crossref** | **str** |  | [optional] 
**updated_date** | **str** |  | [optional] 

## Example

```python
from openalex_api.models.work import Work

# TODO update the JSON string below
json = "{}"
# create an instance of Work from a JSON string
work_instance = Work.from_json(json)
# print the JSON string representation of the object
print(Work.to_json())

# convert the object into a dict
work_dict = work_instance.to_dict()
# create an instance of Work from a dict
work_from_dict = Work.from_dict(work_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



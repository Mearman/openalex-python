# Work


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abstract_inverted_index** | **object** |  | [optional] 
**apc_list** | [**Apc**](Apc.md) |  | [optional] 
**apc_paid** | [**Apc**](Apc.md) |  | [optional] 
**authorships** | **object** |  | [optional] 
**best_oa_location** | [**Location**](Location.md) |  | [optional] 
**biblio** | [**WorkBiblio**](WorkBiblio.md) |  | [optional] 
**cited_by_api_url** | **object** |  | [optional] 
**cited_by_count** | **object** |  | [optional] 
**cited_by_percentile_year** | [**WorkCitedByPercentileYear**](WorkCitedByPercentileYear.md) |  | [optional] 
**concepts** | **object** |  | [optional] 
**corresponding_author_ids** | **object** |  | [optional] 
**corresponding_institution_ids** | **object** |  | [optional] 
**countries_distinct_count** | **object** |  | [optional] 
**counts_by_year** | **object** |  | [optional] 
**created_date** | **object** |  | [optional] 
**display_name** | **object** |  | 
**doi** | **object** |  | [optional] 
**grants** | **object** |  | [optional] 
**has_fulltext** | **object** |  | [optional] 
**id** | **object** |  | 
**ids** | [**Ids**](Ids.md) |  | [optional] 
**institutions_distinct_count** | **object** |  | [optional] 
**is_paratext** | **object** |  | [optional] 
**is_retracted** | **object** |  | [optional] 
**keywords** | **object** |  | [optional] 
**language** | **object** |  | [optional] 
**locations** | **object** |  | [optional] 
**locations_count** | **object** |  | [optional] 
**mesh** | **object** |  | [optional] 
**ngrams_url** | **object** |  | [optional] 
**open_access** | [**WorkOpenAccess**](WorkOpenAccess.md) |  | [optional] 
**primary_location** | [**Location**](Location.md) |  | [optional] 
**publication_date** | **object** |  | [optional] 
**publication_year** | **object** |  | [optional] 
**referenced_works** | **object** |  | [optional] 
**referenced_works_count** | **object** |  | [optional] 
**related_works** | **object** |  | [optional] 
**sustainable_development_goals** | **object** |  | [optional] 
**title** | **object** |  | [optional] 
**type** | **object** |  | [optional] 
**type_crossref** | **object** |  | [optional] 
**updated_date** | **object** |  | [optional] 

## Example

```python
from openalex_api.models.work import Work

# TODO update the JSON string below
json = "{}"
# create an instance of Work from a JSON string
work_instance = Work.from_json(json)
# print the JSON string representation of the object
print Work.to_json()

# convert the object into a dict
work_dict = work_instance.to_dict()
# create an instance of Work from a dict
work_form_dict = work.from_dict(work_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# Author


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affiliations** | [**List[AffiliationsInner]**](AffiliationsInner.md) |  | [optional] 
**cited_by_count** | **int** |  | [optional] 
**counts_by_year** | [**List[CountsByYearInner]**](CountsByYearInner.md) |  | [optional] 
**created_date** | **str** |  | [optional] 
**display_name** | **str** |  | 
**display_name_alternatives** | **List[str]** |  | [optional] 
**id** | **str** |  | 
**ids** | [**Ids**](Ids.md) |  | [optional] 
**last_known_institution** | [**DehydratedInstitution**](DehydratedInstitution.md) |  | [optional] 
**last_known_institutions** | [**List[DehydratedInstitution]**](DehydratedInstitution.md) |  | [optional] 
**orcid** | **str** |  | [optional] 
**summary_stats** | [**SummaryStats**](SummaryStats.md) |  | [optional] 
**updated_date** | **str** |  | [optional] 
**works_api_url** | **str** |  | [optional] 
**works_count** | **int** |  | [optional] 
**x_concepts** | [**List[DehydratedConcept]**](DehydratedConcept.md) |  | [optional] 

## Example

```python
from openalex_api.models.author import Author

# TODO update the JSON string below
json = "{}"
# create an instance of Author from a JSON string
author_instance = Author.from_json(json)
# print the JSON string representation of the object
print(Author.to_json())

# convert the object into a dict
author_dict = author_instance.to_dict()
# create an instance of Author from a dict
author_from_dict = Author.from_dict(author_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



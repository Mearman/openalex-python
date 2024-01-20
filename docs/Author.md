# Author


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affiliations** | **object** |  | [optional] 
**cited_by_count** | **object** |  | [optional] 
**counts_by_year** | **object** |  | [optional] 
**created_date** | **object** |  | [optional] 
**display_name** | **object** |  | 
**display_name_alternatives** | **object** |  | [optional] 
**id** | **object** |  | 
**ids** | [**Ids**](Ids.md) |  | [optional] 
**last_known_institution** | [**DehydratedInstitution**](DehydratedInstitution.md) |  | [optional] 
**last_known_institutions** | **object** |  | [optional] 
**orcid** | **object** |  | [optional] 
**summary_stats** | [**SummaryStats**](SummaryStats.md) |  | [optional] 
**updated_date** | **object** |  | [optional] 
**works_api_url** | **object** |  | [optional] 
**works_count** | **object** |  | [optional] 
**x_concepts** | **object** |  | [optional] 

## Example

```python
from openalex_api.models.author import Author

# TODO update the JSON string below
json = "{}"
# create an instance of Author from a JSON string
author_instance = Author.from_json(json)
# print the JSON string representation of the object
print Author.to_json()

# convert the object into a dict
author_dict = author_instance.to_dict()
# create an instance of Author from a dict
author_form_dict = author.from_dict(author_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



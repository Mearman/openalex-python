# Ids


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**crossref** | **object** |  | [optional] 
**doi** | **object** |  | [optional] 
**fatcat** | **object** |  | [optional] 
**grid** | **object** |  | [optional] 
**issn** | **object** |  | [optional] 
**issn_l** | **object** |  | [optional] 
**mag** | **object** |  | [optional] 
**openalex** | **object** |  | 
**orcid** | **object** |  | [optional] 
**pmcid** | **object** |  | [optional] 
**pmid** | **object** |  | [optional] 
**ror** | **object** |  | [optional] 
**scopus** | **object** |  | [optional] 
**wikidata** | **object** |  | [optional] 
**wikipedia** | **object** |  | [optional] 

## Example

```python
from openalex_api.models.ids import Ids

# TODO update the JSON string below
json = "{}"
# create an instance of Ids from a JSON string
ids_instance = Ids.from_json(json)
# print the JSON string representation of the object
print Ids.to_json()

# convert the object into a dict
ids_dict = ids_instance.to_dict()
# create an instance of Ids from a dict
ids_form_dict = ids.from_dict(ids_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



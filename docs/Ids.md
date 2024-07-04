# Ids


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**crossref** | **str** |  | [optional] 
**doi** | **str** |  | [optional] 
**fatcat** | **str** |  | [optional] 
**grid** | **str** |  | [optional] 
**issn** | **List[str]** |  | [optional] 
**issn_l** | **str** |  | [optional] 
**mag** | **str** |  | [optional] 
**openalex** | **str** |  | 
**orcid** | **str** |  | [optional] 
**pmcid** | **str** |  | [optional] 
**pmid** | **str** |  | [optional] 
**ror** | **str** |  | [optional] 
**scopus** | **str** |  | [optional] 
**wikidata** | **str** |  | [optional] 
**wikipedia** | **str** |  | [optional] 

## Example

```python
from openalex_api.models.ids import Ids

# TODO update the JSON string below
json = "{}"
# create an instance of Ids from a JSON string
ids_instance = Ids.from_json(json)
# print the JSON string representation of the object
print(Ids.to_json())

# convert the object into a dict
ids_dict = ids_instance.to_dict()
# create an instance of Ids from a dict
ids_from_dict = Ids.from_dict(ids_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



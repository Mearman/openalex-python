# ConceptIds


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mag** | **str** |  | [optional] 
**openalex** | **str** |  | 
**umls_cui** | **List[str]** |  | [optional] 
**wikidata** | **str** |  | [optional] 
**wikipedia** | **str** |  | [optional] 

## Example

```python
from openalex_api.models.concept_ids import ConceptIds

# TODO update the JSON string below
json = "{}"
# create an instance of ConceptIds from a JSON string
concept_ids_instance = ConceptIds.from_json(json)
# print the JSON string representation of the object
print(ConceptIds.to_json())

# convert the object into a dict
concept_ids_dict = concept_ids_instance.to_dict()
# create an instance of ConceptIds from a dict
concept_ids_from_dict = ConceptIds.from_dict(concept_ids_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# DehydratedConcept


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **object** |  | 
**id** | **object** |  | 
**level** | **object** |  | [optional] 
**score** | **object** |  | [optional] 
**wikidata** | **object** |  | [optional] 

## Example

```python
from mearman_openalex_api.models.dehydrated_concept import DehydratedConcept

# TODO update the JSON string below
json = "{}"
# create an instance of DehydratedConcept from a JSON string
dehydrated_concept_instance = DehydratedConcept.from_json(json)
# print the JSON string representation of the object
print DehydratedConcept.to_json()

# convert the object into a dict
dehydrated_concept_dict = dehydrated_concept_instance.to_dict()
# create an instance of DehydratedConcept from a dict
dehydrated_concept_form_dict = dehydrated_concept.from_dict(dehydrated_concept_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



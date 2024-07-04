# Concepts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_by** | [**List[GroupByResultInner]**](GroupByResultInner.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 
**results** | [**List[Concept]**](Concept.md) |  | [optional] 

## Example

```python
from openalex_api.models.concepts import Concepts

# TODO update the JSON string below
json = "{}"
# create an instance of Concepts from a JSON string
concepts_instance = Concepts.from_json(json)
# print the JSON string representation of the object
print(Concepts.to_json())

# convert the object into a dict
concepts_dict = concepts_instance.to_dict()
# create an instance of Concepts from a dict
concepts_from_dict = Concepts.from_dict(concepts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



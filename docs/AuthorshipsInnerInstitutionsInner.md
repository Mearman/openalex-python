# AuthorshipsInnerInstitutionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_code** | **str** |  | 
**display_name** | **str** |  | 
**id** | **str** |  | 
**lineage** | **List[str]** |  | 
**ror** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from openalex_api.models.authorships_inner_institutions_inner import AuthorshipsInnerInstitutionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorshipsInnerInstitutionsInner from a JSON string
authorships_inner_institutions_inner_instance = AuthorshipsInnerInstitutionsInner.from_json(json)
# print the JSON string representation of the object
print(AuthorshipsInnerInstitutionsInner.to_json())

# convert the object into a dict
authorships_inner_institutions_inner_dict = authorships_inner_institutions_inner_instance.to_dict()
# create an instance of AuthorshipsInnerInstitutionsInner from a dict
authorships_inner_institutions_inner_from_dict = AuthorshipsInnerInstitutionsInner.from_dict(authorships_inner_institutions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# AuthorshipsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | [**AuthorshipsInnerAuthor**](AuthorshipsInnerAuthor.md) |  | 
**author_position** | **str** |  | 
**countries** | **List[str]** |  | 
**institutions** | [**List[AuthorshipsInnerInstitutionsInner]**](AuthorshipsInnerInstitutionsInner.md) |  | 
**is_corresponding** | **bool** |  | 
**raw_affiliation_string** | **str** |  | [optional] 
**raw_affiliation_strings** | **List[str]** |  | 
**raw_author_name** | **str** |  | 

## Example

```python
from openalex_api.models.authorships_inner import AuthorshipsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorshipsInner from a JSON string
authorships_inner_instance = AuthorshipsInner.from_json(json)
# print the JSON string representation of the object
print(AuthorshipsInner.to_json())

# convert the object into a dict
authorships_inner_dict = authorships_inner_instance.to_dict()
# create an instance of AuthorshipsInner from a dict
authorships_inner_from_dict = AuthorshipsInner.from_dict(authorships_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



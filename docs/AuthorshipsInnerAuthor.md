# AuthorshipsInnerAuthor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** |  | 
**id** | **str** |  | 
**orcid** | **str** |  | [optional] 

## Example

```python
from openalex_api.models.authorships_inner_author import AuthorshipsInnerAuthor

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorshipsInnerAuthor from a JSON string
authorships_inner_author_instance = AuthorshipsInnerAuthor.from_json(json)
# print the JSON string representation of the object
print(AuthorshipsInnerAuthor.to_json())

# convert the object into a dict
authorships_inner_author_dict = authorships_inner_author_instance.to_dict()
# create an instance of AuthorshipsInnerAuthor from a dict
authorships_inner_author_from_dict = AuthorshipsInnerAuthor.from_dict(authorships_inner_author_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# AffiliationsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**institution** | [**DehydratedInstitution**](DehydratedInstitution.md) |  | 
**years** | **List[int]** |  | 

## Example

```python
from mearman_openalex_api.models.affiliations_inner import AffiliationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AffiliationsInner from a JSON string
affiliations_inner_instance = AffiliationsInner.from_json(json)
# print the JSON string representation of the object
print AffiliationsInner.to_json()

# convert the object into a dict
affiliations_inner_dict = affiliations_inner_instance.to_dict()
# create an instance of AffiliationsInner from a dict
affiliations_inner_form_dict = affiliations_inner.from_dict(affiliations_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



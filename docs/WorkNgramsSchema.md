# WorkNgramsSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**NgramMeta**](NgramMeta.md) |  | [optional] 
**ngrams** | **object** |  | [optional] 

## Example

```python
from openalex_api.models.work_ngrams_schema import WorkNgramsSchema

# TODO update the JSON string below
json = "{}"
# create an instance of WorkNgramsSchema from a JSON string
work_ngrams_schema_instance = WorkNgramsSchema.from_json(json)
# print the JSON string representation of the object
print WorkNgramsSchema.to_json()

# convert the object into a dict
work_ngrams_schema_dict = work_ngrams_schema_instance.to_dict()
# create an instance of WorkNgramsSchema from a dict
work_ngrams_schema_form_dict = work_ngrams_schema.from_dict(work_ngrams_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



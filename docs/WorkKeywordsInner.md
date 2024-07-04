# WorkKeywordsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** |  | 
**id** | **str** |  | 
**score** | **float** |  | 

## Example

```python
from openalex_api.models.work_keywords_inner import WorkKeywordsInner

# TODO update the JSON string below
json = "{}"
# create an instance of WorkKeywordsInner from a JSON string
work_keywords_inner_instance = WorkKeywordsInner.from_json(json)
# print the JSON string representation of the object
print(WorkKeywordsInner.to_json())

# convert the object into a dict
work_keywords_inner_dict = work_keywords_inner_instance.to_dict()
# create an instance of WorkKeywordsInner from a dict
work_keywords_inner_from_dict = WorkKeywordsInner.from_dict(work_keywords_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# TopicsResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cited_by_count** | **int** |  | [optional] 
**created_date** | **str** |  | [optional] 
**description** | **str** |  | 
**display_name** | **str** |  | 
**domain** | [**TopicLevelSchema**](TopicLevelSchema.md) |  | [optional] 
**var_field** | [**TopicLevelSchema**](TopicLevelSchema.md) |  | [optional] 
**id** | **str** |  | 
**ids** | [**Ids**](Ids.md) |  | [optional] 
**keywords** | **List[str]** |  | [optional] 
**relevance_score** | **float** |  | [optional] 
**siblings** | [**TopicLevelArraySchema**](TopicLevelArraySchema.md) |  | [optional] 
**subfield** | [**TopicLevelSchema**](TopicLevelSchema.md) |  | [optional] 
**updated_date** | **str** |  | [optional] 
**works_count** | **int** |  | [optional] 

## Example

```python
from openalex_api.models.topics_results_inner import TopicsResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of TopicsResultsInner from a JSON string
topics_results_inner_instance = TopicsResultsInner.from_json(json)
# print the JSON string representation of the object
print(TopicsResultsInner.to_json())

# convert the object into a dict
topics_results_inner_dict = topics_results_inner_instance.to_dict()
# create an instance of TopicsResultsInner from a dict
topics_results_inner_from_dict = TopicsResultsInner.from_dict(topics_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



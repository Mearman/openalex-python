# Publisher


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alternate_titles** | **List[str]** |  | [optional] 
**cited_by_count** | **int** |  | [optional] 
**country_codes** | **List[str]** |  | [optional] 
**counts_by_year** | [**List[CountsByYearInner]**](CountsByYearInner.md) |  | [optional] 
**created_date** | **str** |  | [optional] 
**display_name** | **str** |  | 
**hierarchy_level** | **int** |  | [optional] 
**homepage_url** | **str** |  | [optional] 
**id** | **str** |  | 
**ids** | [**Ids**](Ids.md) |  | [optional] 
**image_thumbnail_url** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 
**lineage** | **List[str]** |  | [optional] 
**parent_publisher** | [**PublisherParentPublisher**](PublisherParentPublisher.md) |  | [optional] 
**roles** | [**List[Role]**](Role.md) |  | [optional] 
**sources_api_url** | **str** |  | [optional] 
**summary_stats** | [**SummaryStats**](SummaryStats.md) |  | [optional] 
**updated_date** | **str** |  | [optional] 
**works_count** | **int** |  | [optional] 

## Example

```python
from openalex_api.models.publisher import Publisher

# TODO update the JSON string below
json = "{}"
# create an instance of Publisher from a JSON string
publisher_instance = Publisher.from_json(json)
# print the JSON string representation of the object
print(Publisher.to_json())

# convert the object into a dict
publisher_dict = publisher_instance.to_dict()
# create an instance of Publisher from a dict
publisher_from_dict = Publisher.from_dict(publisher_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



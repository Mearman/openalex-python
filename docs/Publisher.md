# Publisher


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alternate_titles** | **object** |  | [optional] 
**cited_by_count** | **object** |  | [optional] 
**country_codes** | **object** |  | [optional] 
**counts_by_year** | **object** |  | [optional] 
**created_date** | **object** |  | [optional] 
**display_name** | **object** |  | 
**hierarchy_level** | **object** |  | [optional] 
**homepage_url** | **object** |  | [optional] 
**id** | **object** |  | 
**ids** | [**Ids**](Ids.md) |  | [optional] 
**image_thumbnail_url** | **object** |  | [optional] 
**image_url** | **object** |  | [optional] 
**lineage** | **object** |  | [optional] 
**parent_publisher** | [**PublisherParentPublisher**](PublisherParentPublisher.md) |  | [optional] 
**roles** | **object** |  | [optional] 
**sources_api_url** | **object** |  | [optional] 
**summary_stats** | [**SummaryStats**](SummaryStats.md) |  | [optional] 
**updated_date** | **object** |  | [optional] 
**works_count** | **object** |  | [optional] 

## Example

```python
from openalex_api.models.publisher import Publisher

# TODO update the JSON string below
json = "{}"
# create an instance of Publisher from a JSON string
publisher_instance = Publisher.from_json(json)
# print the JSON string representation of the object
print Publisher.to_json()

# convert the object into a dict
publisher_dict = publisher_instance.to_dict()
# create an instance of Publisher from a dict
publisher_form_dict = publisher.from_dict(publisher_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



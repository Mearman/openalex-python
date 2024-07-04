# openalex_api.MultipleApi

All URIs are relative to *https://api.openalex.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_subfield_by_id**](MultipleApi.md#get_subfield_by_id) | **GET** /subfields/{id} | /subfields/{id}
[**get_topics**](MultipleApi.md#get_topics) | **GET** /topics | /topics


# **get_subfield_by_id**
> Subfield get_subfield_by_id(id, per_page=per_page, user_agent=user_agent, mailto=mailto)

/subfields/{id}



### Example


```python
import openalex_api
from openalex_api.models.subfield import Subfield
from openalex_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.openalex.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openalex_api.Configuration(
    host = "https://api.openalex.org"
)


# Enter a context with an instance of the API client
with openalex_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openalex_api.MultipleApi(api_client)
    id = 'id_example' # str | 
    per_page = 3 # int |  (optional)
    user_agent = 'user_agent_example' # str | [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool) (optional)
    mailto = 'mailto_example' # str | The API is the primary way to get OpenAlex data. It's free and requires no authentication. The daily limit for API calls is 100,000 requests per user per day. For best performance, add your email to all API requests The email can be either in the query string, like `mailto:example@domain.com`, or in the User-Agent request header, like `User-Agent: my-app (mailto:example@domain.com)`. Read more about the polite pool at [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool). (optional)

    try:
        # /subfields/{id}
        api_response = api_instance.get_subfield_by_id(id, per_page=per_page, user_agent=user_agent, mailto=mailto)
        print("The response of MultipleApi->get_subfield_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MultipleApi->get_subfield_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **per_page** | **int**|  | [optional] 
 **user_agent** | **str**| [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool) | [optional] 
 **mailto** | **str**| The API is the primary way to get OpenAlex data. It&#39;s free and requires no authentication. The daily limit for API calls is 100,000 requests per user per day. For best performance, add your email to all API requests The email can be either in the query string, like &#x60;mailto:example@domain.com&#x60;, or in the User-Agent request header, like &#x60;User-Agent: my-app (mailto:example@domain.com)&#x60;. Read more about the polite pool at [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool). | [optional] 

### Return type

[**Subfield**](Subfield.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**403** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_topics**
> Topics get_topics(sort=sort, per_page=per_page, page=page, sample=sample, select=select, filter=filter, search=search, group_by=group_by, user_agent=user_agent, mailto=mailto)

/topics



### Example


```python
import openalex_api
from openalex_api.models.topics import Topics
from openalex_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.openalex.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openalex_api.Configuration(
    host = "https://api.openalex.org"
)


# Enter a context with an instance of the API client
with openalex_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openalex_api.MultipleApi(api_client)
    sort = 'sort_example' # str |  (optional)
    per_page = 3 # int |  (optional)
    page = 'page_example' # str |  (optional)
    sample = 'sample_example' # str |  (optional)
    select = 'select_example' # str |  (optional)
    filter = 'filter_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    group_by = 'group_by_example' # str |  (optional)
    user_agent = 'user_agent_example' # str | [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool) (optional)
    mailto = 'mailto_example' # str | The API is the primary way to get OpenAlex data. It's free and requires no authentication. The daily limit for API calls is 100,000 requests per user per day. For best performance, add your email to all API requests The email can be either in the query string, like `mailto:example@domain.com`, or in the User-Agent request header, like `User-Agent: my-app (mailto:example@domain.com)`. Read more about the polite pool at [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool). (optional)

    try:
        # /topics
        api_response = api_instance.get_topics(sort=sort, per_page=per_page, page=page, sample=sample, select=select, filter=filter, search=search, group_by=group_by, user_agent=user_agent, mailto=mailto)
        print("The response of MultipleApi->get_topics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MultipleApi->get_topics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**|  | [optional] 
 **per_page** | **int**|  | [optional] 
 **page** | **str**|  | [optional] 
 **sample** | **str**|  | [optional] 
 **select** | **str**|  | [optional] 
 **filter** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 
 **group_by** | **str**|  | [optional] 
 **user_agent** | **str**| [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool) | [optional] 
 **mailto** | **str**| The API is the primary way to get OpenAlex data. It&#39;s free and requires no authentication. The daily limit for API calls is 100,000 requests per user per day. For best performance, add your email to all API requests The email can be either in the query string, like &#x60;mailto:example@domain.com&#x60;, or in the User-Agent request header, like &#x60;User-Agent: my-app (mailto:example@domain.com)&#x60;. Read more about the polite pool at [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool). | [optional] 

### Return type

[**Topics**](Topics.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**403** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


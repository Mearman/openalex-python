# openalex_api.CombinedApi

All URIs are relative to *https://api.openalex.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_concept**](CombinedApi.md#get_concept) | **GET** /concepts/{id} | /concepts/{id}
[**get_concepts**](CombinedApi.md#get_concepts) | **GET** /concepts | /concepts
[**get_random_concept**](CombinedApi.md#get_random_concept) | **GET** /concepts/random | /concepts/random


# **get_concept**
> Concept get_concept(id, select=select, user_agent=user_agent, mailto=mailto)

/concepts/{id}

Get a single concept

### Example


```python
import time
import os
import openalex_api
from openalex_api.models.concept import Concept
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
    api_instance = openalex_api.CombinedApi(api_client)
    id = None # object | 
    select = 'select_example' # str |  (optional)
    user_agent = None # object | [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool) (optional)
    mailto = None # object | The API is the primary way to get OpenAlex data. It's free and requires no authentication. The daily limit for API calls is 100,000 requests per user per day. For best performance, add your email to all API requests The email can be either in the query string, like `mailto:example@domain.com`, or in the User-Agent request header, like `User-Agent: my-app (mailto:example@domain.com)`. Read more about the polite pool at [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool). (optional)

    try:
        # /concepts/{id}
        api_response = api_instance.get_concept(id, select=select, user_agent=user_agent, mailto=mailto)
        print("The response of CombinedApi->get_concept:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CombinedApi->get_concept: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 
 **select** | **str**|  | [optional] 
 **user_agent** | [**object**](.md)| [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool) | [optional] 
 **mailto** | [**object**](.md)| The API is the primary way to get OpenAlex data. It&#39;s free and requires no authentication. The daily limit for API calls is 100,000 requests per user per day. For best performance, add your email to all API requests The email can be either in the query string, like &#x60;mailto:example@domain.com&#x60;, or in the User-Agent request header, like &#x60;User-Agent: my-app (mailto:example@domain.com)&#x60;. Read more about the polite pool at [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool). | [optional] 

### Return type

[**Concept**](Concept.md)

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

# **get_concepts**
> ConceptsResponseSchema get_concepts(api_key=api_key, cursor=cursor, filter=filter, group_by=group_by, page=page, per_page=per_page, sample=sample, search=search, seed=seed, select=select, sort=sort, user_agent=user_agent, mailto=mailto)

/concepts



### Example


```python
import time
import os
import openalex_api
from openalex_api.models.concepts_response_schema import ConceptsResponseSchema
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
    api_instance = openalex_api.CombinedApi(api_client)
    api_key = 'api_key_example' # str |  (optional)
    cursor = 'cursor_example' # str |  (optional)
    filter = 'filter_example' # str |  (optional)
    group_by = 'group_by_example' # str |  (optional)
    page = 1 # int |  (optional)
    per_page = 3 # int |  (optional)
    sample = 56 # int |  (optional)
    search = 'search_example' # str |  (optional)
    seed = None # object |  (optional)
    select = 'select_example' # str |  (optional)
    sort = 'sort_example' # str |  (optional)
    user_agent = None # object | [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool) (optional)
    mailto = None # object | The API is the primary way to get OpenAlex data. It's free and requires no authentication. The daily limit for API calls is 100,000 requests per user per day. For best performance, add your email to all API requests The email can be either in the query string, like `mailto:example@domain.com`, or in the User-Agent request header, like `User-Agent: my-app (mailto:example@domain.com)`. Read more about the polite pool at [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool). (optional)

    try:
        # /concepts
        api_response = api_instance.get_concepts(api_key=api_key, cursor=cursor, filter=filter, group_by=group_by, page=page, per_page=per_page, sample=sample, search=search, seed=seed, select=select, sort=sort, user_agent=user_agent, mailto=mailto)
        print("The response of CombinedApi->get_concepts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CombinedApi->get_concepts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | [optional] 
 **cursor** | **str**|  | [optional] 
 **filter** | **str**|  | [optional] 
 **group_by** | **str**|  | [optional] 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 
 **sample** | **int**|  | [optional] 
 **search** | **str**|  | [optional] 
 **seed** | [**object**](.md)|  | [optional] 
 **select** | **str**|  | [optional] 
 **sort** | **str**|  | [optional] 
 **user_agent** | [**object**](.md)| [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool) | [optional] 
 **mailto** | [**object**](.md)| The API is the primary way to get OpenAlex data. It&#39;s free and requires no authentication. The daily limit for API calls is 100,000 requests per user per day. For best performance, add your email to all API requests The email can be either in the query string, like &#x60;mailto:example@domain.com&#x60;, or in the User-Agent request header, like &#x60;User-Agent: my-app (mailto:example@domain.com)&#x60;. Read more about the polite pool at [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool). | [optional] 

### Return type

[**ConceptsResponseSchema**](ConceptsResponseSchema.md)

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

# **get_random_concept**
> Concept get_random_concept(select=select, user_agent=user_agent, mailto=mailto)

/concepts/random

Get a random concept

### Example


```python
import time
import os
import openalex_api
from openalex_api.models.concept import Concept
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
    api_instance = openalex_api.CombinedApi(api_client)
    select = 'select_example' # str |  (optional)
    user_agent = None # object | [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool) (optional)
    mailto = None # object | The API is the primary way to get OpenAlex data. It's free and requires no authentication. The daily limit for API calls is 100,000 requests per user per day. For best performance, add your email to all API requests The email can be either in the query string, like `mailto:example@domain.com`, or in the User-Agent request header, like `User-Agent: my-app (mailto:example@domain.com)`. Read more about the polite pool at [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool). (optional)

    try:
        # /concepts/random
        api_response = api_instance.get_random_concept(select=select, user_agent=user_agent, mailto=mailto)
        print("The response of CombinedApi->get_random_concept:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CombinedApi->get_random_concept: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **select** | **str**|  | [optional] 
 **user_agent** | [**object**](.md)| [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool) | [optional] 
 **mailto** | [**object**](.md)| The API is the primary way to get OpenAlex data. It&#39;s free and requires no authentication. The daily limit for API calls is 100,000 requests per user per day. For best performance, add your email to all API requests The email can be either in the query string, like &#x60;mailto:example@domain.com&#x60;, or in the User-Agent request header, like &#x60;User-Agent: my-app (mailto:example@domain.com)&#x60;. Read more about the polite pool at [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool). | [optional] 

### Return type

[**Concept**](Concept.md)

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


# openalex_api.MultipleApi

All URIs are relative to *https://api.openalex.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_concepts**](MultipleApi.md#get_concepts) | **GET** /concepts | /concepts
[**get_domain_by_id**](MultipleApi.md#get_domain_by_id) | **GET** /domains/{id} | /domains/{id}
[**get_field_by_id**](MultipleApi.md#get_field_by_id) | **GET** /field/{id} | /fields/{id}
[**get_subfield_by_id**](MultipleApi.md#get_subfield_by_id) | **GET** /subfields/{id} | /subfields/{id}
[**get_topics**](MultipleApi.md#get_topics) | **GET** /topics | /topics


# **get_concepts**
> Concepts get_concepts(api_key=api_key, cursor=cursor, filter=filter, group_by=group_by, page=page, per_page=per_page, sample=sample, search=search, seed=seed, select=select, sort=sort, user_agent=user_agent, mailto=mailto)

/concepts



### Example


```python
import time
import os
import openalex_api
from openalex_api.models.concepts import Concepts
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
        print("The response of MultipleApi->get_concepts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MultipleApi->get_concepts: %s\n" % e)
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

[**Concepts**](Concepts.md)

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

# **get_domain_by_id**
> Domain get_domain_by_id(id, per_page=per_page, user_agent=user_agent, mailto=mailto)

/domains/{id}



### Example


```python
import time
import os
import openalex_api
from openalex_api.models.domain import Domain
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
    id = None # object | 
    per_page = 3 # int |  (optional)
    user_agent = None # object | [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool) (optional)
    mailto = None # object | The API is the primary way to get OpenAlex data. It's free and requires no authentication. The daily limit for API calls is 100,000 requests per user per day. For best performance, add your email to all API requests The email can be either in the query string, like `mailto:example@domain.com`, or in the User-Agent request header, like `User-Agent: my-app (mailto:example@domain.com)`. Read more about the polite pool at [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool). (optional)

    try:
        # /domains/{id}
        api_response = api_instance.get_domain_by_id(id, per_page=per_page, user_agent=user_agent, mailto=mailto)
        print("The response of MultipleApi->get_domain_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MultipleApi->get_domain_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 
 **per_page** | **int**|  | [optional] 
 **user_agent** | [**object**](.md)| [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool) | [optional] 
 **mailto** | [**object**](.md)| The API is the primary way to get OpenAlex data. It&#39;s free and requires no authentication. The daily limit for API calls is 100,000 requests per user per day. For best performance, add your email to all API requests The email can be either in the query string, like &#x60;mailto:example@domain.com&#x60;, or in the User-Agent request header, like &#x60;User-Agent: my-app (mailto:example@domain.com)&#x60;. Read more about the polite pool at [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool). | [optional] 

### Return type

[**Domain**](Domain.md)

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

# **get_field_by_id**
> Field get_field_by_id(id, per_page=per_page, user_agent=user_agent, mailto=mailto)

/fields/{id}



### Example


```python
import time
import os
import openalex_api
from openalex_api.models.field import Field
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
    id = None # object | 
    per_page = 3 # int |  (optional)
    user_agent = None # object | [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool) (optional)
    mailto = None # object | The API is the primary way to get OpenAlex data. It's free and requires no authentication. The daily limit for API calls is 100,000 requests per user per day. For best performance, add your email to all API requests The email can be either in the query string, like `mailto:example@domain.com`, or in the User-Agent request header, like `User-Agent: my-app (mailto:example@domain.com)`. Read more about the polite pool at [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool). (optional)

    try:
        # /fields/{id}
        api_response = api_instance.get_field_by_id(id, per_page=per_page, user_agent=user_agent, mailto=mailto)
        print("The response of MultipleApi->get_field_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MultipleApi->get_field_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 
 **per_page** | **int**|  | [optional] 
 **user_agent** | [**object**](.md)| [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool) | [optional] 
 **mailto** | [**object**](.md)| The API is the primary way to get OpenAlex data. It&#39;s free and requires no authentication. The daily limit for API calls is 100,000 requests per user per day. For best performance, add your email to all API requests The email can be either in the query string, like &#x60;mailto:example@domain.com&#x60;, or in the User-Agent request header, like &#x60;User-Agent: my-app (mailto:example@domain.com)&#x60;. Read more about the polite pool at [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool). | [optional] 

### Return type

[**Field**](Field.md)

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

# **get_subfield_by_id**
> Subfield get_subfield_by_id(id, per_page=per_page, user_agent=user_agent, mailto=mailto)

/subfields/{id}



### Example


```python
import time
import os
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
    id = None # object | 
    per_page = 3 # int |  (optional)
    user_agent = None # object | [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool) (optional)
    mailto = None # object | The API is the primary way to get OpenAlex data. It's free and requires no authentication. The daily limit for API calls is 100,000 requests per user per day. For best performance, add your email to all API requests The email can be either in the query string, like `mailto:example@domain.com`, or in the User-Agent request header, like `User-Agent: my-app (mailto:example@domain.com)`. Read more about the polite pool at [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool). (optional)

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
 **id** | [**object**](.md)|  | 
 **per_page** | **int**|  | [optional] 
 **user_agent** | [**object**](.md)| [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool) | [optional] 
 **mailto** | [**object**](.md)| The API is the primary way to get OpenAlex data. It&#39;s free and requires no authentication. The daily limit for API calls is 100,000 requests per user per day. For best performance, add your email to all API requests The email can be either in the query string, like &#x60;mailto:example@domain.com&#x60;, or in the User-Agent request header, like &#x60;User-Agent: my-app (mailto:example@domain.com)&#x60;. Read more about the polite pool at [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool). | [optional] 

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
import time
import os
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
    page = None # object |  (optional)
    sample = None # object |  (optional)
    select = 'select_example' # str |  (optional)
    filter = 'filter_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    group_by = 'group_by_example' # str |  (optional)
    user_agent = None # object | [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool) (optional)
    mailto = None # object | The API is the primary way to get OpenAlex data. It's free and requires no authentication. The daily limit for API calls is 100,000 requests per user per day. For best performance, add your email to all API requests The email can be either in the query string, like `mailto:example@domain.com`, or in the User-Agent request header, like `User-Agent: my-app (mailto:example@domain.com)`. Read more about the polite pool at [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool). (optional)

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
 **page** | [**object**](.md)|  | [optional] 
 **sample** | [**object**](.md)|  | [optional] 
 **select** | **str**|  | [optional] 
 **filter** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 
 **group_by** | **str**|  | [optional] 
 **user_agent** | [**object**](.md)| [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool) | [optional] 
 **mailto** | [**object**](.md)| The API is the primary way to get OpenAlex data. It&#39;s free and requires no authentication. The daily limit for API calls is 100,000 requests per user per day. For best performance, add your email to all API requests The email can be either in the query string, like &#x60;mailto:example@domain.com&#x60;, or in the User-Agent request header, like &#x60;User-Agent: my-app (mailto:example@domain.com)&#x60;. Read more about the polite pool at [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool). | [optional] 

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


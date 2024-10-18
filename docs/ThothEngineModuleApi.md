# upstudy_py_sdk.ThothEngineModuleApi

All URIs are relative to *https://api.cameramath.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_brief_answers_post**](ThothEngineModuleApi.md#v1_brief_answers_post) | **POST** /v1/brief-answers | Answers to all lists of each block
[**v1_show_steps_post**](ThothEngineModuleApi.md#v1_show_steps_post) | **POST** /v1/show-steps | All lists and all steps of all blocks
[**v1_single_answer_post**](ThothEngineModuleApi.md#v1_single_answer_post) | **POST** /v1/single-answer | First answer of the first block, text version


# **v1_brief_answers_post**
> V1BriefAnswersPost200Response v1_brief_answers_post(data)

Answers to all lists of each block

### Example

* Api Key Authentication (BearerAuth):

```python
import upstudy_py_sdk
from upstudy_py_sdk.models.request_solve_request_v1 import RequestSolveRequestV1
from upstudy_py_sdk.models.v1_brief_answers_post200_response import V1BriefAnswersPost200Response
from upstudy_py_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cameramath.com
# See configuration.py for a list of all supported configuration parameters.
configuration = upstudy_py_sdk.Configuration(
    host = "https://api.cameramath.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerAuth
configuration.api_key['BearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with upstudy_py_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = upstudy_py_sdk.ThothEngineModuleApi(api_client)
    data = upstudy_py_sdk.RequestSolveRequestV1() # RequestSolveRequestV1 | Solution request parameters

    try:
        # Answers to all lists of each block
        api_response = api_instance.v1_brief_answers_post(data)
        print("The response of ThothEngineModuleApi->v1_brief_answers_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThothEngineModuleApi->v1_brief_answers_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**RequestSolveRequestV1**](RequestSolveRequestV1.md)| Solution request parameters | 

### Return type

[**V1BriefAnswersPost200Response**](V1BriefAnswersPost200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Brief solution result |  -  |
**400** | Invalid request parameters |  -  |
**401** | Unauthorized, authentication failed |  -  |
**429** | Too many requests, rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_show_steps_post**
> V1ShowStepsPost200Response v1_show_steps_post(data)

All lists and all steps of all blocks

### Example

* Api Key Authentication (BearerAuth):

```python
import upstudy_py_sdk
from upstudy_py_sdk.models.request_solve_request_v1 import RequestSolveRequestV1
from upstudy_py_sdk.models.v1_show_steps_post200_response import V1ShowStepsPost200Response
from upstudy_py_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cameramath.com
# See configuration.py for a list of all supported configuration parameters.
configuration = upstudy_py_sdk.Configuration(
    host = "https://api.cameramath.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerAuth
configuration.api_key['BearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with upstudy_py_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = upstudy_py_sdk.ThothEngineModuleApi(api_client)
    data = upstudy_py_sdk.RequestSolveRequestV1() # RequestSolveRequestV1 | Solution request parameters

    try:
        # All lists and all steps of all blocks
        api_response = api_instance.v1_show_steps_post(data)
        print("The response of ThothEngineModuleApi->v1_show_steps_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThothEngineModuleApi->v1_show_steps_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**RequestSolveRequestV1**](RequestSolveRequestV1.md)| Solution request parameters | 

### Return type

[**V1ShowStepsPost200Response**](V1ShowStepsPost200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Full solution result |  -  |
**400** | Invalid request parameters |  -  |
**401** | Unauthorized, authentication failed |  -  |
**429** | Too many requests, rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_single_answer_post**
> V1SingleAnswerPost200Response v1_single_answer_post(data)

First answer of the first block, text version

### Example

* Api Key Authentication (BearerAuth):

```python
import upstudy_py_sdk
from upstudy_py_sdk.models.request_solve_request_v1 import RequestSolveRequestV1
from upstudy_py_sdk.models.v1_single_answer_post200_response import V1SingleAnswerPost200Response
from upstudy_py_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cameramath.com
# See configuration.py for a list of all supported configuration parameters.
configuration = upstudy_py_sdk.Configuration(
    host = "https://api.cameramath.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerAuth
configuration.api_key['BearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with upstudy_py_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = upstudy_py_sdk.ThothEngineModuleApi(api_client)
    data = upstudy_py_sdk.RequestSolveRequestV1() # RequestSolveRequestV1 | Solution request parameters

    try:
        # First answer of the first block, text version
        api_response = api_instance.v1_single_answer_post(data)
        print("The response of ThothEngineModuleApi->v1_single_answer_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThothEngineModuleApi->v1_single_answer_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**RequestSolveRequestV1**](RequestSolveRequestV1.md)| Solution request parameters | 

### Return type

[**V1SingleAnswerPost200Response**](V1SingleAnswerPost200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Simple solution result |  -  |
**400** | Invalid request parameters |  -  |
**401** | Unauthorized, authentication failed |  -  |
**429** | Too many requests, rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# SolverSelfBriefResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input** | **str** | User&#39;s Latex input | [optional] 
**solutions** | [**List[SolverSolution]**](SolverSolution.md) | All solutions we can provide | [optional] 

## Example

```python
from upstudy_py_sdk.models.solver_self_brief_response import SolverSelfBriefResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SolverSelfBriefResponse from a JSON string
solver_self_brief_response_instance = SolverSelfBriefResponse.from_json(json)
# print the JSON string representation of the object
print(SolverSelfBriefResponse.to_json())

# convert the object into a dict
solver_self_brief_response_dict = solver_self_brief_response_instance.to_dict()
# create an instance of SolverSelfBriefResponse from a dict
solver_self_brief_response_from_dict = SolverSelfBriefResponse.from_dict(solver_self_brief_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



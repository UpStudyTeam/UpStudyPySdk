# SolverStep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**children** | [**List[SolverStep]**](SolverStep.md) | Sub-steps, supplementing how this step is calculated to reach the next step | [optional] 
**description** | [**SolverDescription**](SolverDescription.md) | Description of the current step | [optional] 
**image_url** | **str** | If the current step is drawing, this URL shows the drawing result | [optional] 
**latex** | **str** | Latex display of the current step | [optional] 

## Example

```python
from upstudy_py_sdk.models.solver_step import SolverStep

# TODO update the JSON string below
json = "{}"
# create an instance of SolverStep from a JSON string
solver_step_instance = SolverStep.from_json(json)
# print the JSON string representation of the object
print(SolverStep.to_json())

# convert the object into a dict
solver_step_dict = solver_step_instance.to_dict()
# create an instance of SolverStep from a dict
solver_step_from_dict = SolverStep.from_dict(solver_step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



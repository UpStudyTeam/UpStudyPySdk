# SolverSolutionWithSolvingSteps


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_name** | [**SolverDescription**](SolverDescription.md) | Block name: e.g., Function/Solve the equation | [optional] 
**results** | [**List[SolverStep]**](SolverStep.md) | Results, possibly multiple, e.g., {\\frac{1}{4},0.25} | [optional] 
**solution_name** | [**SolverDescription**](SolverDescription.md) | Specific solution name under the block classification: e.g., Block: Function, Solution: Find the slope | [optional] 
**solving_steps** | [**List[SolverStep]**](SolverStep.md) | Steps to obtain the solution | [optional] 

## Example

```python
from upstudy_py_sdk.models.solver_solution_with_solving_steps import SolverSolutionWithSolvingSteps

# TODO update the JSON string below
json = "{}"
# create an instance of SolverSolutionWithSolvingSteps from a JSON string
solver_solution_with_solving_steps_instance = SolverSolutionWithSolvingSteps.from_json(json)
# print the JSON string representation of the object
print(SolverSolutionWithSolvingSteps.to_json())

# convert the object into a dict
solver_solution_with_solving_steps_dict = solver_solution_with_solving_steps_instance.to_dict()
# create an instance of SolverSolutionWithSolvingSteps from a dict
solver_solution_with_solving_steps_from_dict = SolverSolutionWithSolvingSteps.from_dict(solver_solution_with_solving_steps_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



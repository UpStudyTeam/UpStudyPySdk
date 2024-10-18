# SolverSolution


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_name** | [**SolverDescription**](SolverDescription.md) | Block name: e.g., Function/Solve the equation | [optional] 
**results** | [**List[SolverStep]**](SolverStep.md) | Results, possibly multiple, e.g., {\\frac{1}{4},0.25} | [optional] 
**solution_name** | [**SolverDescription**](SolverDescription.md) | Specific solution name under the block classification: e.g., Block: Function, Solution: Find the slope | [optional] 

## Example

```python
from upstudy_py_sdk.models.solver_solution import SolverSolution

# TODO update the JSON string below
json = "{}"
# create an instance of SolverSolution from a JSON string
solver_solution_instance = SolverSolution.from_json(json)
# print the JSON string representation of the object
print(SolverSolution.to_json())

# convert the object into a dict
solver_solution_dict = solver_solution_instance.to_dict()
# create an instance of SolverSolution from a dict
solver_solution_from_dict = SolverSolution.from_dict(solver_solution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



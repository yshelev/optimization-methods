import pandas as pd

def print_iterations(
	iterations_list: list
) -> None:
	dict_to_pd_adapter_dict = {
		"a": [iteration["a"] for iteration in iterations_list],
		"alpha": [iteration["alpha"] for iteration in iterations_list],
		"b": [iteration["b"] for iteration in iterations_list],
		"betta": [iteration["betta"] for iteration in iterations_list],
		"len": [iteration["len"] for iteration in iterations_list],
		"len_ratio": [-1] + [
			iterations_list[index + 1]["len"] / iterations_list[index]["len"]
			for index in range(len(iterations_list) - 1)
		]
	}

	iterations_data_frame = pd.DataFrame(
		dict_to_pd_adapter_dict
	)

	print(iterations_data_frame)

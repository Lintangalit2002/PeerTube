import json
import re

with open("analysis\code-complexity-audit\CodeComplexityReport.json", "r") as file:
    data = json.load(file)
data = data["reports"]
aggregated = {
    "total_files": len(data),
    "total_program_length": 0,
    "avg_program_length": 0,
    "total_program_volume": 0.0,
    "avg_program_volume": 0.0,
    "total_difficulty": 0.0,
    "avg_difficulty": 0.0,
    "total_effort": 0.0,
    "avg_effort": 0.0,
    "total_estimated_bugs": 0.0,
    "avg_estimated_bugs": 0.0,
    "total_time": 0.0,
    "avg_time": 0.0,
    "total_maintainability_index": 0.0,
    "avg_maintainability_index": 0.0,
    "total_cyclomatic_complexity": 0.0,
    "avg_cyclomatic_complexity": 0.0
}

for file, metrics in data.items():
    for metric in metrics:
        title = metric["title"]
        score = float(re.sub(r"[^\d.]", "", metric["score"]))

        if title == "Maintainability Index IM (%)":
            aggregated["total_maintainability_index"] += score
        elif title == "Cyclomatic Complexity":
            aggregated["total_cyclomatic_complexity"] += score
        elif title == "Program Length (N)":
            aggregated["total_program_length"] += score
        elif title == "Program Volume (V)":
            aggregated["total_program_volume"] += score
        elif title == "Difficulty Level (D)":
            aggregated["total_difficulty"] += score
        elif title == "Implementation Effort (E) or Understanding":
            aggregated["total_effort"] += score
        elif title == "Number of estimated bugs in a module or function (B)":
            aggregated["total_estimated_bugs"] += score
        elif title == "Time (T) to implement or understand the program":
            aggregated["total_time"] += score

if aggregated["total_files"] > 0:
    aggregated["avg_maintainability_index"] = aggregated["total_maintainability_index"] / aggregated["total_files"]
    aggregated["avg_cyclomatic_complexity"] = aggregated["total_cyclomatic_complexity"] / aggregated["total_files"]
    aggregated["avg_program_length"] = aggregated["total_program_length"] / aggregated["total_files"]
    aggregated["avg_program_volume"] = aggregated["total_program_volume"] / aggregated["total_files"]
    aggregated["avg_difficulty"] = aggregated["total_difficulty"] / aggregated["total_files"]
    aggregated["avg_effort"] = aggregated["total_effort"] / aggregated["total_files"]
    aggregated["avg_estimated_bugs"] = aggregated["total_estimated_bugs"] / aggregated["total_files"]
    aggregated["avg_time"] = aggregated["total_time"] / aggregated["total_files"]

output_file = "aggregated_metrics.json"
with open(output_file, "w") as file:
    json.dump(aggregated, file, indent=4)

print(f"Aggregated metrics saved to {output_file}")
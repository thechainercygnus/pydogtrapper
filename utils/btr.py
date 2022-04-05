import argparse
import json
import os
import pprint as pp
from typing import NamedTuple

COV_OBJECTS = ["coverage", "package", "class"]


class CoverageResults(NamedTuple):
    object_type: str
    object_name: str
    line_rate: float


class BTRXMLParseException(Exception):
    pass


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        usage="%(prog)s [options]",
        description="A basic test report parser",
        epilog="🍄 Bryce Jenkins",
    )
    parser.add_argument(
        "-p",
        "--project-root",
        action="store",
        help="root of the project to pull reports for",
        default=os.path.curdir,
    )
    parser.add_argument(
        "-r",
        "--results-path",
        action="store",
        help="path to tests folder",
        default="test-results/",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    test_result_path = os.path.join(args.project_root, args.results_path)
    results_file_list = os.listdir(test_result_path)
    report_content = {"Coverage": {}, "UnitTests": {}}
    for results_file in results_file_list:
        file_path = os.path.join(test_result_path, results_file)
        with open(file_path, "r") as results_reader:
            file_contents = results_reader.read().split("\n")
        for line in file_contents:
            # Grab Coverage
            line_elements = line.strip("\t").lstrip("<").rstrip(">").split(" ")
            _object_type = line_elements[0]
            if _object_type in COV_OBJECTS:
                _object_name = [
                    i.split("=")[1] for i in line_elements if i.startswith("name")
                ]
                if _object_type == "coverage":
                    _object_name = ["coverage"]
                _line_rate = [
                    i.split("=")[1] for i in line_elements if i.startswith("line-rate")
                ]
                if len(_object_name) != 1 or len(_line_rate) != 1:
                    raise BTRXMLParseException
                else:
                    report_content["Coverage"][_object_name[0]] = {
                        "type": _object_type,
                        "line-rate": float(_line_rate[0].strip('"')),
                    }
    with open("test-results.json", "w+") as report_writer:
        report_writer.write(json.dumps(report_content["Coverage"]))

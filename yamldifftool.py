# coding: utf-8
import yaml
import argparse
import sys


def traverse_and_set(user_provided, root_diff, path):
    k = root_diff
    for item in path[:-1]:
        if item not in k.keys():
            k[item] = {}
        k = k.get(item)
    k[path[-1]] = user_provided


def filter_defaults(base, user_provided, root_diff, path=[], strict=False):
    if type(user_provided) is dict:
        for key in user_provided.keys():
            if base is None:
                continue
            if type(base) is str:
                continue
            if not strict and key not in base.keys():
                traverse_and_set(user_provided.get(key), root_diff, path + [key])
            elif key in base.keys():
                filter_defaults(base.get(key), user_provided.get(key), root_diff, path=path + [key], strict=strict)
    elif type(user_provided) is list:
        if user_provided != base:
            traverse_and_set(user_provided, root_diff, path)
    else:
        if base != user_provided:
            traverse_and_set(user_provided, root_diff, path)

if __name__ == "__main__":
    root_diff = {}
    path = []

    parser = argparse.ArgumentParser(description="Tool to identify diffs between values.yaml and default")
    parser.add_argument("user_customized_values", metavar="customized.yaml", type=str, help="Customized values.yaml")
    parser.add_argument("-o", "--output", default=None, type=str,
                        help="Write to filename. If not specified, output is written to stdout.")
    parser.add_argument("-s", "--strict", default=False, action=argparse.BooleanOptionalAction, type=bool,
                        help="strict mode will drop all options not in default values.yaml.")
    parser.add_argument("-d", "--default_values", metavar="default_values.yaml", type=str,
                        help="Base values.yaml for the helm chart version you're using")
    parser.add_argument("-c", "--chart", type=str, help="Helm chart name")
    parser.add_argument("-v", "--version", type=str, help="Helm chart version")
    args = parser.parse_args()

    if args.default_values:
        with open(args.default_values, 'r') as default_values:
            default_v = yaml.safe_load(default_values)
    elif args.chart and args.version:
        import subprocess
        result = subprocess.run(
            ["helm", "show", "values", args.chart, "--version", args.version],
            capture_output=True, text=True, check=True
        )
        default_v = yaml.safe_load(result.stdout)
        print(type(default_v))
    else:
        raise ValueError("Either --default_values or both --chart and --version must be specified")

    with open(args.user_customized_values, 'r') as overwritten_values:
        overwritten_v = yaml.safe_load(overwritten_values)

    filter_defaults(default_v, overwritten_v, root_diff, path, args.strict)

    if args.output:
        with open(args.output, 'w') as outfile:
            yaml.dump(root_diff, outfile, sort_keys=False)
    else:
        yaml.dump(root_diff, sys.stdout, sort_keys=False)
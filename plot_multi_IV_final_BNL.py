#!/usr/bin/env python3
'''
Plot input noise after thermal cycling ATLAS ITk strips barrel modules
Updated by Amelia Stevens, Aug 2025

Usage:
    python plot_multi_IV_final_BNL.py -i 'BNL/ML/*/*.json'
'''

import os
import json
import argparse
import numpy as np
from glob import glob
from pprint import pprint

import matplotlib as mplt
mplt.use("Agg")
import matplotlib.pyplot as plt


def flatten(input_data):
    if isinstance(input_data, list) and all(isinstance(x, (int, float)) for x in input_data):
        return input_data
    elif isinstance(input_data, list) and all(isinstance(x, list) for x in input_data):
        return [item for sublist in input_data for item in sublist]
    else:
        raise TypeError(f"Expected list of floats or list of lists, got: {type(input_data)}")


def json_to_dict(file_path):
    with open(file_path, "r") as f:
        return json.load(f)


def mkdir(path):
    os.makedirs(path, exist_ok=True)


def normalize_serial(serial_number):
    if serial_number.startswith("SN"):
        return serial_number
    return f"SN{serial_number}"


def filter_input_files(infiles, keep_fit_code=4):
    print(f"Filtering to keep fit_type_code = {keep_fit_code}")

    filtered = []

    for f in infiles:
        try:
            data = json_to_dict(f)
            fit_type_code = data.get("properties", {}).get("fit_type_code")

            if fit_type_code == keep_fit_code:
                filtered.append(f)

        except Exception as e:
            print(f"❌ Could not read/filter {f}: {e}")

    return filtered


def get_module_names(files):
    modules = set()

    for f in files:
        try:
            data = json_to_dict(f)
            name = data["properties"]["det_info"]["name"]
            modules.add(name)
        except Exception as e:
            print(f"❌ Could not get module name from {f}: {e}")

    return sorted(modules)


def mk_inoise_plot(module_name, input_files, output_root, stream="under"):
    fig, ax = plt.subplots(figsize=(16, 9))

    print(f"\nPlotting input noise for {module_name}, stream: {stream}")

    files = sorted([f for f in input_files if module_name in json.dumps(json_to_dict(f))])
    n_files = len(files)

    if n_files == 0:
        print(f"⚠️ No files found for module {module_name}, stream {stream}")
        plt.close()
        return

    blues = mplt.cm.Blues(np.linspace(0.4, 0.9, n_files))
    oranges = mplt.cm.Oranges(np.linspace(0.4, 0.9, n_files))

    skipped_msgs = []
    timestamp_str = "Unknown"
    parent_name = "Unknown"

    for f in files:
        try:
            data = json_to_dict(f)
            raw_ts = data.get("timestamp", data.get("date", None))
            parent_name = data.get("parent_name", data.get("component", "Unknown"))

            if raw_ts:
                timestamp_str = raw_ts.replace("T", " ").split(".")[0].replace("Z", "").strip()
                break

        except Exception:
            continue

    for idx, f in enumerate(files):
        try:
            data = json_to_dict(f)

            result_key = "innse_under" if stream == "under" else "innse_away"
            noise = flatten(data["results"][result_key])

            mean_val = np.mean(noise)

            if mean_val > 1000:
                basename = os.path.basename(f)
                msg = f"{basename} — mean = {mean_val:.1f} > 1000"
                print(f"⚠️ Skipping {msg}")
                skipped_msgs.append(msg)
                continue

            temp = float(data["properties"]["DCS"]["AMAC_NTCpb"])
            temp_label = "+20C" if temp > 10 else "-35C"
            color = oranges[idx] if temp > 10 else blues[idx]

            basename = os.path.basename(f)
            file_number = basename.replace(".json", "").split("_")[-1]

            ax.plot(
                range(len(noise)),
                noise,
                lw=1,
                ls="-",
                c=color,
                label=f"{temp_label} file {file_number} [μ: {mean_val:.1f}]",
            )

        except Exception as e:
            basename = os.path.basename(f)
            msg = f"{basename} — {e}"
            print(f"❌ Skipping {msg}")
            skipped_msgs.append(msg)

    ax.set_xlim(0, 1280)
    ax.set_ylim(0, 2000)

    ax.set_xlabel("Channel number", labelpad=15, fontsize=38)
    ax.set_ylabel("Input noise [ENC]", labelpad=15, fontsize=38)
    ax.tick_params(axis="both", labelsize=28)
    ax.set_xticks(list(range(0, 1281, 128)))

    handles, labels = ax.get_legend_handles_labels()

    if handles:
        seen = set()
        unique = [
            (h, l)
            for h, l in zip(handles, labels)
            if not (l in seen or seen.add(l))
        ]

        ax.legend(
            *zip(*unique),
            loc="upper center",
            bbox_to_anchor=(0.5, 0.995),
            ncol=4,
            prop={"size": 15},
            frameon=False,
        )

    fig.text(0.15, 0.31, r"3 point gain response curve, $-$350V, times UTC", color="k", size=22)
    fig.text(0.15, 0.27, f"{module_name}, Stream: {stream}", color="k", size=28)
    fig.text(0.15, 0.23, f"Parent Module: {parent_name}", color="k", size=22)
    fig.text(0.15, 0.19, f"Timestamp: {timestamp_str}", color="k", size=22)

    for i, msg in enumerate(skipped_msgs):
        ypos = 0.14 - i * 0.035
        if ypos < 0.02:
            break
        fig.text(0.15, ypos, msg, color="red", size=16)

    plt.tight_layout(pad=0.3)
    plt.subplots_adjust(top=0.88, bottom=0.12, left=0.11, right=0.97)

    save_dir = os.path.join(output_root, "inputnoise")
    mkdir(save_dir)

    save_path = os.path.join(save_dir, f"{module_name}-{stream}.pdf")

    print(f"Saving: {save_path}")
    plt.savefig(save_path)
    plt.close()


def main():
    parser = argparse.ArgumentParser(
        description="Plot input noise after thermal cycling ATLAS ITk strips barrel modules"
    )

    parser.add_argument(
        "--serial_number",
        required=True,
        help="Example: 20USBHX2002099 or SN20USBHX2002099",
    )

    parser.add_argument(
        "--base_dir",
        default="BNL/HX",
        help="Base directory containing SN folders. Default: BNL/HX",
    )

    parser.add_argument(
        "-i",
        "--input",
        default="",
        help="Optional direct input glob, e.g. 'BNL/HX/SN20USBHX2002099/*.json'",
    )

    args = parser.parse_args()

    serial_sn = normalize_serial(args.serial_number)

    if args.input:
        pattern = args.input
    else:
        pattern = os.path.join(args.base_dir, serial_sn, f"{serial_sn}_*.json")

    input_files = sorted(glob(pattern))

    print(f"\nInput pattern:")
    print(pattern)

    print(f"\nFound {len(input_files)} files for serial: {serial_sn}")
    pprint(input_files)

    if not input_files:
        print("\n❌ No input JSON files found.")
        return

    filtered_files = filter_input_files(input_files)

    print("\nFiltered files:")
    pprint(filtered_files)

    if not filtered_files:
        print("\n❌ No files passed fit_type_code filtering.")
        return

    module_names = get_module_names(filtered_files)

    print("\nModules:")
    pprint(module_names)

    output_root = os.path.join(args.base_dir, serial_sn)

    for module_name in module_names:
        mk_inoise_plot(module_name, filtered_files, output_root, "under")
        mk_inoise_plot(module_name, filtered_files, output_root, "away")


if __name__ == "__main__":
    main()
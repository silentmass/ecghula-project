"""Utility functions for preparing HULA ECG .txt files for Kubios."""

import logging
import os
import sys

import pandas as pd
from tqdm import trange


def list_directory(input_path):
    """Prepared directory .txt files or prepare a single file

    Args:
        dir_path (str): Directory path or file path
    """
    txt_files = []
    if not os.path.exists(input_path):
        sys.exit("Input path doesn't exist")

    if os.path.isfile(input_path) and input_path.endswith(".txt"):
        # Handel single file
        dir_path = os.path.dirname(input_path)
        txt_files.append(os.path.basename(input_path))
    elif os.path.isdir(input_path):
        dir_path = input_path
        # Handle directory
        for file_name in os.listdir(os.path.abspath(dir_path)):
            if file_name.endswith(".txt"):
                txt_files.append(file_name)
    else:
        sys.exit("Not a .txt file or a directory")

    if not txt_files:
        sys.exit("No .txt files found.")
        
    print(txt_files)

    # Prepare files
    pbar = trange(len(txt_files))
    for idx in pbar:
        file_name = txt_files[idx]
        pbar.set_description(f"Processing file: {file_name}")
        file_path = os.path.join(dir_path, file_name)
        prepare_csv_data(file_path)


def get_largest_nan_index_format(value):
    """Format Nan value count for logging

    Args:
        value (int|Nan): Nan value count

    Returns:
        int|str: Formatted Nan value count
    """
    if pd.isna(value):
        return "No Nan values"
    else:
        return value


def get_logger(file_path):
    """Get logger for console and file

    Args:
        file_path (str): ECG .txt file path as a string

    Returns:
        Logger: Logger for console and file
    """
    logger_name = os.path.basename(file_path).replace(".txt", "")
    logger = logging.getLogger(name=logger_name)
    logger.setLevel(logging.INFO)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # File handler
    file_handler = logging.FileHandler(
        filename=(os.path.join(os.path.dirname(file_path),
                               f"{logger_name}.log")),
        mode="w"
    )
    file_handler.setLevel(logging.INFO)

    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger


def get_prepared_file_path(file_path):
    """Get prepared ECG .csv file path with postfix prepared

    Args:
        file_path (str): ECG .txt file path

    Returns:
        str: Prepared file path
    """
    file_name = os.path.basename(file_path)
    prepared_file_name = file_name.replace(".txt", "_prepared.csv")
    dir_name = os.path.dirname(file_path)
    prepared_file_path = os.path.join(dir_name, prepared_file_name)
    return prepared_file_path


def prepare_csv_data(file_path):
    """Get prepared ECG csv file for Kubios
    with Nan values filled with zeros

    Args:
        file_path (str): ECG .txt file path

    """
    logger = get_logger(file_path)

    logger.info(f"Reading file: {file_path}")

    # Check file format and structure to follow HULA format
    header = pd.read_csv(
        file_path,
        sep="\t",
        dtype=str,
        header=None,
        nrows=1
    )
    header_start = header.iloc[0].values[0]

    if not header_start.startswith("Interval"):
        logger.info("Couldn't identify as HULA ECG .txt file. "
                    + "File should start with Interval=. "
                    + "Skipping file.")
        return

    data = pd.read_csv(
        file_path,
        skiprows=6,
        names=["TIME", "ECG1", "ECG2", "HR1", "HR2", "EVENT"],
        sep="\t",
        dtype=str,
    )

    # Change commas to dots and format string to float
    for col in ["TIME", "ECG1", "ECG2"]:
        data[col] = data[col].str.replace(",", ".").astype(float)

    data = data.set_index("TIME")

    # Get filled Nan value counts
    (filled_nan_values_ecg1, filled_nan_values_ecg2) = (
        data[["ECG1", "ECG2"]].isna().sum().values
    )
    largest_nan_index_ecg1 = get_largest_nan_index_format(
        data[data["ECG1"].isna()].index.max()
    )
    largest_nan_index_ecg2 = get_largest_nan_index_format(
        data[data["ECG2"].isna()].index.max()
    )

    logger.info(
        f"""Filling Nan values:
CHANNEL\tFILLED\tLAST Nan TIME
ECG1\t{filled_nan_values_ecg1}\t{largest_nan_index_ecg1}
ECG2\t{filled_nan_values_ecg2}\t{largest_nan_index_ecg2}"""
    )

    # Fill Nan values
    data[["ECG1", "ECG2"]] = data[["ECG1", "ECG2"]].fillna(0)

    prepared_file_path = get_prepared_file_path(file_path)

    logger.info(f"Saving file: {prepared_file_path}")

    # Save prepared data
    data.to_csv(prepared_file_path)

    logger.info("Done!")

    del data

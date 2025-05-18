import csv
import os
import pytest


def load_user_credentials(filename="credentials.csv"):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    absolute_path = os.path.join(base_dir, filename)
    if not os.path.exists(absolute_path):
        raise FileNotFoundError(f"File not found: {absolute_path}")
    credentials = []
    with open(absolute_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            credentials.append((row['username'], row['password']))
    return credentials




def load_all_users_for_login_only():
    return [
        ("standard_user", "secret_sauce"),
        ("locked_out_user", "secret_sauce"),
        ("problem_user", "secret_sauce"),
        ("performance_glitch_user", "secret_sauce"),
        ("error_user", "secret_sauce"),
        ("visual_user", "secret_sauce"),
        ("invalid_user", "invalid_credentials")
    ]


def load_active_users_for_full_tests():
    return [
        ("standard_user", "secret_sauce"),
        ("problem_user", "secret_sauce"),
        ("performance_glitch_user", "secret_sauce"),
        ("error_user", "secret_sauce"),
        ("visual_user", "secret_sauce")
    ]


def load_checkout_valid_users():
    return [
        ("standard_user", "secret_sauce"),
        ("performance_glitch_user", "secret_sauce"),
        ("error_user", "secret_sauce"),
        ("visual_user", "secret_sauce")
    ]

def load_performance_valid_users():
    return [
        ("standard_user", "secret_sauce"),
        ("performance_glitch_user", "secret_sauce"),
        ("visual_user", "secret_sauce")
    ]
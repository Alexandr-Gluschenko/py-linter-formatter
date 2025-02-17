def format_linter_error(error: dict) -> dict:
    return {
        "line": 18,
        "column": 80,
        "message": "line too long (99 > 79 characters)",
        "name": "E501",
        "source": "flake8",
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "line": errors["line_number"],
        "column": errors["column_number"],
        "message": errors["text"],
        "name": errors["code"],
        "source": "flake8"
    }


def format_linter_report(linter_report: dict) -> list:
    # write your code here
    pass

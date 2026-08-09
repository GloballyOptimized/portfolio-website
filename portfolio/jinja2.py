from jinja2 import Environment


def format_number(value):
    try:
        return f"{int(value):,}"
    except (TypeError, ValueError):
        return value


def environment(**options):
    env = Environment(**options)
    env.filters["format_number"] = format_number
    return env

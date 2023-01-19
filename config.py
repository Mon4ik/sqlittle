from rich import box

# Style of table
# Default: `box.ROUNDED` (rounded corners)
TABLE_BOX_STYLE = box.ROUNDED

# Auto save on INSERT, CREATE TABLE, etc...
# Default: `True`
AUTO_COMMIT = True

# Style table
# Default: `{ "python's type": "color name" }`
TABLE_STYLES = {
    "str": "green",
    "int": "blue",
    "float": "blue",
    "boolean": "dark_orange",
    "bytes": "light_green"
}
# Parquet Metadata Viewer

A simple Python CLI tool to view metadata of Parquet files.

## Installation

Requires Python 3.10 or higher.

```bash
# Clone the repository
git clone <repository-url>
cd parquet

# Install dependencies using uv (recommended)
uv add pyarrow typer parquet-tools
```

## Usage

To view the metadata of a Parquet file:

```bash
python main.py <parquet-file-path>
```

### Example Output

```
created_by: github.com/parquet-go/parquet-go version 0.24.0(build )
num_columns: 7
num_rows: 2
num_row_groups: 1
format_version: 2.6
serialized_size: 721
```

### Metadata Fields

- `created_by`: The library or tool that created the Parquet file
- `num_columns`: Number of columns in the dataset
- `num_rows`: Total number of rows in the dataset
- `num_row_groups`: Number of row groups in the file
- `format_version`: Parquet format version
- `serialized_size`: Size of the serialized metadata in bytes
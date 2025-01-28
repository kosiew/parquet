#!/usr/bin/env python3

import typer
import pyarrow.parquet as pq
from typing import Optional

app = typer.Typer()

@app.command()
def show_metadata(file_path: str):
    """Display metadata of a Parquet file."""
    try:
        # Open the parquet file
        parquet_file = pq.ParquetFile(file_path)
        metadata = parquet_file.metadata
        
        # Extract and display metadata
        print(f"created_by: {metadata.created_by}")
        print(f"num_columns: {metadata.num_columns}")
        print(f"num_rows: {metadata.num_rows}")
        print(f"num_row_groups: {metadata.num_row_groups}")
        print(f"format_version: {metadata.format_version}")
        print(f"serialized_size: {metadata.serialized_size}")
        
    except Exception as e:
        typer.echo(f"Error reading parquet file: {str(e)}", err=True)
        raise typer.Exit(1)

if __name__ == "__main__":
    app()
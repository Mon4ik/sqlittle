import sys

from rich.console import Console
from rich.table import Table

import config
import sqlite3
import argparse
import readline

console = Console()


def main(args: argparse.Namespace):
    try:
        conn = sqlite3.connect(args.database)
        cursor = conn.cursor()
    except sqlite3.Error as e:
        console.print(f"[red] Raised error while connecting: {e.sqlite_errorname} ({e.sqlite_errorcode})")
        return

    console.print("Welcome to SQLittle!")
    console.print(".exit - Exit; .help - Help menu")

    while True:
        try:
            sql = input("sqlittle> ")
            while not sql.strip().endswith(";"):
                add_line = input("........> ")
                sql += f"\n{add_line}"

            console.print("")
            cursor.execute(sql)

            first_q = cursor.fetchone()
            if first_q is not None:
                queried = [first_q] + cursor.fetchall()
                # draw table
                table = Table(title=sql.replace('\n', ' ')[:16] + "...", box=config.TABLE_BOX_STYLE)
                for i, name in enumerate(map(lambda x: x[0], cursor.description)):
                    table.add_column(name, style=config.TABLE_STYLES[type(first_q[i]).__name__])

                for q in queried:
                    table.add_row(*list(map(str, q)))

                console.print(table)
            else:
                if config.AUTO_COMMIT:
                    conn.commit()
        except sqlite3.OperationalError as e:
            console.print(f"[red]Error: [bold]{e}")
        except KeyboardInterrupt or EOFError:
            conn.close()
            exit(0)


def parseArgs():
    parser = argparse.ArgumentParser("SQLittle")
    parser.add_argument("database", help="Path to .sqlite database")
    args = parser.parse_args(sys.argv[1:])

    main(args)

if __name__ == '__main__':
    parseArgs()
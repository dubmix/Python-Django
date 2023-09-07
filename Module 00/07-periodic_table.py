#!/usr/bin/python3

def main():
    HTML = """
    <!DOCTYPE html>
    <head>
        <title>periodic_table</title>
        <style>
            table {{
                border-collapse: collapse;
            }}
            h4 {{
                text-align: center;
            }}
            body{{
                font-family: "Futura", sans-serif;
            }}
        </style>
    </head>
    <body>
        <h1>Mendeleiev's Table</h1>
        <table>
            {body}
        </table>
    </body>
    </html>
    """

    TEMPLATE = """
            <td style="border: 2px solid black; padding: 5px">
                <h4>{name}</h4>
                <u1>
                    <li>No {number}</li>
                    <li>{small}</li>
                    <li>{molar}</li>
                    <li>{electron} electron</li>
                </u1>
            </td>
        """

    body = "<tr>"
    f = open("periodic_table.txt", "r")
    periodic_table = f.readlines()
    f.close()
    i = 0
    while i < 2:
        body += TEMPLATE.format(
            name = "lol",
            number = "42",
            small = "L",
            molar = "10.78",
            electron = "2 3",
        )
        i += 1
    body += "</tr>\n"
    f = open("periodic_table.html", "w")
    f.write(HTML.format(body=body))
    f.close()

if __name__ == '__main__':
    main()
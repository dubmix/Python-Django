#!/usr/bin/python3

def parse_line(line: str):
    element = line.split("=")
    result = dict((value.strip().split(":") for value in element[1].split(", ")))
    result["name"] = element[0].strip()
    return result

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
            body {{
                font-family: "Futura", sans-serif;
            }}
            .title-container {{
                text-align:center;
                padding:20px;
                width: 100%;
                top: 0;
            }}
            h1 {{
                margin: 0;
            }}
        </style>
    </head>
    <body>
        <div class="title-container">
            <h1>Mendeleiev's Table</h1>
        </div>
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
                    <li>{electron}</li>
                </u1>
            </td>
        """

    body = "<tr>"
    f = open("periodic_table.txt", "r")
    periodic_table = [(parse_line(line)) for line in f.readlines()]
    f.close()
    pos = 0
    for dic in periodic_table:
        if pos > int(dic["position"]):
            body += "    </tr>\n    <tr>"
            pos = 0
        for _ in range(pos, int(dic["position"]) - 1):
            body += "      <td></td>\n"
        pos = int(dic["position"])
        body += TEMPLATE.format(
            name = dic["name"],
            number = dic["number"],
            small = dic["small"],
            molar = dic["molar"],
            electron = dic["electron"],
        )
    body += "    </tr>\n"
    f = open("periodic_table.html", "w")
    f.write(HTML.format(body=body))
    f.close()

if __name__ == '__main__':
    main()
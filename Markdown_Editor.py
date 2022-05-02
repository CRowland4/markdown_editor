commands = [
    '!help',
    '!done',
    'plain',
    'bold',
    'italic',
    'header',
    'link',
    'inline-code',
    'new-line',
    'ordered-list',
    'unordered-list'
]

outputs = []


def get_formatter():
    formatter = input("Choose a formatter: ")
    return formatter


def format_new_line():
    markdown = '\n'
    outputs.append(markdown)
    print("".join(outputs))


def format_plain():
    markdown = input("Text: ")
    outputs.append(markdown)
    print("".join(outputs))


def format_bold():
    text = input("Text: ")
    markdown = "**" + text + "**"
    outputs.append(markdown)
    print("".join(outputs))


def format_italic():
    text = input("Text: ")
    markdown = "*" + text + "*"
    outputs.append(markdown)
    print("".join(outputs))


def format_inline_code():
    text = input("Text: ")
    markdown = "`" + text + "`"
    outputs.append(markdown)
    print("".join(outputs))


def format_header():
    level = int(input("Level: "))
    if not (1 <= level <= 6):
        print("The level should be within the range of 1 to 6")
    else:
        text = input("Text: ")
        markdown = ('#' * level) + ' ' + text + '\n'
        outputs.append(markdown)
        print("".join(outputs))


def format_link():
    label = input("Label: ")
    url = input("URL: ")
    markdown = f'[{label}]({url})'
    outputs.append(markdown)
    print("".join(outputs))


def format_list(list_type):
    row_count = int(input("Number of rows: "))
    if row_count <= 0:
        print("The number of rows should be greater than zero")
        return format_list(list_type)

    if list_type == 'ordered-list':
        for i in range(1, row_count + 1):
            element_i = input(f'Row #{i}: ')
            row = f'{i}. ' + element_i + '\n'
            outputs.append(row)
    elif list_type == 'unordered-list':
        for i in range(1, row_count + 1):
            element_i = input(f'Row #{i}: ')
            row = '* ' + element_i + '\n'
            outputs.append(row)

    for output in outputs:
        print(output, sep='', end='')

    print('')


def execute(command):
    while True:
        if command == '!help':
            print("""Available formatters: plain bold italic header link inline-code new-line
            Special commands: !help !done""")
            return execute(get_formatter())
        elif command == '!done':
            save = open('output.md', 'w')
            for output in outputs:
                save.write(output)
            save.close()
            break
        elif command == 'plain':
            format_plain()
            return execute(get_formatter())
        elif command == 'bold':
            format_bold()
            return execute(get_formatter())
        elif command == 'italic':
            format_italic()
            return execute(get_formatter())
        elif command == 'inline-code':
            format_inline_code()
            return execute(get_formatter())
        elif command == 'link':
            format_link()
            return execute(get_formatter())
        elif command == 'header':
            format_header()
            return execute(get_formatter())
        elif command == 'new-line':
            format_new_line()
            return execute(get_formatter())
        elif 'list' in command:
            format_list(command)
            return execute(get_formatter())
        else:
            print("Unknown formatting type or command")
            return execute(get_formatter())


execute(get_formatter())

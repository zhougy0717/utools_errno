import json
import re


def is_empty_line(line):
    pattern = r'^\s*$'  # 匹配只包含空白字符的行
    return re.match(pattern, line) is not None


def is_digit_line(line):
    pattern = r'^\s*\d+\s*$'  # 匹配只包含空白字符的行
    return re.match(pattern, line) is not None


if __name__ == '__main__':
    items = []
    with open('./openssl_tls_error', 'r') as f:
        lines = f.readlines()
        i = 0
        while i < len(lines):
            line = lines[i]
            if is_empty_line(line):
                i += 1
                continue
            if is_digit_line(line):
                item = {
                    'errno': line.strip(),
                    'title': lines[i + 2].strip(),
                    'description': lines[i + 4].strip(),
                    'icon': 'icons/tls.png'
                }
                i += 5
                items.append(item)
            else:
                i += 1

    with open('../openssl_tls_errno.json', 'w', encoding='utf-8') as out:
        json.dump(items, out, ensure_ascii=False, indent=4)
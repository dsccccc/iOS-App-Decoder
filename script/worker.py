def replacer(line: str, input_file: str = './tmp/README.md', output_file: str = 'README.md'):
    with open(input_file, 'r') as f:
        data = f.read()
    data = data.rstrip('\n') + f'\n|{line.split('🆓')[0]|🆓 {line.split('🆓')[1]|}'
    with open(output_file, 'w') as f:
        f.write(data)


if __name__ == '__main__':
    from src.decoder import AppStore
    app = AppStore()
    app.crawler()
    requests.post('https://ntfy.sh/ios-app-free-for-a-limited-time', data=app.content.encode(encoding='utf-8'))
    replacer(app.content)

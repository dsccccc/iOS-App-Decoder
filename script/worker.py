import emoji

def replacer(line: str, input_file: str = './tmp/README.md', output_file: str = 'README.md'):
    with open(input_file, 'r') as f:
        data = f.read()
    print(line)
    data = data.rstrip('\n') + f'\n|{line[:emoji.emoji_list('🆓')[0]['match_start']]}|🆓{line[emoji.emoji_list('🆓')[0]['match_end']:]}|'
    with open(output_file, 'w') as f:
        f.write(data)


if __name__ == '__main__':
    from src.decoder import AppStore
    app = AppStore()
    app.crawler()
    requests.post('https://ntfy.sh/ios-app-free-for-limited-time', data=app.content.encode('UTF-8'))
    replacer(app.content, input_file='./README.md')

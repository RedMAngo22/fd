import requests

if len(prompt) == 1:
    print('rget: usage: rget <url|--help> [arg]')
elif len(prompt) == 2:
    if prompt[1] == "--help":
        print("""
        rget - Make simple HTTP requests
        ----------
        args:
        url               - The url to get
        --help            - Displays this message
        --include-headers - Includes HTTP headers
        --user-agent      - Uses a custom User-Agent
        """)
    else:
        spinner.start("Getting url " + prompt[1])
        r = requests.get(prompt[1])
        spinner.stop()
        print("Response code: {}\n".format(r.status_code))
        print(r.text)
elif len(prompt) > 2:
    headers = {}
    if "--user-agent" in prompt:
        headers['User-Agent'] = input("Enter user-agent: ")
    spinner.start("Getting url " + prompt[1])
    r = requests.get(prompt[1], headers=headers)
    spinner.stop()
    print("Response code: {}\n".format(r.status_code))
    if "--include-headers" in prompt:
        print("Headers:")
        for h in r.headers.keys():
            print("  {0}: {1}".format(h, r.headers[h]))
        print("")
    print(r.text)

from requests_html import AsyncHTMLSession

async def get_ip():
    asession = AsyncHTMLSession()
    r = await asession.get('https://ip.seeip.org/jsonip?')
    return str(r.json()["ip"])

def main():
    session = AsyncHTMLSession()
    ip = str(session.run(get_ip))[2:-2]
    print("Az Ön IP címe: "+ip)


if __name__ == '__main__':
    main()
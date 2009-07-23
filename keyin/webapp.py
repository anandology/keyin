import web

urls = (
    "/hello/(.*)", "hello"
)

app = web.application(urls, globals())

class hello:
    def GET(self, name):
        web.header('Content-Type', 'text/plain')
        return "hello " + name

if __name__ == "__main__":
    app.run()

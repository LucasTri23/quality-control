from app import create_app
local_host = '0.0.0.0'
#private ip aws instance
remote_host = '172.31.24.18'
app = create_app()
if __name__ == '__main__':
        # app.run(host=local_host, port=8080, debug=True)
        app.run()
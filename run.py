from app import app
local_host = '0.0.0.0'
#private ip aws instance
remote_host = '172.31.24.18'
if __name__ == '__main__':
        app.run(host=local_host, port=443, debug=True)
from app import app
import ssl

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain(certfile='cert.pem', keyfile='key.pem')

if __name__ == '__main__':
    app.run(debug=True, port=5000, threaded=True, host='0.0.0.0', ssl_context=context)
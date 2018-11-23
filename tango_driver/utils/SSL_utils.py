import os
import random
# from OpenSSL import crypto
import socket


# def create_ssl_certificate(key_file, cert_file):
#     '''
#         Generate a new pair of SSL KEY and CER files.
#     '''
#     host_name = socket.gethostname()

#     key = crypto.PKey()
#     key.generate_key(crypto.TYPE_RSA, 2048)

#     cer = crypto.X509()
#     cer.get_subject().C = 'XX'
#     cer.get_subject().ST = 'None'
#     cer.get_subject().L = 'None'
#     cer.get_subject().O = 'Infosys'
#     cer.get_subject().OU = 'Auto-generated Certificate'
#     cer.get_subject().CN = host_name

#     cer.set_serial_number(random.randint(1000, 9999))
#     cer.gmtime_adj_notBefore(0)

#     # Set validity for 5 Years (in Seconds)
#     cer.gmtime_adj_notAfter(5 * 365 * 24 * 3600)

#     cer.set_issuer(cer.get_subject())
#     cer.set_pubkey(key)

#     # SIgn with SHA256 algorithm
#     cer.sign(key, 'sha256')

#     # write the Cert file
#     with open(cert_file, "wb") as cert_file_obj:
#         cert_file_obj.write(crypto.dump_certificate(crypto.FILETYPE_PEM, cer))

#     # write the key file
#     with open(key_file, "wb") as key_file_obj:
#         key_file_obj.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, key))

from uvicorn.workers import UvicornWorker
import gunicorn
from gunicorn import config
from uvicorn.workers import UvicornWorker


class DevUvicornWorker(UvicornWorker):
    CONFIG_KWARGS = {"loop": "uvloop", "http": "httptools", "lifespan": "off"}

wsgi_app: None
bind: ['unix:/tmp/eCom.sock']
backlog: 1024
workers: 6
#worker_class: uvicorn.workers.UvicornWorker
worker_class: DevUvicornWorker
threads: 24
worker_connections: 1000
max_requests: 10860
max_requests_jitter: 0
timeout: 30
graceful_timeout: 30
keepalive: 2
limit_request_line: 4094
limit_request_fields: 100
limit_request_field_size: 8190
reload: False
reload_extra_files: []
spew: False
check_config: False
print_config: False
preload_app: True
sendfile: None
reuse_port: False
chdir: ['/app/website']
daemon: False
raw_env: []
pidfile: ['/tmp/gunicorn.pid']
worker_tmp_dir: ['/tmp']
user: 101
group: 101
umask: 0
initgroups: False
tmp_upload_dir: ['/tmp/upload']
#secure_scheme_headers: {'X-FORWARDED-PROTOCOL': 'ssl', 'X-FORWARDED-PROTO': 'https', 'X-FORWARDED-SSL': 'on'}
#forwarded_allow_ips: ['127.0.0.1']
accesslog: ['/proc/self/fd/1']
disable_redirect_access_to_syslog: False
access_log_format: '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
errorlog: ['/proc/self/fd/2']
loglevel: 6
capture_output: False
logger_class: gunicorn.glogging.Logger
logconfig: None
logconfig_dict: {}
logconfig_json: None
syslog_addr: ['udp://localhost:514']
syslog: False
syslog_prefix: None
syslog_facility: user
enable_stdio_inheritance: False
statsd_host: None
proc_name: None
default_proc_name: ['app:app']
pythonpath: ['/home/starlette/.python/bin/python']
paste: None
proxy_protocol: False
#proxy_allow_ips: ['127.0.0.1']
#keyfile: None
#certfile: None
#ssl_version: 2
#cert_reqs: 0
#ca_certs: None
suppress_ragged_eofs: True
do_handshake_on_connect: False
ciphers: None
raw_paste_global_conf: []
strip_header_spaces: True

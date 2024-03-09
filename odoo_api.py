import xmlrpc.client as xmlrpclib
import ssl

url = ''
database = ''
password = ''
uid = ''
object = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url), context=ssl._create_unverified_context())

object.execute_kw(
    database,
    uid,
    password,
    'model',
    'search_read',
    [[[['field', '=', 'value']]]],
    {'fields': []}
)

object.execute_kw(
    database,
    uid,
    password,
    'model',
    'create',
    [{
        
    }]
)

object.execute_kw(
    database,
    uid,
    password,
    'model',
    'write',
    [[], {'fields': 'value'}],
)
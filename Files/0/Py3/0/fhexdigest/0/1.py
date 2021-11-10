def fhexdigest(filepath, algorithm = 'sha1'):
    exec('from hashlib import ' + algorithm + ' as algo\n')
    with open(filepath, 'rb') as f:
        return eval('algo')(f.read()).hexdigest()

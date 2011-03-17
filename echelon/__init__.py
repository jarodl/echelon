"""
Echelon
=======
"""

try:
    VERSION = __import__('pkg_resources')\
        .get_distribution('Echelon').version
except:
    VERSION = 'unknown'

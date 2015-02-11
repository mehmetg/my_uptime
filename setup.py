import sys
from setuptools import setup

__version__ = ''
with open('my_uptime/__init__.py') as inp:
  for line in inp:
      if (line.startswith('__version__')):
          exec(line.strip())
          break

setup(	name='my_uptime',
		version='0.01',
		description='Uptime for linux',
		long_description = 'Uptime for linux long',
		url='http://github.com/mehmetg/uptime',
		author='Mehmet Gerceker',
		author_email='mehmetg@msn.com',
		license='MIT',
		packages=['my_uptime'],
		package_dir={'my_uptime': 'my_uptime'},
		#package_data={'my_uptime': []},
		keywords=(),
		classifiers=[
	                 'Development Status :: 1 - Alpha',
	                 'Topic :: Software Development :: Tools',
	                 'License :: OSI Approved :: MIT License',
	                 'Operating System :: MacOS',
	                 #'Operating System :: Microsoft :: Windows',
	                 #'Operating System :: POSIX',
	                 'Programming Language :: Python',
	                 'Programming Language :: Python :: 2',
	                 'Programming Language :: Python :: 3',
                	],
      	provides=['my_uptime ({0:s})'.format(__version__)], 
      	requires=[],
      	#message_extractors={},
      	entry_points = {
      		'console_scripts': [
      			'my_uptime = my_uptime.my_uptime:main',
      			'my_uptime%s = my_uptime.my_uptime:main' % sys.version_info[0],
      		],
      		'distutil.commands': [
      			'my_uptime = my_uptime:main'
      		],
      	},
		zip_safe=False,
		test_suite = 'my_uptime_tests',
		test_require = [],
		#test_loader = '',
		)
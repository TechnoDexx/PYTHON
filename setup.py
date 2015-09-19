from distutils.core import setup

setup(
    name='PYTHON',
    version='.0.1',
    packages=['libs', 'Test', 'build.lib.libs', 'build.lib.Test', 'build.bdist.win32.msi.Lib.site-packages.libs',
              'build.bdist.win32.msi.Lib.site-packages.Test'],
    url='http://',
    license='',
    author='Owner',
    author_email='itshark@mail.ru',
    description='', requires=['pyodbc']
)

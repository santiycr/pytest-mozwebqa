from setuptools import setup

setup(name='pytest-mozwebqa',
      version='1.0',
      description='Mozilla WebQA plugin for py.test.',
      author='Dave Hunt',
      author_email='dhunt@mozilla.com',
      url='https://github.com/davehunt/pytest-mozwebqa',
      py_modules=[
        'pytest_mozwebqa.pytest_mozwebqa',
        'pytest_mozwebqa.credentials',
        'pytest_mozwebqa.html_report',
        'pytest_mozwebqa.selenium_client',
        'pytest_mozwebqa.sauce_labs'],
      install_requires=['pytest>=2.2.4', 'selenium>=2.21.0', 'pyyaml', 'requests'],
      entry_points={'pytest11': ['pytest_mozwebqa = pytest_mozwebqa.pytest_mozwebqa']},
      license='Mozilla Public License 2.0 (MPL 2.0)',
      keywords='py.test pytest selenium saucelabs mozwebqa webqa qa mozilla',
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing',
        'Topic :: Utilities',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7'])

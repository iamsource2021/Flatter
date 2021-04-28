from setuptools import setup

setup(name='flatter',
      version='0.1',
      description='can flatten nested array',
      url='https://github.com/iamsource2021/Flatter.git',
      author='Eduardo Ortiz',
      author_email='eduardooa1980@gmail.com',
      license='MIT',
      include_package_data=True,
      test_suite='nose2.collector.collector',
      install_requires=['underscore.py'],
      zip_safe=False)
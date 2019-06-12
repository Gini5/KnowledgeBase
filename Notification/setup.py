from setuptools import setup

setup(name='testnotification',
      version='1.0',
      description='Notify missed tests',
      author='Gini.Hu',
      author_email='gini.hu@intel.com',
      license='MIT',
      install_requires=[
          'configparser',
      ],
      zip_safe=False)
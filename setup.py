from setuptools import setup, find_packages

setup(
        author='Ana Nelson',
        author_email='ana@ananelson.com',
        classifiers=[
            "Development Status :: 4 - Beta",
            "Environment :: Console",
            "Intended Audience :: Developers",
            "Intended Audience :: Education",
            "Intended Audience :: Financial and Insurance Industry",
            "Intended Audience :: Science/Research",
            "License :: OSI Approved :: MIT License",
            "Topic :: Documentation",
            "Topic :: Software Development :: Build Tools",
            "Topic :: Software Development :: Code Generators",
            "Topic :: Software Development :: Documentation",
            "Topic :: Text Processing",
            "Topic :: Text Processing :: Markup :: HTML",
            "Topic :: Text Processing :: Markup :: LaTeX"
            ],
        description='Templates for the Getting Started dexy examples.',
        include_package_data = True,
        install_requires = [
            'dexy>=0.9.7'
            ],
        name='dexy_getting_started',
        packages=find_packages(),
        url='http://dexy.it',
        version="0.0.1"
        )
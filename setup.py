from setuptools import setup

setup(
    name="scrapy-deltafetch",
    version="1.2.1",
    license="BSD",
    description="Scrapy middleware to ignore previously crawled pages",
    author="Scrapinghub",
    author_email="info@scrapinghub.com",
    url="http://github.com/scrapy-plugins/scrapy-deltafetch",
    packages=["scrapy_deltafetch"],
    platforms=["Any"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    install_requires=["Scrapy>=2.3.0", "bsddb3"],
)

# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "swagger_server"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["connexion"]

setup(
    name=NAME,
    version=VERSION,
    description="Computer Vision API (v3.2)",
    author_email="",
    url="",
    keywords=["Swagger", "Computer Vision API (v3.2)"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['swagger_server=swagger_server.__main__:main']},
    long_description="""\
    The Computer Vision API provides state-of-the-art algorithms to process images and return information.  For example, it can be used to determine if an image contains mature content, or it can be used to find all the faces in an image.  It also has other features like estimating dominant and accent colors, categorizing the content of images, and describing an image with complete English sentences.  Additionally, it can also intelligently generate images thumbnails for displaying large images effectively.    This API is currently available in:    * Australia East - australiaeast.api.cognitive.microsoft.com  * Brazil South - brazilsouth.api.cognitive.microsoft.com  * Canada Central - canadacentral.api.cognitive.microsoft.com  * Central India - centralindia.api.cognitive.microsoft.com  * Central US - centralus.api.cognitive.microsoft.com  * East Asia - eastasia.api.cognitive.microsoft.com  * East US - eastus.api.cognitive.microsoft.com  * East US 2 - eastus2.api.cognitive.microsoft.com  * France Central - francecentral.api.cognitive.microsoft.com  * Japan East - japaneast.api.cognitive.microsoft.com  * Japan West - japanwest.api.cognitive.microsoft.com  * Korea Central - koreacentral.api.cognitive.microsoft.com  * North Central US - northcentralus.api.cognitive.microsoft.com  * North Europe - northeurope.api.cognitive.microsoft.com  * South Africa North - southafricanorth.api.cognitive.microsoft.com  * South Central US - southcentralus.api.cognitive.microsoft.com  * Southeast Asia - southeastasia.api.cognitive.microsoft.com  * UK South - uksouth.api.cognitive.microsoft.com  * West Central US - westcentralus.api.cognitive.microsoft.com  * West Europe - westeurope.api.cognitive.microsoft.com  * West US - westus.api.cognitive.microsoft.com  * West US 2 - westus2.api.cognitive.microsoft.com
    """
)


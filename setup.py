import setuptools

setuptools.setup(

    name="blurdetection",

    version="0.1.0",

    url="https://github.com/nhiq/blur-detection",

    author="Nhi Nguyen",

    author_email="email@email.com",

    description="Detect blur in images using Haar wavelets.",

    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=["cv2", "numpy", "pywt"],

    classifiers=[

        'Programming Language :: Python',

        'Programming Language :: Python :: 3',

        'Programming Language :: Python :: 3.6',

    ],

)

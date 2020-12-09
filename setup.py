import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="GinVPN-Zokontech", # Replace with your own username
    version="0.0.11",
    author="Zander Krasny",
    author_email="akrasny@ufl.edu",
    description="Psudo VPN using proxy.py",
    install_requires=['proxy.py', 'aiohttp',],
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    entry_points={
        'console_scripts': [
            'GinServer = GinVPN.gin_vpn_server:main',
            'GinConfig = GinVPN.gin_vpn_config:main'
        ],
    }
)
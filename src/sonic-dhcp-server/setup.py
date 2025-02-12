from setuptools import setup, find_packages

dependencies = [
    "psutil"
]

test_deps = [
    "pytest",
    "freezegun"
]

setup(
    name="sonic-dhcp-server",
    install_requires=dependencies,
    description="Module of SONiC built-in dhcp_server",
    version="1.0",
    url="https://github.com/Azure/sonic-buildimage",
    tests_require=test_deps,
    author="SONiC Team",
    author_email="yaqiangzhu@microsoft.com",
    setup_requires=[
        "pytest-runner",
        "wheel",
    ],
    packages=[
        "dhcp_server.common",
        "dhcp_server.dhcpservd",
        "dhcp_server.dhcprelayd"
    ],
    entry_points={
        "console_scripts": [
            "dhcprelayd = dhcp_server.dhcprelayd.dhcprelayd:main",
            "dhcpservd = dhcp_server.dhcpservd.dhcpservd:main"
        ]
    },
    classifiers=[
        "Intended Audience :: Developers",
        "Operating System :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8"
    ]
)

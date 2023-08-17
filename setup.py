import setuptools

setuptools.setup(
    name="ma-mail-sender",
    version="0.0.1",
    author="Fatih Mehmet ARSLAN",
    author_email="contact@fmarslan.com",
    description="This script enables sending emails asynchronously from Azure Service Bus. Each bus message contains a sender's email address along with SMTP configurations. The script utilizes its SMTP configuration of the message for sending emails.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    platforms="all",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Internet",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Intended Audience :: Developers",
        "Operating System :: MacOS",
        "Operating System :: POSIX",
        "Operating System :: Microsoft",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8"
    ],
    install_requires=["aiosmtplib","azure-servicebus"],
    python_requires=">=3.8, <4",
    packages=['ma_mail_sender'],
    scripts=['bin/ma-mail-sender']
)

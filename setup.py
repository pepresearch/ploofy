from setuptools import setup, find_packages
import os
import sys

# reading long description from file
with open('DESCRIPTION.txt') as file:
    long_description = file.read()


# specify requirements of your package here
REQUIREMENTS = ['tweepy','docutils>=0.3']

# some more details
CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Internet',
    'License :: OSI Approved :: GNU AFFERO GENERAL PUBLIC LICENSE Version 3, 19 November 2007',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    ]

# calling the setup function
setup(name='ploofy',
      version='1.0.0',
      description='Assist in the migration of Twitter followers and friends to your backup account.',
      long_description=long_description,
      url='https://github.com/',
      author='@omegaroyalau',
      author_email='nil',
      license='GNU AFFERO GENERAL PUBLIC LICENSE Version 3, 19 November 2007',
      packages=find_packages(),
      classifiers=CLASSIFIERS,
      install_requires=REQUIREMENTS,
      keywords='twitter'
      )

sys.argv.pop(0)
for account in sys.argv:
    if account[0] == '@':
        account = account[1:]

    account_dir = os.path.join(".", "accounts", account)
    secrets_path = os.path.join(account_dir, 'secrets.txt')

    try:
        if not os.path.exists(account_dir):
            print("Creating account directory '" + account_dir + "' for " + account)
            os.makedirs(account_dir)
    except:
        print("[ERROR]: Unable to create " + secrets_path + ".")

    try:
        if os.path.isfile(secrets_path):
            continue

        fd = open(secrets_path, 'w')
        fd.write("consumer_key = YOUR_CONSUMER_KEY\n")
        fd.write("consumer_secret = YOUR_CONSUMER_SECRET\n")
        fd.write("\n")
        fd.write("access_token = YOUR_ACCESS_TOKEN\n")
        fd.write("access_token_secret = YOUR_ACCESS_TOKEN_SECRET\n")
        fd.write("\n")
        fd.write("backup_account = YOUR_BACKUP_ACCOUNT_TWITTER_HANDLE\n")
        fd.close()
    except:
        print("[ERROR]: Unable to create " + secrets_path + ".")

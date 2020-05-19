from distutils.core import setup
setup(
    name='scalary',         # How you named your package folder (MyLib)
    packages=['scalary'],   # Chose the same as "name"
    version='0.1.3',      # Start with a small number and increase it with every change you make
    # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    license='MIT',
    # Give a short description about your library
    description='Collection of practical tools for working with image data',
    author='Andrew Pynch',                   # Type in your name
    author_email='andrewpynchbusiness@gmail.com',      # Type in your E-Mail
    # Provide either the link to your github or to your website
    url='https://github.com/andrew-pynch',
    # I explain this later on
    download_url='https://github.com/Andrew-Pynch/scalary/archive/0.1.3.tar.gz',
    keywords=['image', 'data collection', 'data processing',
              'data pipeline'],   # Keywords that define your package best
    install_requires=[            # I get to this in a second
        'pyautogui',
        'melee',
        'opencv-python',
        'pandas',
        'matplotlib',
        'numpy',
        'pillow'
    ],
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 3 - Alpha',
        # Define that your audience are developers
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)

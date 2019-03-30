from setuptools import setup, find_packages

setup(
    name='ttclustGUI',
    version='1.0.2',
    url='https://github.com/tubiana/TTClustGUI',
    license='GPL3',
    author='Thibault Tubiana',
    author_email='tubiana.thibault@gmail.com',
    description='A molecular simulation clustering program',
    platforms=["Linux", "Solaris", "Mac OS-X", "darwin", "Unix", "win32"],
    install_requires=["ttclust",
                      'RXPY>=0.1.0',
                      'wxpython==4.0.0b1',
                      'Pillow==4.3.0',
                      'psutil==5.4.2',
                      'gooey'],
    entry_points={'gui_scripts':['ttclustGUI=ttclust.ttclustGUI:main']},


    packages=find_packages(),
)

from setuptools import setup

package_name = 'burglar_alarm'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Rajesh Kumar Reddy',
    maintainer_email='rajeshkumarreddykasireddy5@gmail.com',
    description='Burglar alarm project',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'detector = burglar_alarm.detector:main',
        ],
    },
)

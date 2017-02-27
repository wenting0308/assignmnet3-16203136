from setuptools import setup

setup(name="led",
      version="0.1",
      description="Run LED for Assignment3 in COMP30670-2017",
      url="",
      author="Wen-ting, Chang",
      author_email="wen-ting.chang@ucdconnect.ie",
      licence="GPL3",
      packages=['a3_led'],
      entry_points={
        'console_scripts':['led=a3_led.main:main']
        },
      )
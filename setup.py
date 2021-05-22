# pylint: disable = C0111
from setuptools import setup

with open("README.md", "r") as f:
    DESCRIPTION = f.read()

setup(name="codequestion",
      version="1.3.0",
      author="avs & rishi",
      description="Ask coding questions directly from the terminal",
      long_description=DESCRIPTION,
      long_description_content_type="text/markdown",
      url="https://github.com/avshrudai1/RECOM-ENGINE-COLLAB",
      project_urls={
          "Documentation": "https://github.com/avshrudai1/RECOM-ENGINE-COLLAB",
          "Issue Tracker": "https://github.com/avshrudai1/RECOM-ENGINE-COLLAB/issues",
          "Source Code": "https://github.com/avshrudai1/RECOM-ENGINE-COLLAB",
      },
      download_url="https://github.com/avshrudai1/RECOM-ENGINE-COLLAB/archive/refs/heads/main.zip",
      packages=["recom"],
      package_dir={"": "src/python/"},
      keywords="python search embedding machine-learning",
      python_requires=">=3.6",
      entry_points={
          "console_scripts": [
              "recom = recom.shell:main",
          ],
      },
      install_requires=[
          "html2markdown>=0.1.7",
          "mdv>=1.7.4",
          "tqdm==4.48.0",
          "txtai>=2.0.0"
      ],
      classifiers=[
          "Operating System :: OS Independent",
          "Programming Language :: Python :: 3",
          "Topic :: Software Development",
          "Topic :: Text Processing :: Indexing",
          "Topic :: Utilities recommending code"
      ])

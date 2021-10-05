from distutils.core import setup

setup(name='trm.cline',
      version='1.0.0',
      packages = ['trm'],

      # metadata
      author='Tom Marsh',
      author_email='t.r.marsh@warwick.ac.uk',
      description="Python command line parameter handling",
      url='http://www.astro.warwick.ac.uk/',
      long_description="""
cline defines a class to handle command line scripts with parameters with defaults that get saved to disk.
""",

)


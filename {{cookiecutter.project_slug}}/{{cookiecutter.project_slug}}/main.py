# -*- python -*-
# -*- coding: utf-8 -*-
import sys
import argparse
import subprocess as sp
from lts_workflows.utils import RSTHelpFormatter

def {{ cookiecutter.project_slug }}_wrapper():
    """
{{ cookiecutter.project_slug }}
----------------------------------------

Wrapper for running {{ cookiecutter.project_slug }} workflow. Any argument
will be passed to snakemake. Consequently, this means you *must*
supply a workflow target to run the workflow.

Examples
~~~~~~~~

.. code-block:: bash

   $ {{ cookiecutter.project_slug }} all
   $ {{ cookiecutter.project_slug }} -l

Docker usage
-------------

If the docker image is used to run the workflow, this wrapper serves as
the entry point. 

Examples
~~~~~~~~

.. code-block:: bash

   $ docker run {{ cookiecutter.docker_username }}/{{ cookiecutter.project_slug }}
   $ docker run -v /path/to/workdir:/workspace -w /workspace {{ cookiecuter.docker_username }}/{{ cookiecutter.project_slug }} all
    """
    if int(sys.version[0]) != 3:
        logger.error("python version 3 required to run")
        sys.exit(1)

    parser = argparse.ArgumentParser(
        description="Workflow wrapper for {{ cookiecutter.project_slug }}",
        epilog={{ cookiecutter.project_slug }}_wrapper.__doc__,
        formatter_class = RSTHelpFormatter,
        add_help=False)
    parser.add_argument('options', nargs="*",
                        help="options and arguments passed to snakemake")
    
    args, unknown = parser.parse_known_args()
    
    if len(args.options + unknown) == 0:
        parser.print_help()
        print()
    else:
        cmd = ['snakemake'] + unknown + args.options
        sp.run(cmd)

Usage
=====

The intended usage is to include the main workflow file in a
Snakefile. See the examples in the test directory. For information on
what the workflow does, see `workflow`_.

Running
--------

.. code-block:: console
		
   $ snakemake -s Snakefile -d /path/to/workdir --configfile config.yaml all

Example Snakefile
-------------------

A minimum Snakefile example is given here:

.. code-block:: python
		
   # -*- snakemake -*-
   from {{ cookiecutter.project_slug }} import WORKFLOW

   configfile: "config.yaml"

   include: WORKFLOW


Required configuration
-------------------------------

.. note:: The configuration key nomenclature hasn't been settled yet

The following options must be set in the configuration file:

.. code-block:: yaml

   settings:
     sampleinfo: sampleinfo.csv
     runfmt: "{SM}/{SM}_{PU}"
     samplefmt: "{SM}/{SM}"
   ngs.settings:

   # list of sample identifiers
   samples:
     - sample1
     - sample2

The configuration settings 'runfmt' and 'samplefmt' describe how your
data is organized. They represent `python miniformat strings
<https://docs.python.org/3/library/string.html#formatspec>`_, where
the entries correspond to columns in the sampleinfo file; hence, in
this case, the columns **SM**, **PU**, and **DT** must be present in
the sampleinfo file.



Example sampleinfo.csv
---------------------------

.. code-block:: text
		
   SM,PU,DT,fastq
   s1,AAABBB11XX,010101,s1_AAABBB11XX_010101_1.fastq.gz
   s1,AAABBB11XX,010101,s1_AAABBB11XX_010101_2.fastq.gz
   s1,AAABBB22XX,020202,s1_AAABBB22XX_020202_1.fastq.gz
   s1,AAABBB22XX,020202,s1_AAABBB22XX_020202_2.fastq.gz
   s2,AAABBB11XX,010101,s2_AAABBB11XX_010101_1.fastq.gz
   s2,AAABBB11XX,010101,s2_AAABBB11XX_010101_2.fastq.gz

Workflow specific configuration
-----------------------------------

In addition to the required configuration, there are some
configuration settings that affect the workflow itself.

.. code-block:: yaml
		
   workflow:


Application level configuration
------------------------------------

Individual applications (e.g. app1) are located at the top level, with
sublevels corresponding to specific application rules. For instance,
the following configuration would affect settings in *app1*

.. code-block:: yaml
		
   app1:
       options: 


Additional advice
---------------------

Troubleshooting
--------------------


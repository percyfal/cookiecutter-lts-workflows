FROM continuumio/miniconda3
MAINTAINER {{ cookiecutter.full_name }} <{{ cookiecutter.email }}>
ADD . /tmp/repo
RUN apt-get upgrade -y
RUN conda update conda
RUN conda env update --name root --file /tmp/repo/lts_workflows_sm_scrnaseq/environment.yaml
RUN pip install /tmp/repo
RUN conda env create --name py2.7 --file /tmp/repo/lts_workflows_sm_scrnaseq/environment-27.yaml

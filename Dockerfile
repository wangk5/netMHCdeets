FROM python:2.7.13
MAINTAINER kjwang <wangk5@email.chop.edu>

ADD tsv2list.py /

CMD [ "python", ""./tsv2list.py" ]

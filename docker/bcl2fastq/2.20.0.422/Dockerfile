FROM continuumio/miniconda3:latest
SHELL ["/bin/bash", "-c"]

RUN apt-get update && \
apt-get install --no-install-recommends -y build-essential dpkg-dev gnupg lsb-release procps && \
export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)" && \
echo "deb http://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && \
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - && \
apt-get update && apt-get install -y google-cloud-sdk

RUN pip install --upgrade pip && \
pip install pandas

RUN mkdir /software
ADD https://raw.githubusercontent.com/klarman-cell-observatory/KCO/master/docker/cellranger/bcl2fastq2_0v2.20.0.422-2_amd64.deb /software
ADD https://raw.githubusercontent.com/klarman-cell-observatory/KCO/master/docker/monitor_script.sh /software

RUN dpkg -i /software/bcl2fastq2_0v2.20.0.422-2_amd64.deb && chmod a+rx /software/monitor_script.sh
ENV PATH=/software:$PATH
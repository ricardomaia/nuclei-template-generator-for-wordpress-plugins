FROM ubuntu:latest AS wp-plugin-template-builder
WORKDIR /app

COPY ./src/python /app

ENV GOPATH $HOME/go
ENV PATH $PATH:/go/bin:$GOPATH/bin
RUN apt update
RUN apt install -y python3
RUN apt install python3-pip -y
RUN apt install golang -y
RUN apt install -y ca-certificates
RUN update-ca-certificates
RUN apt install git -y
RUN apt install jq -y
RUN apt install curl -y
RUN apt install wget -y

# Install Python3 requirements
RUN pip3 install --upgrade pip && pip3 install -r /app/requirements.txt

# Install Nuclei
RUN go install -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest
RUN nuclei -update-templates

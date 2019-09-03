FROM microsoft/dotnet:2.1-sdk-bionic AS neo-cli-build
WORKDIR /app
COPY neo-cli/neo-cli/neo-cli.csproj ./
RUN dotnet restore
COPY ./neo-cli/neo-cli/. ./
RUN dotnet publish -c Release -o neo-cli

FROM microsoft/dotnet:2.1-runtime-bionic AS neo-cli
SHELL ["/bin/bash", "-c"]
WORKDIR /app
RUN apt update
RUN apt install -y libleveldb-dev
RUN rm /var/lib/apt/lists/* -fr
COPY --from=neo-cli-build /app/neo-cli ./
COPY ./config.json ./
COPY ./protocol.json ./

EXPOSE 10332
EXPOSE 10333

ENV DEBIAN_FRONTEND noninteractive
ENV DOTNET_CLI_TELEMETRY_OPTOUT 1

CMD ["/usr/bin/dotnet", "/app/neo-cli.dll", "/rpc"]
